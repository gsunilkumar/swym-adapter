FROM python:3.7-slim

WORKDIR /app

RUN pip install flask

RUN apt-get update && apt-get install -y curl

COPY . /app

EXPOSE 7003

CMD ["python", "main.py"]