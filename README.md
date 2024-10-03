# Kidney Disease Classification with MLflow & DVC

This project uses Deep Learning to classify kidney disease images, and incorporates MLflow and DVC for experiment tracking and pipeline orchestration. Additionally, it can be deployed to AWS using GitHub Actions for continuous integration and delivery (CI/CD).

## Workflows

   1. Update `config.yaml`
   2. Update `secrets.yaml` [Optional]
   3. Update `params.yaml`
   4. Update the entity
   5. Update the configuration manager in `src/config`
   6. Update the components
   7. Update the pipeline
   8. Update `main.py`
   9. Update `dvc.yaml`
   10. Update `app.py`

## How to Run

### Step 1: Clone the Repository

```bash
git clone github.com:Kamal934/KidneyDisease-Classification-DL.git
cd KidneyDisease-Classification-DL
```

### Step 2: Create a Conda Environment

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Access the Application

Open your local host and port to access the running application.

## MLflow Setup

### Run the MLflow UI

```bash
mlflow ui
```

### Track Experiments on Dagshub

Set environment variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/societylens0/KidneyDisease-Classification-DL.mlflow
export MLFLOW_TRACKING_USERNAME=societylens0
export MLFLOW_TRACKING_PASSWORD= 
```

Run the following script:

```bash
python script.py
```

## DVC Commands

1. Initialize DVC:

    ```bash
    dvc init
    ```

2. Run the pipeline:

    ```bash
    dvc repro
    ```

3. View the pipeline DAG:

    ```bash
    dvc dag
    ```

## About MLflow and DVC

### MLflow

- **Production Grade**: Track your experiments and models.
- **Logging & Tagging**: Easily log and tag models.

### DVC

- **Lightweight for POCs**: Ideal for lightweight experiment tracking.
- **Orchestration**: Build and manage pipelines easily.

---

## AWS CI/CD Deployment with GitHub Actions

### Step 1: Login to AWS Console

Create an IAM user for deployment with the following permissions:

- EC2 access: Virtual machines for deployment.
- ECR access: To store Docker images in AWS.

### Step 2: Deployment Description

1. Build Docker image of the source code.
2. Push the Docker image to ECR.
3. Launch an EC2 instance.
4. Pull the image from ECR on EC2.
5. Run the Docker image on EC2.

### Step 3: AWS Policies

Add the following policies to the IAM user:

1. `AmazonEC2ContainerRegistryFullAccess`
2. `AmazonEC2FullAccess`

### Step 4: Create an ECR Repository

Save the repository URI. Example:

```
566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
```

### Step 5: Create an EC2 Instance

1. Launch an EC2 Ubuntu machine.
2. Install Docker on EC2:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### Step 6: Configure EC2 as a Self-Hosted GitHub Runner

1. Go to GitHub repository settings > Actions > Runners.
2. Create a new self-hosted runner for the EC2 instance.
3. Run the provided commands on your EC2 instance one by one.

### Step 7: Setup GitHub Secrets

In your GitHub repository, add the following secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION = us-east-1`
- `AWS_ECR_LOGIN_URI = 566373416292.dkr.ecr.us-east-1.amazonaws.com`
- `ECR_REPOSITORY_NAME = <your-repo-name>`

---

## Documentation

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow Tutorial](https://mlflow.org/docs/latest/tutorial.html)

---

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for more details.
