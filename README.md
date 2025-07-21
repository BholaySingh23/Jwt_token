# 🔐 JWT-Based Authentication API for ML Services (FastAPI)

This is a mini-project built using **FastAPI** that demonstrates how to implement **JWT (JSON Web Token)** authentication and role-based authorization in a data science context. It features protected endpoints like ML model predictions and analytics dashboards.

---

## 📌 Features

- ✅ Secure JWT-based login system
- ✅ Role-based access (`free`, `premium`, `admin`)
- ✅ New user registration with hashed password storage
- ✅ ML model prediction and analytics endpoints
- ✅ Swagger UI for easy testing

---

## 📚 How JWT Authentication Works

### 🧠 What is JWT?

**JWT (JSON Web Token)** is a compact, URL-safe token used for securely transmitting information between parties. It is commonly used for authentication and authorization.

A JWT consists of three parts:
- **Header**: Algorithm & token type
- **Payload**: Claims like `username`, `plan`, and expiration time
- **Signature**: To verify that the payload was not tampered with

### 🔁 Workflow

1. A user **registers** or logs in.
2. If login is successful, the server **returns a signed JWT** containing the user's `username` and `plan`.
3. The user **sends this token** in the `Authorization` header for subsequent requests.
4. The server **validates the token**, extracts user data, and authorizes access to endpoints accordingly.

---

📡 API Endpoints
| Method | Endpoint           | Access Level  | Description                 |
| ------ | ------------------ | ------------- | --------------------------- |
| POST   | `/register`        | Public        | Register a new user         |
| POST   | `/token`           | Public        | Login and get JWT token     |
| GET    | `/predict`         | Authenticated | Get dummy model prediction  |
| GET    | `/analytics/basic` | Premium/Admin | View basic analytics report |
| GET    | `/analytics/full`  | Admin only    | View full analytics report  |



🧪 How to Use the API (Step-by-Step)
🔹 Step 1: Register a New User
Go to: POST /register

Click "Try it out"

Example input:
{
  "username": "bholay",
  "password": "test123",
  "plan": "premium"
}
Valid plan values: free, premium, admin

🔹 Step 2: Login to Get JWT Token
Go to: POST /token

Input:

username: bholay

password: test123

Response:
{
  "access_token": "your.jwt.token.here",
  "token_type": "bearer"
}

Copy the access_token.

🔹 Step 3: Authorize with JWT Token
Click "Authorize" button on the Swagger UI (top-right)

Enter:
Bearer your.jwt.token.here

🔹 Step 4: Access Protected Endpoints
Now you can access:

/predict (for all users)

/analytics/basic (for premium and admin)

/analytics/full (for admin only)

🧾 Roles & Permissions Table
| Role    | `/predict` | `/analytics/basic` | `/analytics/full` |
| ------- | ---------- | ------------------ | ----------------- |
| free    | ✅          | ❌                  | ❌                 |
| premium | ✅          | ✅                  | ❌                 |
| admin   | ✅          | ✅                  | ✅                 |


🚀 Future Improvements
Add persistent database (e.g., SQLite or PostgreSQL)

Add refresh tokens

Add real ML models

Add rate limiting per plan

👨‍💻 Author
Bholay Nath Singh
M.Tech Data Science & Engineering
Email: bholaynathsingh335619@gmail.com