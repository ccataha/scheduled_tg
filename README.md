# Telegram Bot with Task Scheduler

This project is a simple Telegram bot that sends scheduled messages to a specified chat.

## Features

- Sends scheduled messages at specified times.
- Supports loading configuration from an external YAML file.

## Requirements

- Python 3.9+
- Docker (optional)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/koidula/scheduled_tg_bot.git
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. or if you are using Docker:
    ```
    docker build -t telegram_bot .
    ```

## Configuration

1. Create a config.yml file in the root directory of the project.
2. Add your Telegram bot token, chat ID, and the scheduled message. Example:

    ```yaml
    TOKEN: "your_bot_token_here"
    CHAT_ID: "your_chat_id_here"
    SCHEDULED_MESSAGE: "Your scheduled message here"
    ```

## Usage
### Via Python
Run:
```bash
python telegram_bot.py
```
### Via Docker
If you've already built the Docker image, run the container:
```bash
docker run telegram_bot
```
Now your bot will send scheduled messages at specified times to the specified chat.
