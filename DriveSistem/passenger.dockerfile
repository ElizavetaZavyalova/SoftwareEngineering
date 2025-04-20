FROM python:3.12.8
WORKDIR /app

COPY libs/ ./libs/
COPY passenger/ ./passenger
COPY passenger_register.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","passenger_register.py"]