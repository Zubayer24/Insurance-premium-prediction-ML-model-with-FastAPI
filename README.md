# 🏥 Insurance Premium Category Predictor

A production-ready Machine Learning API that predicts insurance premium categories based on user demographics and lifestyle factors. Built with **FastAPI**, containerized with **Docker**, and deployed on **AWS**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [ML Model](#ml-model)
- [API Reference](#api-reference)
- [Running Locally](#running-locally)
- [Docker Deployment](#docker-deployment)
- [AWS Deployment](#aws-deployment)
- [Frontend](#frontend)
- [Live Demo](#live-demo)

---

## Overview

This project trains a classification model on insurance data and exposes it as a REST API. Given a user's BMI, age group, lifestyle risk, city tier, income, and occupation, the API returns a predicted insurance premium category along with confidence scores and class probabilities.

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | scikit-learn 1.5.2 |
| API Framework | FastAPI + Uvicorn |
| Data Processing | Pandas |
| Schema Validation | Pydantic |
| Frontend | Streamlit |
| Containerization | Docker |
| Cloud Deployment | AWS EC2 |
| Language | Python 3.11 |

---

## Project Structure

```
├── app.py                  # FastAPI application & route definitions
├── predict.py              # Model loading & prediction logic
├── frontend.py             # Streamlit UI (connects to deployed API)
├── Insurance_ml_model.ipynb # Model training & EDA notebook
├── insurance.csv           # Training dataset
├── model.pkl               # Serialized trained model
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build instructions
├── schema/
│   ├── user_input.py       # Pydantic input schema
│   └── predicted_response.py # Pydantic response schema
└── config/                 # Configuration files
```

---

## ML Model

The model is trained in `Insurance_ml_model.ipynb` on `insurance.csv`. It is a scikit-learn classifier (serialized as `model.pkl`) that predicts which insurance premium tier a person falls into.

**Input Features:**

| Feature | Type | Description |
|---|---|---|
| `bmi` | float | Body Mass Index |
| `age_group` | string | Categorized age bracket |
| `lifestyle_risk` | string | Risk level based on habits |
| `city_tier` | int | City classification (Tier 1/2/3) |
| `income_lpa` | float | Annual income in Lakhs Per Annum |
| `occupation` | string | One of: `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job` |

**Output:** Predicted premium category + confidence score + per-class probabilities.

---

## API Reference

### `GET /`
Health welcome message.

**Response:**
```json
{
  "message": "Welcome to the Insurance Premium Category Predictor API!"
}
```

---

### `GET /health`
Check API and model status.

**Response:**
```json
{
  "status": "API is healthy and running!",
  "model_version": "1.0.0",
  "Model_loaded": true
}
```

---

### `POST /predict`
Predict the insurance premium category.

**Request Body:**
```json
{
  "bmi": 24.5,
  "age_group": "adult",
  "lifestyle_risk": "low",
  "city_tier": 1,
  "income_lpa": 10.0,
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": {
    "predicted_category": "Silver",
    "confidence": 0.8721,
    "class_probabilities": {
      "Bronze": 0.0512,
      "Silver": 0.8721,
      "Gold": 0.0767
    }
  }
}
```

---

## Running Locally

### Prerequisites
- Python 3.11+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Zubayer24/Insurance-premium-prediction-ML-model-with-FastAPI.git
cd Insurance-premium-prediction-ML-model-with-FastAPI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the API server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Visit `http://localhost:8000/docs` for the interactive Swagger UI.

---

## Docker Deployment

### Build the Image

```bash
docker build -t insurance-premium-api .
```

### Run the Container

```bash
docker run -d -p 8000:8000 --name insurance-api insurance-premium-api
```

The API will be available at `http://localhost:8000`.

### Dockerfile Summary

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## AWS Deployment

The backend is deployed on an **AWS EC2** instance running Docker.

**Steps used to deploy:**

```bash
# On EC2 instance (Amazon Linux / Ubuntu)

# 1. Install Docker
sudo apt update && sudo apt install docker.io -y
sudo systemctl start docker

# 2. Clone the repo
git clone https://github.com/Zubayer24/Insurance-premium-prediction-ML-model-with-FastAPI.git
cd Insurance-premium-prediction-ML-model-with-FastAPI

# 3. Build and run the container
sudo docker build -t insurance-premium-api .
sudo docker run -d -p 8000:8000 insurance-premium-api
```

> **Note:** Make sure port `8000` is open in your EC2 Security Group inbound rules.

**Live API Base URL:** `http://184.72.90.42:8000`

---

## Frontend

The Streamlit frontend (`frontend.py`) connects to the deployed AWS API.

### Run the Frontend Locally

```bash
pip install streamlit requests
streamlit run frontend.py
```

**Features:**
- Input fields for age, weight, height, income, smoker status, city, and occupation
- Displays predicted premium category, confidence score, and full class probability breakdown
- Connects directly to the live AWS-hosted FastAPI backend

---

## Live Demo

| Service | URL |
|---|---|
| FastAPI Backend (AWS) | `http://184.72.90.42:8000` |
| Swagger Docs | `http://184.72.90.42:8000/docs` |
| Health Check | `http://184.72.90.42:8000/health` |

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

> Built by [Zubayer24](https://github.com/Zubayer24)
