#  DevOps CI/CD Pipeline with Kubernetes Deployment Strategies

This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, SonarQube, and Kubernetes (Minikube), along with implementation of multiple deployment strategies.


##  Tech Stack

- Jenkins (CI/CD)
- Docker (Containerization)
- SonarQube (Code Quality)
- Kubernetes / Minikube (Deployment)
- Python (Flask App)



##  Setup Instructions

#### 1. Start Minikube

```bash
minikube start
````
<img width="1402" height="376" alt="1_minikube_ setup" src="https://github.com/user-attachments/assets/4b27e35a-2ee0-482c-b2bd-3a1b04a7224c" />

#### 2. Use Minikube Docker Environment
```bash
eval $(minikube docker-env)
````
<img width="1402" height="476" alt="2 _rebuild_docker_image" src="https://github.com/user-attachments/assets/94d0b145-51a5-430e-9f92-f7191c34630f" />

#### 3. Build Docker Image
```bash
docker build -t aceest-app:jenkins .
````



#### 4. Verify Image
```bash
docker images
````



## Kubernetes Deployment
Apply Deployment
```bash
kubectl apply -f deployment.yaml
````
Apply Service
```bash
kubectl apply -f service.yaml
````


Check Pods
```bash
kubectl get pods
````

Check Services
```bash
kubectl get svc
````
<img width="1402" height="407" alt="3_kubectl _apply" src="https://github.com/user-attachments/assets/415b4aaa-3f6a-49b8-990e-66685ee0479a" />

Access Application
```bash
minikube service aceest-service
````
<img width="769" height="228" alt="5_app_started_in_browser" src="https://github.com/user-attachments/assets/7870a651-3882-431a-a378-7fe9421fc025" />

App started in browser

Deployment Strategies

1. Rolling Update Deployment
Update Image Version
Edit deployment.yaml:
image: aceest-app:v2
Apply Changes
```bash
kubectl apply -f deployment.yaml
````
<img width="1440" height="900" alt="6 1_Rolling_update" src="https://github.com/user-attachments/assets/7c079e7f-6b2f-4f03-8d79-89f873725b04" />


Monitor Rollout
```bash
kubectl rollout status deployment aceest-deployment
````
<img width="1440" height="900" alt="6 2_rolling_update_success" src="https://github.com/user-attachments/assets/1a512337-beb1-4f06-ae0b-83d4f0f4438a" />

Rollout success - UI
<img width="1440" height="900" alt="6 3_rolling_update_success_ui" src="https://github.com/user-attachments/assets/8fdd51b9-1c08-4391-b994-c68ce5764d86" />



2. Blue-Green Deployment
Step 1: Create Blue Deployment
```bash
kubectl apply -f blue-deployment.yaml
````
Step 2: Create Green Deployment
```bash
kubectl apply -f green-deployment.yaml
````
<img width="1440" height="900" alt="7 1_create_green_deployment_file" src="https://github.com/user-attachments/assets/c2a6238b-d8b8-4aa3-bc2c-db5477bef80f" />


Step 3: Switch Traffic
Edit service.yaml:
```bash
selector:
 app: green
````
Apply:
```bash
kubectl apply -f service.yaml
````
<img width="769" height="125" alt="7 2_apply_new_service yaml_for_green_deployment" src="https://github.com/user-attachments/assets/1748d9f5-bbc1-4275-904e-bfa8c18bd71a" />




Starting app in minikube again
<img width="1440" height="900" alt="7 3_starting_app_again_minikube" src="https://github.com/user-attachments/assets/41da91c4-7e7f-4d29-9981-1044cf50ff06" />


App started successfully in UI
<img width="769" height="125" alt="7 4_app_started_successfully_ui" src="https://github.com/user-attachments/assets/ffffccd3-2b54-4cfb-b9e9-3a15f194efcc" />

3. Canary Deployment
Step 1: Deploy Stable Version
```bash
kubectl apply -f stable-deployment.yaml
````
Step 2: Deploy Canary Version
```bash
kubectl apply -f canary-deployment.yaml
````
Step 3: Scale Canary
```bash
kubectl scale deployment canary --replicas=1
````
Executing the commands part1- Canary Deployment
<img width="1440" height="900" alt="8 1_canary_deployment_commands_1" src="https://github.com/user-attachments/assets/2a2e3937-857c-498c-845d-a184b933d9e1" />

Executing the commands part2- Canary Deployment
<img width="1440" height="900" alt="8 2_canary_commands_part-2" src="https://github.com/user-attachments/assets/e8a2272f-c4b0-40e9-a88e-9c6115ac5099" />

Version 1- output
<img width="769" height="125" alt="8 3_output version _1" src="https://github.com/user-attachments/assets/099e53f2-a83d-4bd8-a94f-21484b080d94" />


Version 2 - output
<img width="769" height="125" alt="8 4_output_version_2_ canary" src="https://github.com/user-attachments/assets/6423f101-00ff-4395-85bb-7b58020899c3" />


4. A/B Testing Deployment
Create Version A
```bash
kubectl apply -f deployment-a.yaml
````
Create Version B
```bash
kubectl apply -f deployment-b.yaml
````
Route Traffic Using Labels
Modify service:
selector:
 version: A

<img width="1440" height="900" alt="9_a:b testing" src="https://github.com/user-attachments/assets/d3f98311-4565-4298-8ece-7ec9541048ee" />


6. Shadow Deployment
Deploy Shadow Version
```bash
kubectl apply -f shadow-deployment.yaml
````
Run Alongside Production
(No traffic exposed to users, used for testing)

<img width="769" height="246" alt="10_shadow_deploymemt" src="https://github.com/user-attachments/assets/5ffe17dd-9607-4996-a8a1-02717c7faacd" />


SONARQUBE

<img width="1440" height="900" alt="11_sonarqube" src="https://github.com/user-attachments/assets/5a454329-a84d-4dc1-ae34-1092c425be22" />


Jenkins Pipeline Stages
Checkout Code
Setup Python Environment
Run Tests (pytest)
SonarQube Analysis
Build Docker Image
Deploy to Kubernetes
<img width="1440" height="692" alt="12_jenkins" src="https://github.com/user-attachments/assets/f5fe976f-8c9e-4c22-b5ce-824181a84c07" />

# Author

Vaishnavi Bhavsar
DevOps Assignment – ACEest Fitness & Gym




