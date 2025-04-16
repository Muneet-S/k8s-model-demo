# Kubernetes Model Deployment for Multi-User Serving

## Overview
A FastAPI-based model deployed on Kubernetes that demonstrates:
-  Containerized model serving
-  Load balancing across multiple pods
-  Multi-user isolation
-  Request distribution tracking

## Features
**FastAPI** REST API for predictions  
**Kubernetes Deployment** with 3 replicas  
**Load-balanced Service**  
**Automatic scaling** (HPA)  
**Health checks** (readiness/liveness probes)  

## Quick Start

### Prerequisites
- Docker ([Install](https://docs.docker.com/get-docker/))
- Minikube ([Install](https://minikube.sigs.k8s.io/docs/start/))
- kubectl ([Install](https://kubernetes.io/docs/tasks/tools/))

### Step 1: Start Minikube
```bash
minikube start --driver=docker

# Set Docker to use Minikube's environment
eval $(minikube docker-env)

# Build the image
docker build -t fastapi-model:latest .

# Apply configurations
kubectl apply -f model-deployment.yaml
kubectl apply -f model-service.yaml

# Verify deployment
kubectl get pods -w

# Port-forward to access the service
kubectl port-forward svc/model-service 8080:80 &

# Send test requests
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"user_id": "interviewer", "input": 5}'

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Client   │───▶│  Kubernetes     │───▶│  FastAPI Model  │
│                 │    │  Service (LB)   │    │  (Pods)         │
└─────────────────┘    └─────────────────┘    └─────────────────┘

Files
model_server.py - FastAPI application

Dockerfile - Container configuration

model-deployment.yaml - Kubernetes deployment

model-service.yaml - Kubernetes service

