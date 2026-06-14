# DevOps Flask App

![CI Pipeline](https://github.com/Alibras257/DevOps-flask-app/actions/workflows/ci.yml/badge.svg)

A production-ready DevOps practice project built with Flask, PostgreSQL, Docker, Docker Compose, GitHub Actions, and Render.

## Overview

This project demonstrates a complete DevOps workflow for a simple Python web application. It includes:

- application development with Flask
- containerization with Docker
- multi-service orchestration with Docker Compose
- PostgreSQL database integration
- automated testing with pytest
- CI pipeline with GitHub Actions
- cloud deployment on Render

## Live Demo

Base URL: `https://devops-flask-app-l7ko.onrender.com`

### Available Endpoints

- `/` → Home page
- `/health` → Health check endpoint
- `/db-check` → Database connectivity check

## Tech Stack

- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions
- pytest
- Gunicorn
- Render

## Project Structure

```bash
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
└── README.md


## Architecture Diagram

```text
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
                |   Flask + Gunicorn   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Render PostgreSQL   |
                |   Managed Database   |
                +----------------------+


## Cleaner plain-text version

```md
## Architecture Overview

- **GitHub Repository**
  - stores source code
  - stores Docker configuration
  - stores GitHub Actions workflow

- **GitHub Actions**
  - installs dependencies
  - runs automated tests
  - checks database connectivity
  - builds Docker image

- **Render Web Service**
  - deploys the Flask application
  - runs the app using Gunicorn

- **Render PostgreSQL**
  - provides the managed database
  - connects to the web app using environment variables
