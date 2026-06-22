# Containerized Flask Application with CI/CD Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?logo=github-actions)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A production-style DevOps project that demonstrates how to build, test, containerize, and deploy a Flask application using PostgreSQL, Docker, Docker Compose, and GitHub Actions.

---

## Project Overview

This project is a Flask web application integrated with a PostgreSQL database and packaged using Docker. It includes automated testing, database connectivity validation, and a Continuous Integration (CI) pipeline using GitHub Actions.

The purpose of this project is to demonstrate practical DevOps and cloud engineering skills, including:

- application containerization
- multi-service orchestration with Docker Compose
- database integration with PostgreSQL
- automated testing with `pytest`
- CI workflow automation with GitHub Actions
- deployment readiness for cloud platforms

---

## Features

- Flask web application
- PostgreSQL database integration
- Dockerized application setup
- Docker Compose for local multi-container development
- Automated testing with `pytest`
- Database connectivity checks
- GitHub Actions CI pipeline
- Deployment-ready configuration
- Clean project structure for portfolio and production-style presentation

---

## Tech Stack

- **Backend:** Flask
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Orchestration:** Docker Compose
- **CI/CD:** GitHub Actions
- **Testing:** Pytest
- **Deployment:** Render

---

## Repository Structure

```text
devops-flask-app/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── test_app.py
├── .dockerignore
├── .gitignore
├── .env.example
└── README.md

## Architecture Diagram

                +----------------------+
                |      GitHub Repo     |
                |  Source Code & CI    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  GitHub Actions CI   |
                |  - Install deps      |
                |  - Run tests         |
                |  - DB connectivity   |
                |  - Build Docker img  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |    Render Web App    |
                |   Flask Application  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Render PostgreSQL   |
                |   Managed Database   |
                +----------------------+


                
                
                CI/CD Workflow
The GitHub Actions pipeline automates the following:

Checks out the repository
Sets up Python
Installs dependencies
Runs automated tests
Starts PostgreSQL service for validation
Performs database connectivity check
Builds the Docker image
Workflow file:
.github/workflows/ci.yml

How It Works
Code is pushed to GitHub.
GitHub Actions triggers the CI pipeline automatically.
The application is validated through tests and database checks.
Docker image build is verified.
The application can run locally with Docker Compose or be deployed to Render.

Installation and Setup
1. Clone the repository
bash
git clone https://github.com/Alibras257/DevOps-flask-app.git
cd DevOps-flask-app

2. Create environment variables file
Copy .env.example to .env:

bash
cp .env.example .env
Update the values in .env to match your local or cloud PostgreSQL configuration.

3. Install dependencies locally
bash
pip install -r requirements.txt
4. Run the application locally
bash
python app.py
The app should be available at:

text
http://localhost:5000
Run with Docker
Build the Docker image
bash
docker build -t devops-flask-app .
Run the container
bash
docker run -p 5000:5000 devops-flask-app
Run with Docker Compose
To start both the Flask application and PostgreSQL together:

bash
docker-compose up --build
To stop the services:

bash
docker-compose down
Running Tests
Run tests locally with:

bash
pytest
Environment Variables
Example environment variables:

env
POSTGRES_DB=devops_db
POSTGRES_USER=devops_user
POSTGRES_PASSWORD=devops_pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
Use:

.env for local development
cloud platform environment variables for deployment
Deployment
This project is deployment-ready and suitable for:

Render
AWS
Azure
DigitalOcean
Kubernetes environments
Current deployment target: Render

API Endpoints
Example routes:

/ — main application route
/health — health check endpoint
Update this section if your project contains additional routes.

Why This Project Matters
This project highlights essential DevOps skills in a practical and portfolio-ready format:

containerizing applications with Docker
integrating application and database services
automating testing and validation in CI
preparing services for cloud deployment
maintaining a clean and reproducible development workflow
It is suitable for showcasing DevOps, Cloud, SRE, and Backend engineering capabilities.

Future Improvements
Potential next enhancements:

push Docker images to Docker Hub automatically
add full Continuous Deployment (CD)
create Kubernetes deployment manifests
provision infrastructure with Terraform
add monitoring with Prometheus and Grafana
implement centralized logging
expand automated test coverage

Author
Ibraheem Aloyinlapa
GitHub: Alibras257

License
This project is for educational and portfolio purposes.