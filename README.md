# Flask CI/CD Pipeline — Azure DevOps + Azure App Service

A production-style CI/CD pipeline deploying a Python Flask app to Azure App Service using Azure DevOps.

## Pipeline Overview

```
Push to main
    │
    ▼
[Stage 1: Build & Test]
    ├── Install Python 3.11
    ├── pip install dependencies
    ├── Run pytest (4 tests)
    └── Publish test results
    │
    ▼ (only if tests pass)
[Stage 2: Deploy]
    ├── Zip application
    └── Deploy to Azure App Service (Free F1)
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | App status and author info |
| `GET /health` | Health check with timestamp |
| `GET /info` | App version and pipeline info |

## Local Setup

```bash
# Clone and install
pip install -r requirements.txt

# Run locally
python app.py

# Run tests
pytest test_app.py -v
```

## Tech Stack

- **App:** Python 3.11, Flask 3.0, Gunicorn
- **CI/CD:** Azure DevOps Pipelines (multi-stage)
- **Hosting:** Azure App Service (Linux, Free F1)
- **Tests:** pytest with JUnit XML reporting
