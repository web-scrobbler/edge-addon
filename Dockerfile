FROM python:3.15-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT [ "/app/entrypoint.py" ]
