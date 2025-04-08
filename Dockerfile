FROM python:3.10-slim-buster


RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV TRANSFORMERS_CACHE=/app/cache

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]