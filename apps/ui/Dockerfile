FROM python:3.11-slim

WORKDIR /app

COPY apps/ui/index.html .
COPY apps/ui/server.py .

ENV PORT=3000
EXPOSE 3000

CMD ["python", "server.py"]
