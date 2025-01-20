# Project Name

This repository contains the catalog and order services for an e-commerce platform, built using FastAPI, Beanie, and MongoDB. It also includes an integration with **Bruno** for API testing.

## Installation Guide

### Prerequisites

- Python 3.8 or above
- MongoDB server running locally or on a cloud service
- Access to Bruno for API testing

### Steps to Set Up
```bash

1. git clone https://github.com/yourusername/yourproject.git
   cd yourproject

2. Install Python and Pip
   Ensure you have Python 3.7 or later installed. Use the following commands:
   sudo apt install python3 python3-pip -y

3. Set Up a Virtual Environment
    sudo apt install python3-venv -y
    python3 -m venv fastapi_env
    source fastapi_env/bin/activate

4. Install FastAPI and Uvicorn
    pip install fastapi uvicorn

5. Install the Beanie Module
     pip install beanie

6. Install Bruno
    npm install -g @usebruno/cli

7. Set Up MongoDB
     Go to MongoDB Atlas and sign up or log in.

    Create a new project and cluster:
       -> Click "Create a Cluster" and select a free or paid plan.
       -> Choose your cloud provider and region.
       -> Complete the setup and create your cluster.

    Whitelist your IP address:
       -> Go to the Network Access tab in Atlas.
       -> Click Add IP Address and add your current IP or allow access from anywhere (0.0.0.0/0).

    Create a database user:
       -> Go to the Database Access tab.
       -> Click Add New Database User and set a username and password.

    Connect to your cluster:
       -> Go to the Clusters tab.
       -> Click Connect and select Connect Your Application.
       -> Copy the connection string. Replace <username> and <password> with your database credentials.
       -> Use the connection string in your application: mongodb_uri = "mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority"

8. Run the Catalog Service
     uvicorn catalog_service.main:app --reload --host 0.0.0.0 --port 8000

9. Run the Order Service
     uvicorn order_service.main:app --reload --host 0.0.0.0 --port 8080

10. Accessing Your App
    You can access the Swagger UI for the services at the following URLs:
    Catalog Service: http://127.0.0.1:8000/docs
    Order Service: http://127.0.0.1:8080/docs

11. Running Bruno Files
    The Bruno files are located in the bruno/ directory. To test APIs:
    Open Bruno.
    Load the bruno/ folder as a collection.
    Test all the APIs directly using Bruno.

