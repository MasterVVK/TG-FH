# Финансовый Помощник Бот

## Описание

Этот Telegram бот выступает в роли вашего финансового помощника. Он помогает вам следить за расходами, узнавать текущий курс валют и получать советы по экономии. Бот имеет несколько функциональных возможностей, включая регистрацию пользователей, отображение курса валют, предоставление советов по экономии и ведение учёта личных финансов.

## Функционал

- **Регистрация**: Регистрация пользователя в Telegram.
- **Курс валют**: Отображение курса валют с помощью API.
- **Советы по экономии**: Получение советов по экономии в виде текста.
- **Личные финансы**Конечно, вот пример README.md и полный проект для вашего финансового помощника:

### README.md

```markdown
# Финансовый Помощник Бот

## Описание

Этот Telegram бот выступает в роли вашего финансового помощника. Он помогает вам следить за расходами, узнавать текущий курс валют и получать советы по экономии. Бот имеет несколько функциональных возможностей, включая регистрацию пользователей, отображение курса валют, предоставление советов по экономии и ведение учёта личных финансов.

## Функционал

- **Регистрация**: Регистрация пользователя в Telegram.
- **Курс валют**: Отображение курса валют с помощью API.
- **Советы по экономии**: Получение советов по экономии в виде текста.
- **Личные финансы**: Ведение учёта личных финансов по категориям.

## Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/financial-helper-bot.git
    ```
2. Перейдите в директорию проекта:
    ```bash
    cd financial-helper-bot
    ```
3. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
5. Создайте файл `config.json` и добавьте ваши API ключи:
    ```json
    {
        "API_TOKEN": "your_telegram_bot_token",
        "EXCHANGE_API_KEY": "your_exchange_rate_api_key"
    }
    ```
6. Запустите бота:
    ```bash
    python bot.py
    ```

## Использование

- **/start**: Начать работу с ботом.
- **Регистрация в телеграм боте**: Зарегистрироваться в боте.
- **Курс валют**: Узнать текущий курс валют.
- **Советы по экономии**: Получить советы по экономии.
- **Личные финансы**: Ввести данные о своих расходах по категориям.

## Лицензия

Этот проект лицензирован под MIT License - подробности в файле LICENSE.
