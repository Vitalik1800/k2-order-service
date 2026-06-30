# 📦 K2 ERP Order Service

A REST API service for managing clients, products, and orders.

This project was developed as a technical assignment using FastAPI, SQLAlchemy, and SQLite. It follows a layered architecture with a clear separation between models, schemas, CRUD operations, business logic, and API routes.

---

## ✨ Features
👤 Create clients
📦 Create products
🛒 Create orders
📋 Retrieve all orders for a specific client
✅ Input data validation
⚠️ Error handling
📖 Interactive Swagger documentation
🐳 Docker support
🧪 Automated testing

## 🛠️ Technology Stack

| Technology | Description |
|------------|-------------|
| 🐍 Python 3.12 | Programming language |
| ⚡ FastAPI | Modern framework for building REST APIs |
| 🗄️ SQLAlchemy | ORM for database interaction |
| 💾 SQLite | Relational database |
| ✅ Pydantic | Data validation and serialization |
| 🌐 Uvicorn | ASGI server for FastAPI |
| 🧪 Pytest | Framework for automated testing |
| 🐳 Docker | Containerization platform |
| 📦 Docker Compose | Multi-container application management |

### 🏗️ Project Architecture

The project follows a layered architecture:

- **Routers** — API endpoints
- **Services** — business logic
- **CRUD** — database operations
- **Models** — SQLAlchemy models
- **Schemas** — Pydantic validation models
- **Database** — database configuration and session management 

---

## 📁 Project Structure

```text
k2-order-service/
│
├── app/
│   ├── routers/
│   │   ├── client.py
│   │   ├── product.py
│   │   └── order.py
│   │
│   ├── services/
│   │   └── order_service.py
│   │
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── tests/
│   ├── conftest.py
│   └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

### 📂 Folder Description

| Folder/File | Description |
|-------------|-------------|
| 📁 app | Main application package |
| 📁 routers | API endpoints |
| 📁 services | Business logic |
| 📄 crud.py | Database CRUD operations |
| 📄 models.py | SQLAlchemy models |
| 📄 schemas.py | Pydantic schemas |
| 📄 database.py | Database configuration |
| 📄 dependencies.py | FastAPI dependencies |
| 📁 tests | Automated tests |
| 🐳 Dockerfile | Docker image configuration |
| 🐳 docker-compose.yml | Docker Compose configuration |
| 📄 requirements.txt | Python dependencies |
| 📘 README.md | Project documentation |

---

## 🚀 Installation & Local Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/k2-order-service.git
cd k2-order-service
```

> Replace `<your-username>` with your GitHub username.

---

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 🐳 Running with Docker

### Build and start the application

```bash
docker compose up --build
```

Or, if the image has already been built:

```bash
docker compose up
```

The API will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

### Stop the application

Press **Ctrl + C** in the terminal or run:

```bash
docker compose down
```

---

### Rebuild the Docker image

If you change the application code or dependencies:

```bash
docker compose up --build
```

### 📦 Docker Requirements

Before running the project with Docker, make sure:

- Docker Desktop is installed.
- Docker Desktop is running.
- Docker Compose is available.

---

## 📖 API Documentation

After starting the application, the API documentation is available at:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Available Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Check API status | `201 OK` |
| `POST` | `/clients` | Create a new client | `201 OK` |
| `POST` | `/products` | Create a new product | `201 OK` |
| `POST` | `/orders` | Create a new order | `201 OK` |
| `GET` | `/orders/client/{client_id}` | Get all orders for a client | `201 OK` |

---

### Error Responses

The API returns appropriate HTTP status codes for invalid requests.

| Status Code | Description |
|------------|-------------|
| `201 OK` | Request completed successfully |
| `400 Bad Request` | Invalid request data |
| `404 Not Found` | Client or product not found |
| `422 Unprocessable Entity` | Validation error |

---

### Data Validation

The API validates all incoming requests.

Examples of validation:

- Client ID must be greater than **0**
- Product ID must be greater than **0**
- Quantity must be greater than **0**
- An order must contain at least one item
- Email address must be valid

---

## 📬 Example Requests

### 👤 Create Client

**Request**

```http
POST /clients
```

```json
{
  "name": "Vitalii",
  "email": "vitalii@example.com"
}
```

**Response**

```json
{
  "id": 1,
  "name": "Vitalii",
  "email": "vitalii@example.com"
}
```

---

### 📦 Create Product

**Request**

```http
POST /products
```

```json
{
  "name": "Laptop",
  "price": 1500.00
}
```

**Response**

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 1500.00
}
```

---

### 🛒 Create Order

**Request**

```http
POST /orders
```

```json
{
  "client_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    }
  ]
}
```

**Response**

```json
{
  "id": 1,
  "client_id": 1,
  "total_price": 3000.00
}
```

---

### 📋 Get Client Orders

**Request**

```http
GET /orders/client/1
```

**Response**

```json
[
  {
    "id": 1,
    "client_id": 1,
    "total_price": 3000.00
  }
]
```

---

### ❌ Client Not Found

**Request**

```http
POST /orders
```

```json
{
  "client_id": 999,
  "items": [
    {
      "product_id": 1,
      "quantity": 1
    }
  ]
}
```

**Response**

```json
{
  "detail": "Client with ID 999 not found"
}
```

---

### ❌ Product Not Found

**Request**

```http
POST /orders
```

```json
{
  "client_id": 1,
  "items": [
    {
      "product_id": 999,
      "quantity": 1
    }
  ]
}
```

**Response**

```json
{
  "detail": "Product with ID 999 not found"
}
```

---

## 🧪 Testing

The project includes automated tests built with **Pytest**.

### Run all tests

```bash
pytest
```

### Run tests with verbose output

```bash
pytest -v
```

### Current Test Coverage

The test suite verifies the following scenarios:

- ✅ API availability
- ✅ Successful client creation
- ✅ Successful product creation
- ✅ Successful order creation
- ✅ Correct total price calculation
- ✅ Retrieving client orders
- ✅ Error when client does not exist
- ✅ Error when product does not exist
- ✅ Error when the order contains no items

---

### Expected Result

```text
============================= test session starts =============================

collected 4 tests

tests/test_api.py ....                                     [100%]

============================== 4 passed ==============================
``` 

👨‍💻 Author

Vitaly
Python Developer

📧 Feel free to contact me if you have any questions, suggestions, or feedback regarding this project.

📌 Project Information
🎯 Project: K2 ERP Order Service
🏗️ Purpose: Test assignment
🚀 Framework: FastAPI
🗄️ Database: SQLite
🐳 Containerized with: Docker
🧪 Tested with: Pytest

⭐ If you found this project useful, consider giving it a star on GitHub.