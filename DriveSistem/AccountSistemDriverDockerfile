FROM python:3.12.8
WORKDIR /app


COPY . .

RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "driver_register.py"]
