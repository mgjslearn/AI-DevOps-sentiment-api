# AI DevOps Sentiment Analysis API

This project demonstrates a small-scale DevOps + AI workflow:
- A sentiment analysis model (positive/negative)
- FastAPI REST API
- Docker containerization
- CI/CD pipeline with GitHub Actions

## Run Locally

```bash
# Build Docker image
docker build -t ai-sentiment-api .

# Run container
docker run -p 8000:8000 ai-sentiment-api
