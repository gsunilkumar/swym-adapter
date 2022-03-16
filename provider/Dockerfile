FROM python:3.7-slim

WORKDIR /app

RUN pip install flask

RUN apt-get update && apt-get install -y curl

COPY . /app

EXPOSE 7001

CMD ["python", "main.py"]