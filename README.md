# Cars Dealership – Full-Stack Capstone Project

## Project Overview
This project was completed as part of the **Full-Stack Development Capstone**.  
The goal was to build a **responsive, cloud-native web application** for *Cars Dealership*, a national car retailer in the United States.

The application allows users to:
- View car dealership branches
- Register and log in
- View and submit dealer reviews
- Analyze review sentiment
- Filter dealers by state
- View car makes and models

The project follows **microservices architecture** and demonstrates **end-to-end full-stack development**, including frontend, backend, containerization, CI/CD, and cloud deployment.

---

## Technology Stack

### Frontend
- React
- HTML5 / CSS3
- Bootstrap

### Backend
- Django (Main application & Admin)
- Flask (Sentiment Analysis Microservice)
- Node.js (Dealer & Review APIs)

### Databases
- MongoDB (Dealer & Review data)
- SQLite (Django authentication & admin)

### DevOps & Cloud
- Docker
- Kubernetes
- IBM Cloud Code Engine
- GitHub Actions (CI/CD)

---

## Application Features
- User registration and authentication
- Dealer listing and filtering by state
- Dealer review creation and display
- Sentiment analysis on submitted reviews
- Django admin panel for managing data
- RESTful APIs using Flask and Node.js
- Fully containerized microservices
- Deployed on IBM Cloud Code Engine

---

## Microservices Architecture
The application is composed of multiple independently deployed microservices:

1. **Django Backend**
   - User authentication
   - Admin dashboard
   - API gateway

2. **Node.js Service**
   - Dealer information
   - Reviews management

3. **Flask Service**
   - Sentiment analysis for reviews

4. **React Frontend**
   - User interface
   - Dealer browsing and reviews

---

## CI/CD Pipeline
- GitHub Actions used for:
  - Code checkout
  - Build and test
  - Docker image creation
  - Container registry push
  - Deployment to IBM Cloud Code Engine

---

## Deployment
The application is deployed on **IBM Cloud Code Engine** using container images.  
Each microservice is independently deployed and scaled.

---

## Repository Structure
