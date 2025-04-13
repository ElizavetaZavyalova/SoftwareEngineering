FROM python:3.12.8
WORKDIR /app

COPY libs/entity/passenger/ ./libs/entity/passenger
COPY libs/entity/trip/ ./libs/entity/trip
COPY libs/entity/account.py ./libs/entity
COPY libs/entity/user.py ./libs/entity
COPY libs/tocken_generator/ ./libs/tocken_generator

COPY connect_trip/ ./connect_trip
COPY connect_trips.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","connect_trips.py"]