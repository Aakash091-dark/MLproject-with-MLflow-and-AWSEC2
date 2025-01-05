# End-to-End Machine Learning Project with MLflow

This repository contains an end-to-end machine learning project implementation leveraging MLflow for experiment tracking, model management, and deployment workflows. It also includes AWS CI/CD deployment using GitHub Actions.

## Workflows

1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update the `entity`
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline
8. Update the `main.py`
9. Update the `app.py`

---

## How to Run the Project

### Steps

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Conda Environment**

    ```bash
    conda create -n mlproj python=3.8 -y
    conda activate mlproj
    ```

3. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**

    ```bash
    python app.py
    ```

5. **Access the Application**

    Open your browser and navigate to `http://localhost:<PORT>` to access the application.

---

## MLflow Integration

MLflow is used for tracking experiments, logging metrics, and managing model deployments.

### Launch MLflow UI Locally

```bash
mlflow ui
```

Access the MLflow UI at `http://localhost:5000`.

### DAGsHub Integration

Use DAGsHub for centralized experiment tracking with MLflow.

**Run the following commands to set up environment variables:**

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow
export MLFLOW_TRACKING_USERNAME=entbappy
export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0
```

Run the script:

```bash
python script.py
```

For more details, refer to the [MLflow Documentation](https://mlflow.org/docs/latest/index.html).

---

## AWS CI/CD Deployment with GitHub Actions

### Steps

1. **Login to AWS Console**

2. **Create IAM User for Deployment**
   - Grant specific access:
     - **EC2 Access**: For virtual machine hosting.
     - **ECR Access**: To store Docker images.
   - Attach policies:
     - `AmazonEC2ContainerRegistryFullAccess`
     - `AmazonEC2FullAccess`

3. **Create ECR Repository**
   - Repository URI: `566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj`

4. **Launch EC2 Instance**
   - Use Ubuntu as the operating system.

5. **Install Docker on EC2**

    ```bash
    sudo apt-get update -y
    sudo apt-get upgrade -y
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

6. **Configure EC2 as a Self-Hosted Runner**
   - Go to GitHub > Repository > Settings > Actions > Runners > New Self-Hosted Runner.
   - Follow the commands provided for your operating system.

7. **Setup GitHub Secrets**

    ```plaintext
    AWS_ACCESS_KEY_ID=<your-access-key>
    AWS_SECRET_ACCESS_KEY=<your-secret-key>
    AWS_REGION=us-east-1
    AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com
    ECR_REPOSITORY_NAME=mlproj
    ```

8. **Deployment Workflow**
   - Build Docker image from the source code.
   - Push the Docker image to ECR.
   - Pull the image from ECR in EC2.
   - Launch the application from the Docker container in EC2.

---

## About MLflow

- **Production Grade**: Suitable for real-world deployments.
- **Experiment Tracking**: Logs metrics, parameters, and outputs.
- **Model Management**: Facilitates model tagging and deployment.

---

## Adding Images

Upload your images to the following placeholders:

1. **MLflow Experiment UI Screenshot**
   ![Upload your image here](./assets/mlflow_ui.png)

Place your images in the `assets` folder and replace the placeholders above with the correct file paths.

---

### Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DAGsHub Documentation](https://dagshub.com/)
- [AWS EC2 Documentation](https://aws.amazon.com/ec2/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- https://youtu.be/pxk1Fr33-L4?si=LwUBQ2OlDH2cwwX6
