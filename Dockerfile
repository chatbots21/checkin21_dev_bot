FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [“python3”, “./polling_app.py”] 


