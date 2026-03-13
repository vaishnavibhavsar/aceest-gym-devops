# ACEest Fitness & Gym – DevOps CI/CD Pipeline

## Project Overview

This project demonstrates the implementation of a **modern DevOps workflow** for the ACEest Fitness & Gym management API.
The goal is to ensure **code quality, automated testing, containerized deployment, and continuous integration** using industry-standard tools.

The application is built using **Python Flask** and provides simple REST APIs to manage gym members.

This project implements the following DevOps practices:

* Version Control using **Git & GitHub**
* Automated Testing using **Pytest**
* Containerization using **Docker**
* Continuous Integration using **GitHub Actions**
* Build Automation using **Jenkins**

---

# Application Features

The Flask API provides the following endpoints:

| Endpoint   | Method | Description                   |
| ---------- | ------ | ----------------------------- |
| `/`        | GET    | Displays welcome message      |
| `/health`  | GET    | Returns API health status     |
| `/members` | GET    | Retrieves list of gym members |
| `/members` | POST   | Adds a new gym member         |

Example JSON response:

```json
{
  "message": "Welcome to ACEest Fitness & Gym API"
}
```

---

# Project Structure

```
aceest-gym-devops
│
├── app.py
├── requirements.txt
├── test_app.py
├── Dockerfile
├── README.md
│
└── .github
    └── workflows
        └── main.yml
```

Description of files:

| File               | Purpose                       |
| ------------------ | ----------------------------- |
| `app.py`           | Main Flask API application    |
| `requirements.txt` | Python dependencies           |
| `test_app.py`      | Unit tests using Pytest       |
| `Dockerfile`       | Containerization instructions |
| `main.yml`         | GitHub Actions CI pipeline    |
| `README.md`        | Project documentation         |

---

# Technologies Used

* Python
* Flask
* Pytest
* Docker
* GitHub Actions
* Jenkins
* Git / GitHub

---

# Local Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/aceest-gym-devops.git
cd aceest-gym-devops
```

## 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the application

```bash
python app.py
```

The application will start on:

```
http://localhost:5000
```

---

# API Usage Examples

## Check API health

```
GET /health
```

Example response:

```json
{
  "status": "healthy"
}
```

---

## View members

```
GET /members
```

Example response:

```json
[]
```

---

## Add a new member

Use **POST request**:

```
POST /members
```

Example request body:

```json
{
"name": "Rahul",
"membership": "Gold"
}
```

Example response:

```json
{
"name": "Rahul",
"membership": "Gold"
}
```

---

# Running Unit Tests

This project uses **Pytest** for automated testing.

Run tests manually:

```bash
pytest
```

Expected output:

```
3 passed in 0.02s
```

These tests ensure that:

* The API is accessible
* Core endpoints work correctly
* The application loads successfully

---

# Docker Containerization

Docker is used to package the application along with its dependencies, ensuring it runs consistently across different environments.

## Build Docker image

```bash
docker build -t aceest-gym-app .
```

## Run Docker container

```bash
docker run -p 5000:5000 aceest-gym-app
```

The API will be available at:

```
http://localhost:5000
```

---

# Continuous Integration – GitHub Actions

The project includes a **GitHub Actions workflow** that automatically runs whenever code is pushed to the repository.

The pipeline performs the following steps:

1. Checkout repository
2. Install Python dependencies
3. Run syntax checks
4. Execute Pytest unit tests
5. Build Docker image

Workflow file location:

```
.github/workflows/main.yml
```

Example pipeline stages:

```
✔ Install dependencies
✔ Run tests
✔ Build Docker image
```

This ensures that every commit maintains **code quality and application stability**.

---

# Jenkins Integration

Jenkins is used as an additional **build automation tool**.

The Jenkins pipeline performs:

1. Pull latest code from GitHub repository
2. Install dependencies
3. Run automated tests
4. Build Docker image

This provides an extra layer of verification before deployment.

---

# CI/CD Workflow Architecture

```
Developer
   │
   │ push code
   ▼
GitHub Repository
   │
   ▼
GitHub Actions Pipeline
   │
   ├── Install dependencies
   ├── Run tests
   └── Build Docker image
   │
   ▼
Jenkins Build Server
   │
   └── Build verification
```

This workflow ensures:

* Continuous Integration
* Automated testing
* Consistent deployment environment

---

# Screenshots

*(Add screenshots here if required)*

Example sections:

## Docker Build

![Docker Build](images/1_basic setup.png)

## Running Container

![Docker Container](images/docker-run.png)

## API Endpoint Test

![API Test](images/api-test.png)

---

# Future Improvements

Potential enhancements for this project include:

* Adding a database (PostgreSQL)
* Implementing authentication
* Deploying to cloud platforms
* Adding Kubernetes for orchestration

---

# Conclusion

This project demonstrates the implementation of a **complete DevOps pipeline** for a Python-based web application.

By integrating **version control, automated testing, containerization, and CI/CD pipelines**, the project ensures that the application can be developed, tested, and deployed efficiently with high reliability.

---

# Author

Vaishnavi Bhavsar
DevOps Assignment – ACEest Fitness & Gym

