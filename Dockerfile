FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "/app/entrypoint.py" ]
