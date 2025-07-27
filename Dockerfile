FROM python:3.11.0

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

CMD ["python", "app.py"]
