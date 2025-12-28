FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install poetry && poetry install
CMD ["uvicorn", "src.analytics_engine.api.app:app", "--host", "0.0.0.0", "--port", "8080"]
