# Vendor Management System

This Vendor Management System is built using Django and Django REST Framework. It manages vendor profiles, tracks purchase orders, and evaluates vendor performance metrics. Swagger UI is also integrated in understand the api structure.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

Python 3.8+
Django 3.2+
Django REST Framework

git clone https://github.com/parthsingh-pcd/vendor-management-system.git
cd vendor-management-system


## Install virtualenv (Optional)

`pip install virtualenv`

`virtualenv vmsenv`

`source vmsenv/bin/activate`  (On Windows use `vmsenv\Scripts\activate`)

## Install Reuirements

`pip install -r requirements.txt`

## Run the app

`python manage.py makemigrations`

`python manage.py migrate`

`chmod +x run.sh`

`./run.sh`

Now visit http://localhost:8080/ in your browser to view the app. (If using vmware use the ip address of the server instead of localhost)

## API Endpoints

Here is a brief overview of the API endpoints available:

### Vendor Profiles
POST /api/vendors/: Create a new vendor.

GET /api/vendors/: List all vendors.

GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.

PUT /api/vendors/{vendor_id}/: Update a vendor's details.

DELETE /api/vendors/{vendor_id}/: Delete a vendor.

### Purchase Orders
POST /api/purchase_orders/: Create a purchase order.

GET /api/purchase_orders/: List all purchase orders.

GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.

PUT /api/purchase_orders/{po_id}/: Update a purchase order.

DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

### Vendor Performance
GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.

### Swagger UI

Visit http://localhost:8080/swagger to get the complete documentation of the UI and if you want you can try the api endpoints from there as well.