# Project Name

This repository contains the catalog and order services for an e-commerce platform, built using FastAPI, Beanie, and MongoDB. It also includes an integration with **Bruno** for API testing.

## Installation Guide

### Prerequisites

- Python 3.8 or above
- MongoDB server running locally or on a cloud service
- Access to Bruno for API testing

 Clone the Repository
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject

Install Python and Pip
    Ensure you have Python 3.7 or later installed:
    sudo apt install python3 python3-pip -y

Set Up a Virtual Environment 
    sudo apt install python3-venv -y
    python3 -m venv fastapi_env
    source fastapi_env/bin/activate

Install FastAPI and Uvicorn
   pip install fastapi uvicorn

Install the beanie Module
   pip install beanie

Install Bruno 
   npm install -g @usebruno/cli

MongoDB
   Create a MongoDB clus

Run the services
   uvicorn catalog_service.main:app --reload --host 0.0.0.0 --port 8000
   uvicorn order_service.main:app --reload--host 0.0.0.0 --port 8080

Accessing Your App(swagger)
   http://127.0.0.1:8000/docs
   http://127.0.0.1:8080/docs

