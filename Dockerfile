FROM python:3.12-slim   

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && \ 
    python3 manage.py makemigrations && \
    python3 manage.py migrate 

EXPOSE 8000:8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
