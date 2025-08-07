# Self-Hosted GitLab CI/CD Pipeline for Flask App

This project demonstrates how to set up a **self-hosted GitLab CE instance** with a **GitLab Runner** to automate CI/CD pipelines for a containerized Flask web application.

---

<img width="1879" height="1009" alt="image" src="https://github.com/user-attachments/assets/34318554-8180-41d3-9e78-2f9ef5a9a748" />


## 🚀 Project Overview

- **Host GitLab CE locally using Docker**
- **Register a GitLab Runner** to execute CI/CD jobs
- Build and test a Dockerized Flask app using `.gitlab-ci.yml`
- Showcase skills in **CI/CD automation**, **Docker**, and **self-hosting**

---

## 🛠️ Technologies & Tools

- [GitLab Community Edition (CE)](https://about.gitlab.com/install/)
- [GitLab Runner](https://docs.gitlab.com/runner/)
- Docker & Docker Compose
- Flask (Python Web Framework)
- pytest (for testing Flask app)
- Git & YAML

---

## 📦 Project Structure

```

.
├── flask-app/               # Your Flask app source code
│   ├── app.py
│   ├── requirements.txt
│   └── tests/
│       └── test\_app.py
├── gitlab/                  # Docker Compose setup for GitLab CE
│   └── docker-compose.yml
├── .gitlab-ci.yml           # GitLab CI/CD pipeline configuration
└── README.md

````

---

## 🔧 Setup Instructions

### 1. Run GitLab CE locally with Docker

```bash
cd gitlab
docker-compose up -d
````

* Access GitLab UI at: `http://localhost:8929`
* Log in as `root` user and reset password if needed

### 2. Register GitLab Runner

* On your server (or container), install GitLab Runner
* Register runner with tag `docker`:

```bash
sudo gitlab-runner register
```

* Use your GitLab URL and registration token
* Choose `docker` executor and Docker image `docker:latest`

### 3. Prepare your Flask app

* Write your Flask app in `flask-app/`
* Containerize the app with a Dockerfile
* Write tests using `pytest`

### 4. Configure CI/CD pipeline

* Use `.gitlab-ci.yml` in project root:

```yaml
stages:
  - build
  - test

variables:
  IMAGE_NAME: flask-ci-app

build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t $IMAGE_NAME .
  tags:
    - docker

test:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pytest tests/
  tags:
    - docker
```

### 5. Push your code and watch the pipeline run!

---

## 📁 .gitignore

Make sure to ignore sensitive and large GitLab folders:

```
gitlab/config/
gitlab/data/
gitlab/logs/
__pycache__/
*.pyc
.env
.env.*
.vscode/
```

---

## 🎯 Skills Demonstrated

* Setting up and managing a self-hosted GitLab instance
* Registering and configuring GitLab Runners
* Building Docker images and running containerized applications
* Writing and configuring CI/CD pipelines with GitLab CI
* Python Flask app development and testing
* Managing Linux permissions and Docker volumes

---

## 🔗 Useful Links

* [GitLab CE Docker Image](https://hub.docker.com/r/gitlab/gitlab-ce)
* [GitLab Runner Documentation](https://docs.gitlab.com/runner/)
* [Flask Official Documentation](https://flask.palletsprojects.com/)
* [pytest Documentation](https://docs.pytest.org/)
