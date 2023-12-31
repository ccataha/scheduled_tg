FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir python-telegram-bot schedule PyYAML
EXPOSE 80
CMD ["python", "./Notifier-bot.py"]
