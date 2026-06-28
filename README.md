# 🚀 Enterprise Monitor

A production-ready DevOps monitoring application built using **Python, Flask, Docker, Jenkins, AWS EC2, and Linux**. The application provides real-time server monitoring through a web dashboard.

---

# 📖 Overview

Enterprise Monitor helps DevOps Engineers monitor server resources and container status from a single dashboard.

The application displays:

- CPU Usage
- Memory Usage
- Disk Usage
- Docker Container Status
- Server Health
- Live Monitoring Dashboard

---

# ✨ Features

- ✅ Real-Time CPU Monitoring
- ✅ Memory Monitoring
- ✅ Disk Usage Monitoring
- ✅ Docker Container Monitoring
- ✅ Linux Server Monitoring
- ✅ Beautiful Web Dashboard
- ✅ AWS EC2 Deployment
- ✅ Jenkins CI/CD Integration
- ✅ REST API Support

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|--------|
| Linux | Operating System |
| Git | Version Control |
| GitHub | Source Code |
| Python | Backend |
| Flask | Web Framework |
| Docker | Containerization |
| Jenkins | CI/CD |
| AWS EC2 | Deployment |
| Shell Script | Automation |

---

# 🏗️ Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins Pipeline
    │
    ▼
Docker Build
    │
    ▼
AWS EC2 Server
    │
    ▼
Enterprise Monitor
    │
    ▼
Browser
```

---

# 📂 Project Structure

```
enterprise-monitor/
│
├── app.py
├── monitor.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── templates/
├── static/
├── screenshots/
└── README.md
```

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/Salim-0018/enterprise-monitor.git
```

Move into Project

```bash
cd enterprise-monitor
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Environment

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
python app.py
```

---

# 🐳 Docker

Build Image

```bash
docker build -t enterprise-monitor .
```

Run Container

```bash
docker run -d -p 5000:5000 enterprise-monitor
```

---

# ⚙️ Jenkins Pipeline

Pipeline Stages

- Pull Source Code
- Build Docker Image
- Run Container
- Deploy Application
- Health Check

---

# 📷 Screenshots

Add screenshots here after running the application.

Example:

- Dashboard
- Docker Containers
- Jenkins Pipeline
- AWS EC2
- System Monitoring

---

# 🔮 Future Improvements

- Kubernetes Deployment
- Terraform Infrastructure
- Prometheus Monitoring
- Grafana Dashboard
- Email Alerts
- Slack Notifications
- Kubernetes Auto Scaling

---

# 👨‍💻 Author

**Salim Khan**

DevOps Engineer

Linux | Git | Docker | Jenkins | AWS

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.
