from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from typing import List
from order_service.models import Order,OrderItem
from order_service.schemas import OrderCreate, OrderResponse,OrderItemCreate,OrderItemResponse

# Adjust the import paths based on your project structure
from user_service.models import User  # Ensure correct path
from restaurant_service.models import Restaurant  # Ensure correct path
from items_service.models import Item  # Ensure correct path

router = APIRouter()

@router.post("/orders/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    # Validate that the restaurant exists
    restaurant = await Restaurant.get(ObjectId(order.restaurant_id))
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    # Validate that the user exists
    user = await User.get(ObjectId(order.user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Initialize total price
    total_price = 0.0

    # List to hold OrderItem instances
    order_items = []

    # Validate each item and calculate total price
    for item in order.items:
        # Validate item ID format
        if not ObjectId.is_valid(item.item_id):
            raise HTTPException(status_code=400, detail=f"Invalid item_id format: {item.item_id}")

        # Fetch the item from the items collection
        db_item = await Item.get(ObjectId(item.item_id))
        if not db_item:
            raise HTTPException(status_code=404, detail=f"Item not found: {item.item_id}")

        # Ensure the item belongs to the specified restaurant
        if db_item.restaurant_id != order.restaurant_id:
            raise HTTPException(
                status_code=400,
                detail=f"Item {item.item_id} does not belong to restaurant {order.restaurant_id}"
            )

        # Calculate total price
        total_price += db_item.price * item.quantity

        # Append to order_items list
        order_items.append(OrderItem(item_id=item.item_id, quantity=item.quantity))

    # Create the Order instance
    new_order = Order(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        items=order_items,
        total_price=total_price
    )

    # Insert the order into the database
    await new_order.insert()

    # Prepare the response
    response = OrderResponse(
        id=str(new_order.id),
        user_id=new_order.user_id,
        restaurant_id=new_order.restaurant_id,
        items=[OrderItemResponse(item_id=oi.item_id, quantity=oi.quantity) for oi in new_order.items],
        total_price=new_order.total_price
    )

    return response

@router.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order_id format")

    order = await Order.get(ObjectId(order_id))
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return OrderResponse(
        id=str(order.id),
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        items=[OrderItemResponse(item_id=oi.item_id, quantity=oi.quantity) for oi in order.items],
        total_price=order.total_price
    )

@router.get("/orders/", response_model=List[OrderResponse])
async def get_orders():
    orders = await Order.find_all().to_list()
    return [
        OrderResponse(
            id=str(order.id),
            user_id=order.user_id,
            restaurant_id=order.restaurant_id,
            items=[OrderItemResponse(item_id=oi.item_id, quantity=oi.quantity) for oi in order.items],
            total_price=order.total_price
        ) for order in orders
    ]
@router.get("/orders/restaurant/{restaurant_id}", response_model=List[Order])
async def get_orders_by_restaurant(restaurant_id: str):
    try:
        # Fetch all orders with the given restaurant_id
        orders = await Order.find(Order.restaurant_id == restaurant_id).to_list()

        if not orders:
            raise HTTPException(status_code=404, detail="No orders found for this restaurant")

        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: str):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order_id format")

    order = await Order.get(ObjectId(order_id))
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    await order.delete()
    return {"message": "Order deleted successfully"}