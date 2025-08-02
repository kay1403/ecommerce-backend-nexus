# 🛒 E-Commerce Backend

This project is a backend system designed for a real-world e-commerce application. It focuses on scalability, security, and performance using Django and PostgreSQL.

## 🚀 Project Overview

This backend supports a complete e-commerce product catalog, user authentication, and robust APIs for frontend integration. It is built to simulate real-world backend development scenarios.

---

## 🎯 Project Goals

- ✅ **CRUD APIs** for managing products, categories, and users.
- ✅ **User Authentication** using JSON Web Tokens (JWT).
- ✅ **Filtering, Sorting, and Pagination** for efficient product browsing.
- ✅ **Database Optimization** via indexing and query tuning.
- ✅ **API Documentation** with Swagger/OpenAPI for ease of use.

---

## 🛠️ Technologies Used

| Tool          | Description                                  |
|---------------|----------------------------------------------|
| Django        | Backend web framework                        |
| PostgreSQL    | Relational database                          |
| JWT           | Secure token-based user authentication       |
| Swagger       | API documentation and testing                |
| Django REST Framework | For building RESTful APIs            |

---

## 🔑 Key Features

### 1. Authentication
- User registration and login using JWT.
- Token-based authentication for secured endpoints.

### 2. Product & Category Management
- CRUD operations for products and categories.
- Each product is associated with a category.

### 3. Advanced API Features
- **Filtering** by category or name (case-insensitive).
- **Sorting** by price (ascending or descending).
- **Pagination** with configurable page size.
- **Search** support via query parameters.

### 4. API Documentation
- Swagger (drf-yasg) is used for auto-generating interactive API documentation.
- Available at: `https://ecommerce-backend-nexus.onrender.com/swagger/
`

---

## 📦 API Endpoints

| Method | Endpoint              | Description                   |
|--------|-----------------------|-------------------------------|
| POST   | `/api/register/`      | Register new users            |
| POST   | `/api/login/`         | Log in and receive JWT        |
| GET    | `/api/products/`      | List all products             |
| GET    | `/api/products/<id>/` | Retrieve a single product     |
| POST   | `/api/products/`      | Create a new product          |
| PUT    | `/api/products/<id>/` | Update product details        |
| DELETE | `/api/products/<id>/` | Delete a product              |
| GET    | `/api/categories/`    | List categories               |
| GET    | `/api/orders/`        | View user orders (auth only)  |

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/kay1403/ecommerce-backend-nexus.git
cd ecommerce-backend-nexus

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

🧪 API Testing

📃 Swagger Docs
Swagger UI: https://ecommerce-backend-nexus.onrender.com/swagger/

Redoc: https://ecommerce-backend-nexus.onrender.com/redoc/



Postman:
A Postman collection can also be used to test the API endpoints.

🚀 Deployment
The project is deployed on Render and can be accessed here:

🔗 Live API

✅ Git Commit History

feat: set up Django project with PostgreSQL
feat: implement JWT user authentication
feat: add product/category CRUD endpoints
feat: enable filtering, sorting and pagination
docs: add Swagger UI for API usage
perf: optimize queries with indexes


📊 Evaluation Criteria

✅ Functionality
Full CRUD for products and categories.

JWT authentication implemented.

Search, filter, pagination logic included.

✅ Code Quality
Clean, readable code.

Proper use of serializers, views, and models.

Indexing and optimized queries.

✅ API Usability
Full Swagger documentation.

Easy-to-navigate endpoints.

✅ Git Workflow
Descriptive and regular commits.

Well-structured repository.

👤 Author
Ange Koumba
Backend Developer | Django Enthusiast
GitHub:kay1403

📬 Contact
For questions, feel free to open an issue or contact me at: angekoumba754@gmail.comm