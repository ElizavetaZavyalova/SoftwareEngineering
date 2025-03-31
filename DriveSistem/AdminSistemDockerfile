FROM python:3.12.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

COPY . .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для приложения
EXPOSE 8000

# Указываем команду для запуска приложения
CMD ["python", "admin.py"]