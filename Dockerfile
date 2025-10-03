FROM python:3.12-slim

WORKDIR /app

COPY scalculator.py .
COPY test_scalculator.py .

CMD ["python", "scalculator.py"]