# Scientific Calculator DevOps Pipeline

This project implements a CI/CD pipeline for a Python-based scientific calculator application using Jenkins, Docker, Ansible, and ngrok. The pipeline automates building, testing, and deploying the calculator.

## Prerequisites
- **Python 3.11+**: For running the calculator and tests.
- **Docker**: To build and push container images.
- **Jenkins**: For pipeline automation.
- **Ansible**: For local deployment.
- **ngrok**: For exposing Jenkins to GitHub webhooks.
- **GitHub Account**: For version control.
- **Docker Hub Account**: For image storage.

## Setup Instructions
1. **Clone Repository**:
   ```bash
   git clone https://github.com/anirudh-pathaneni/ScientificCalculator-DevOps.git
   cd ScientificCalculator-DevOps
   ```

2. **Install Dependencies**:
   - Install Python: `brew install python` (macOS) or equivalent.
   - Install Docker: Download from https://www.docker.com/products/docker-desktop.
   - Install Jenkins: `brew install jenkins-lts` (macOS) or use Docker.
   - Install Ansible: `pip3 install ansible && ansible-galaxy collection install community.docker`.
   - Install ngrok: Follow https://ngrok.com/download.

3. **Configure Jenkins**:
   - Start Jenkins: `brew services start jenkins-lts`.
   - Access at `http://localhost:8080`, set up admin user.
   - Install plugins: GitHub Integration, Docker Pipeline, Email Extension.
   - Configure GitHub webhook in `Manage Jenkins` > `Configure System`.
   - Update `jenkins-lts.plist` for tool paths

4. **Set Up ngrok**:
   - Run: `ngrok http 8080 --url=https://your-static-ngrok-url.ngrok-free.dev`.
   - Add webhook in GitHub repo: `Settings` > `Webhooks` > `Add webhook`, set Payload URL to `https://your-static-ngrok-url.ngrok-free.dev/github-webhook/`, select "Just the push event".

5. **Configure Pipeline**:
   - Create a pipeline job in Jenkins, set SCM to `https://github.com/anirudh-pathaneni/ScientificCalculator-DevOps.git`, branch `main`.
   - Enable "GitHub hook trigger for GITScm polling".

## Pipeline Overview
- **Push to GitHub**: Triggers webhook on code push.
- **Webhook**: Notifies Jenkins via ngrok.
- **Jenkins Pipeline** (`Jenkinsfile`):
  - Pulls repo.
  - Runs tests (`python3 -m unittest test_scalculator.py`).
  - Builds Docker image (`5unnysunny/scalculator:<BUILD_NUMBER>`).
  - Pushes to Docker Hub.
  - Deploys locally via Ansible (`ansible/deploy.yml`).

## Usage
- **Run Locally**:
  ```bash
  python3 scalculator.py
  ```
- **Test Pipeline**:
  - Manual: Jenkins > `scalculator-pipeline` > `Build Now`.
  - Automated: `git commit -m "Test change" && git push origin main`.
- **Verify Deployment**:
  - Check container: `docker ps`.
  - Interact: `docker exec -it scientific-calculator python scalculator.py`.
  - Check Docker Hub: https://hub.docker.com/r/5unnysunny/scalculator.

## Files
- `scalculator.py`: Scientific calculator code.
- `test_scalculator.py`: Unit tests.
- `Dockerfile`: Defines container image.
- `Jenkinsfile`: Pipeline script.
- `ansible/deploy.yml`: Ansible playbook for deployment.
- `ansible/inventory`: Host configuration for Ansible

## Links
- GitHub: https://github.com/anirudh-pathaneni/ScientificCalculator-DevOps
- Docker Hub: https://hub.docker.com/r/5unnysunny/scalculator