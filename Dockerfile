FROM python:3.8.1-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
EXPOSE 9207
RUN chmod +x /app/deploy.sh
CMD ["/app/deploy.sh"]