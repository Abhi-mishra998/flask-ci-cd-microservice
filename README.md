
# flask-ci-cd-microservice
# 🚀 Flask CI/CD Microservice with Docker & Jenkins

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-green?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker)
![Jenkins](https://img.shields.io/badge/Jenkins-Automation-red?style=for-the-badge&logo=jenkins)

## 📌 Overview
This project demonstrates a **Flask-based microservice** deployed using **Docker** and automated with **Jenkins CI/CD**.  
It includes:
- REST API endpoints
- Unit testing with `pytest`
- Automated build, test, and deploy pipeline
- Containerization for consistent environments

## ⚙️ Tech Stack
- **Language:** Python 3.12
- **Framework:** Flask 2.3
- **Containerization:** Docker
- **Automation:** Jenkins
- **Testing:** Pytest

## 📂 Project Structure
```
📦 flask-ci-cd
├── 📄 app.py              # Main Flask app
├── 📄 requirements.txt    # Python dependencies
├── 📄 test_app.py         # Unit tests
├── 📄 Dockerfile          # Docker image configuration
├── 📄 Jenkinsfile         # CI/CD pipeline script
└── 📄 README.md           # Project documentation
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/flask-ci-cd.git
cd flask-ci-cd
```

### 2️⃣ Build & Run with Docker
```bash
docker build -t flask-ci-cd .
docker run -p 5000:5000 flask-ci-cd
```

### 3️⃣ Access the App
- **Home:** `http://localhost:5000/`
- **Health Check:** `http://localhost:5000/health`

## 🧪 Running Tests
```bash
pytest
```

## 🔄 CI/CD with Jenkins
This project includes a `Jenkinsfile` for:
- Installing dependencies
- Running tests
- Building Docker images
- Deploying to the target environment



## 📜 License
This project is licensed under the **MIT License**.

## ✨ Author
**Abhishek Mishra**  
💼 [LinkedIn](https://www.linkedin.com/in/abhishek-mishra-49888123b/) | 📧 abhimishra9896@gmail.com
> _Automating deployment is not just a skill — it's the power to deliver faster with confidence._


>>> a88245f (Initial commit - Advanced Flask CI/CD Microservice)
