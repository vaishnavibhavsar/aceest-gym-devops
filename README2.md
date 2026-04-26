# 🚀 DevOps CI/CD Pipeline with Kubernetes Deployment Strategies

This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, SonarQube, and Kubernetes (Minikube), along with implementation of multiple deployment strategies.

---

## 📌 Tech Stack

- Jenkins (CI/CD)
- Docker (Containerization)
- SonarQube (Code Quality)
- Kubernetes / Minikube (Deployment)
- Python (Flask App)

---

## ⚙️ Setup Instructions

### 1. Start Minikube

```bash
minikube start
2. Use Minikube Docker Environment
eval $(minikube docker-env)
<img src="images/Assignment_2_screenshots_minikube_setup.png" width="800">

3. Build Docker Image
docker build -t aceest-app:jenkins .
4. Verify Image
docker images
📸 Screenshot Placeholder

Add screenshot of Docker image here

☸️ Kubernetes Deployment
Apply Deployment
kubectl apply -f deployment.yaml
Apply Service
kubectl apply -f service.yaml
Check Pods
kubectl get pods
Check Services
kubectl get svc
Access Application
minikube service aceest-service
📸 Screenshot Placeholder

Add screenshot of running application here

🚀 Deployment Strategies
1️⃣ Rolling Update Deployment
Update Image Version

Edit deployment.yaml:

image: aceest-app:v2
Apply Changes
kubectl apply -f deployment.yaml
Monitor Rollout
kubectl rollout status deployment aceest-deployment
📸 Screenshot Placeholder

Add screenshot of rolling update here

2️⃣ Blue-Green Deployment
Step 1: Create Blue Deployment
kubectl apply -f blue-deployment.yaml
Step 2: Create Green Deployment
kubectl apply -f green-deployment.yaml
Step 3: Switch Traffic

Edit service.yaml:

selector:
  app: green

Apply:

kubectl apply -f service.yaml
📸 Screenshot Placeholder

Add screenshot of blue-green switching here

3️⃣ Canary Deployment
Step 1: Deploy Stable Version
kubectl apply -f stable-deployment.yaml
Step 2: Deploy Canary Version
kubectl apply -f canary-deployment.yaml
Step 3: Scale Canary
kubectl scale deployment canary --replicas=1
📸 Screenshot Placeholder

Add screenshot of canary deployment here

4️⃣ A/B Testing Deployment
Create Version A
kubectl apply -f deployment-a.yaml
Create Version B
kubectl apply -f deployment-b.yaml
Route Traffic Using Labels

Modify service:

selector:
  version: A
📸 Screenshot Placeholder

Add screenshot of A/B testing here

5️⃣ Shadow Deployment
Deploy Shadow Version
kubectl apply -f shadow-deployment.yaml
Run Alongside Production

(No traffic exposed to users, used for testing)

📸 Screenshot Placeholder

Add screenshot of shadow deployment here

🔁 Jenkins Pipeline Stages
Checkout Code
Setup Python Environment
Run Tests (pytest)
SonarQube Analysis
Build Docker Image
Deploy to Kubernetes
📸 Screenshot Placeholder

Add Jenkins pipeline success screenshot here

📊 SonarQube Analysis
Code quality checks
Bugs & vulnerabilities detection
Maintainability metrics
📸 Screenshot Placeholder

Add SonarQube dashboard screenshot here

✅ Conclusion

This project successfully demonstrates:

CI/CD pipeline automation
Containerization using Docker
Kubernetes deployments
Multiple deployment strategies used in real-world DevOps

👩‍💻 Author
Vaishnavi Bhavsar
