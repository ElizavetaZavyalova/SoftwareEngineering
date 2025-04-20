FROM python:3.12.8
WORKDIR /app

COPY libs/ ./libs/

COPY connect_trip/ ./connect_trip
COPY connect_trips.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","connect_trips.py"]