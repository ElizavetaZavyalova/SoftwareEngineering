FROM python:3.12.8
WORKDIR /app

COPY libs/ ./libs/

COPY adding_trip/ ./adding_trip
COPY adding_trips.py .

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","adding_trips.py"]