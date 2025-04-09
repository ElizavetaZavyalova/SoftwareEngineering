FROM python:3.12.8
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","passenger_register.py"]