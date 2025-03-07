# Проект "Payment"

"Payment" — это веб-приложение, для оплаты товаров.

## Установка и запуск

1. **Клонирование репозитория**

   ```bash
   git clone git@github.com:richesel-student/reshat.git
   
   ```

2. **Создание и запуск контейнеров**

   Используйте `docker-compose` для сборки и запуска контейнеров:

   ```bash
   docker-compose up --build
   ```


3. **Создание суперпользователя**

   Для доступа к административной панели Django создайте суперпользователя:

   ```bash
    docker exec -it payment bash 
    ```
   затем
   ```bash
    python manage.py createsuperuser
   ```

4. **Доступ к приложению**

   После выполнения вышеуказанных шагов приложение будет доступно по адресам: http://0.0.0.0:8000/item/1/

   Административная панель Django доступна по адресу: `http://0.0.0.0:8000/admin/`


## Переменные окружения

Для настройки базы данных и других параметров используйте переменные окружения. Вы можете создать файл `.env` в корневой директории проекта и определить следующие переменные:

```env
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
STRIPE_PUBLIC_KEY=example
STRIPE_SECRET_KEY=example
```

Для получения дополнительной информации: @RinatDevlikamov

