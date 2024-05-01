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

`cd vendor_management`

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

#### Create a New Vendor

- **POST /api/vendors/**
  - **Description**: Create a new vendor profile.
  - **Payload**:
    ```json
    {
      "name": "Vendor Name",
      "contact_details": "Contact Information",
      "address": "Vendor Address",
      "vendor_code": "V001"
    }
    ```
  - **Example Request**:
    ```bash
    curl -X POST http://localhost:8080/api/vendors/ \
         -H 'Content-Type: application/json' \
         -d '{
               "name": "Vendor Name",
               "contact_details": "Contact Information",
               "address": "Vendor Address",
               "vendor_code": "V001"
             }'
    ```

#### List All Vendors

- **GET /api/vendors/**
  - **Description**: Retrieve a list of all vendors in the system.
  - **Example Request**:
    ```bash
    curl -X GET http://localhost:8080/api/vendors/
    ```

#### Retrieve a Specific Vendor's Details

- **GET /api/vendors/{vendor_id}/**
  - **Description**: Retrieve detailed information about a specific vendor.
  - **Example Request**:
    ```bash
    curl -X GET http://localhost:8080/api/vendors/1/
    ```

#### Update a Vendor's Details

- **PUT /api/vendors/{vendor_id}/**
  - **Description**: Update details of a specific vendor.
  - **Payload**:
    ```json
    {
      "name": "Updated Vendor Name",
      "contact_details": "Updated Contact Information",
      "address": "Updated Address",
      "vendor_code": "V001"
    }
    ```
  - **Example Request**:
    ```bash
    curl -X PUT http://localhost:8080/api/vendors/1/ \
         -H 'Content-Type: application/json' \
         -d '{
               "name": "Updated Vendor Name",
               "contact_details": "Updated Contact Information",
               "address": "Updated Address",
               "vendor_code": "V001"
             }'
    ```

#### Delete a Vendor

- **DELETE /api/vendors/{vendor_id}/**
  - **Description**: Delete a specific vendor from the system.
  - **Example Request**:
    ```bash
    curl -X DELETE http://localhost:8080/api/vendors/1/
    ```

### Purchase Orders

#### Create a New Purchase Order

- **POST /api/purchase_orders/**
  - **Description**: Create a new purchase order.
  - **Payload**:
    ```json
    {
      "po_number": "PO123456",
      "vendor": 1,
      "order_date": "2024-05-01T14:00:00Z",
      "delivery_date": "2024-05-15T14:00:00Z",
      "items": [
        {
          "item": "Item 1",
          "quantity": 10,
          "unit_price": 100
        },
        {
          "item": "Item 2",
          "quantity": 5,
          "unit_price": 200
        }
      ],
      "quantity": 15,
      "status": "PENDING"
    }
    ```
  - **Example Request**:
    ```bash
    curl -X POST http://localhost:8080/api/purchase_orders/ \
         -H 'Content-Type: application/json' \
         -d '{
               "po_number": "PO123456",
               "vendor": 1,
               "order_date": "2024-05-01T14:00:00Z",
               "delivery_date": "2024-05-15T14:00:00Z",
               "items": [{"item": "Item 1", "quantity": 10, "unit_price": 100}, {"item": "Item 2", "quantity": 5, "unit_price": 200}],
               "quantity": 15,
               "status": "PENDING"
             }'
    ```

#### List All Purchase Orders

- **GET /api/purchase_orders/**
  - **Description**: Retrieve a list of all purchase orders in the system.
  - **Example Request**:
    ```bash
    curl -X GET http://localhost:8080/api/purchase_orders/
    ```

#### Retrieve Details of a Specific Purchase Order

- **GET /api/purchase_orders/{po_id}/**
  - **Description**: Retrieve detailed information about a specific purchase order.
  - **Example Request**:
    ```bash
    curl -X GET http://localhost:8080/api/purchase_orders/123/
    ```

#### Update a Purchase Order

- **PUT /api/purchase_orders/{po_id}/**
  - **Description**: Update details of a specific purchase order.
  - **Payload**:
    ```json
    {
      "order_date": "2024-05-01T15:00:00Z",
      "delivery_date": "2024-05-20T15:00:00Z",
      "items": [
        {
          "item": "Item 1",
          "quantity": 20,
          "unit_price": 100
        }
      ],
      "quantity": 20,
      "status": "completed"
    }
    ```
  - **Example Request**:
    ```bash
    curl -X PUT http://localhost:8080/api/purchase_orders/123/ \
         -H 'Content-Type: application/json' \
         -d '{
               "order_date": "2024-05-01T15:00:00Z",
               "delivery_date": "2024-05-20T15:00:00Z",
               "items": [{"item": "Item 1", "quantity": 20, "unit_price": 100}],
               "quantity": 20,
               "status": "completed"
             }'
    ```

#### Delete a Purchase Order

- **DELETE /api/purchase_orders/{po_id}/**
  - **Description**: Delete a specific purchase order from the system.
  - **Example Request**:
    ```bash
    curl -X DELETE http://localhost:8080/api/purchase_orders/123/
    ```

##### Acknowledging a Purchase Order

To acknowledge a purchase order, send a POST request to `/api/purchase_orders/{po_id}/acknowledge` with optional JSON payload containing the quality rating. Here is an example request:

```bash
curl -X POST http://localhost:8080/api/purchase_orders/1/acknowledge \
     -H 'Content-Type: application/json' \
     -d '{"status": "COMPLETED","quality_rating": 8.5}'
```

### Vendor Performance

- **GET /api/vendors/{vendor_id}/performance**
  - **Description**: Retrieve performance metrics for a specific vendor. These metrics include on-time delivery rate, quality rating average, average response time, and fulfillment rate.
  - **Example Request**:
    ```bash
    curl -X GET http://localhost:8080/api/vendors/1/performance
    ```

### Swagger UI

Visit http://localhost:8080/swagger to get the complete documentation of the UI and if you want you can try the api endpoints from there as well.