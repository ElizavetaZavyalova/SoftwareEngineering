FROM python:3.12.8
WORKDIR /app

COPY libs/entity/passenger/ ./libs/entity/passenger
COPY libs/entity/account.py ./libs/entity
COPY libs/entity/user.py ./libs/entity
COPY libs/tocken_generator/ ./libs/tocken_generator
COPY libs/account_sistem/ ./libs/account_sistem
ADD libs/account_sistem/ ./libs/account_sistem

COPY passenger/ ./passenger
COPY passenger_register.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","passenger_register.py"]