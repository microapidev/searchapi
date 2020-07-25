FROM python:3.8.1-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
ENV FLASK_ENV production