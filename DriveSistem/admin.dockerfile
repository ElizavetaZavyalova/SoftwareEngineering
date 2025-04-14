FROM python:3.12.8

WORKDIR /app


COPY libs/entity/ ./libs/entity
COPY libs/tocken_generator/ ./libs/tocken_generator

COPY admin_sistem/ ./admin_sistem
COPY admin.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# Указываем команду для запуска приложения
CMD ["python", "admin.py"]