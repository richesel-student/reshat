#!/bin/bash

echo "Удаление образов"
docker system prune -a
# Загружаем сохранённые образы
echo "Загрузка образов..."

docker load -i postgres.tar

#docker load -i python3.tar
docker load -i python311.tar
echo "Все образы загружены!"

echo "Сборка проекта!"
docker-compose -f docker-compose.yml up --build



