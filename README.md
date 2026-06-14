# DevOps Flask App

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
