FROM python:3.11-slim

# Устанавливаем system зависимости
RUN apt-get update && apt-get install -y \
    wget gnupg curl unzip fonts-liberation libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2 \
    libpangocairo-1.0-0 libgtk-3-0 libxshmfence1 libxss1 libxtst6 libxext6 libxfixes3 \
    && rm -rf /var/lib/apt/lists/*

# Установка Playwright и его браузеров
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps

# Копируем весь проект
COPY . /app
WORKDIR /app

# Старт
CMD ["python", "main.py"]