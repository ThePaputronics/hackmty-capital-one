FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY apps/generator/pyproject.toml .
RUN pip install --no-cache-dir .

COPY apps/generator/src ./src

ENV PYTHONPATH=/app/src
ENV PORT=8001
ENV API_URL=http://api:8000
ENV SIM_SPEED=6.0
ENV AUTO_START=false

EXPOSE 8001

CMD ["python", "-m", "generator.server", "--host", "0.0.0.0", "--port", "8001", "--api-url", "http://api:8000"]
