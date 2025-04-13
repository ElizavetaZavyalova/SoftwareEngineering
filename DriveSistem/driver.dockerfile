FROM python:3.12.8
WORKDIR /app

ADD libs/entity/driver/ ./libs/entity/driver
ADD libs/entity/account.py ./libs/entity
ADD libs/entity/user.py ./libs/entity
ADD libs/tocken_generator/ ./libs/tocken_generator
ADD libs/account_sistem/ ./libs/account_sistem

ADD driver/ ./driver
ADD driver_register.py .

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["python", "driver_register.py"]
