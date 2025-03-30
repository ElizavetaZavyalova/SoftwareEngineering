FROM python:3.12.8
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","connect_trips.py"]