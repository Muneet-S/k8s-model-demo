FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "model_server:app", "--host", "0.0.0.0", "--port", "5000"]
