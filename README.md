# Mini Cloud Project – Docker, Flask, PostgreSQL, Redis, Nginx

## Description
This project is a cloud application based on a microservices architecture containerized with Docker.  
The application allows managing tasks (todo-service) and displaying statistics (stats-service).  
The system uses PostgreSQL for the database, Redis for caching, Nginx as a reverse proxy and load balancer, cAdvisor for monitoring, and GitHub Actions for CI/CD.

---

## Architecture
The project architecture is composed of:

- Nginx: Reverse proxy + Load balancer + HTTPS
- todo-service: Main application (Flask) – 3 instances
- stats-service: Statistics service (Flask)
- PostgreSQL: Database
- Redis: Cache
- cAdvisor: Monitoring
- GitHub Actions: CI/CD
- Docker Hub: Docker image storage

The client accesses the application via Nginx (HTTP or HTTPS), then Nginx redirects the requests to the internal services.

---

## Technologies Used
- Docker
- Docker Compose
- Python Flask
- PostgreSQL
- Redis
- Nginx
- GitHub Actions
- Docker Hub
- cAdvisor

---

## Run the Project
### 1. Clone the project
```bash
git clone https://github.com/NermineKouki1/mini-projet-cloud.git
cd mini-projet-cloud
```

### 2. Start the containers
```bash
docker compose up --build
```

### 3. Scalability / Load Balancing (multiple instances):
Load balancing is handled by Nginx between multiple instances of the todo-service.
```bash
docker compose up --scale todo-service=3
```

### 4. Access to services
| Service             | URL                                                        |
| ------------------- | ---------------------------------------------------------- |
| HTTP Application    | http://localhost:8080                                      |
| HTTPS Application   | https://localhost:8443                                     |
| Statistics          | http://localhost:8080/stats                                |
| Monitoring cAdvisor | http://localhost:8081                                      |
| PostgreSQL          | localhost:5432                                             |
| Redis               | localhost:6379                                             |

### 5. Volumes
The project uses a Docker volume for PostgreSQL to save data:
```bash
mini-projet-cloud_db-data
```

### 6. CI/CD

The project uses GitHub Actions to:
Build Docker images
Push Docker images to Docker Hub
Automate deployment

The CI/CD file is located here: ( .github/workflows/docker-ci.yml )
