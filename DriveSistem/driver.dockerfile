FROM python:3.12.8
WORKDIR /app

ADD libs/ ./libs/

ADD driver/ ./driver
ADD driver_register.py .

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["python", "driver_register.py"]
