#!/bin/bash
set -e

wait_for_it() {
  local host="$1"
  local port="$2"
  local retries=30

  echo "Waiting for $host:$port to be available..."

  for i in $(seq 1 $retries); do
    if nc -z "$host" "$port"; then
      echo "$host:$port is available!"
      return 0
    fi
    echo "Retrying in 2 seconds..."
    sleep 2
  done

  echo "Error: $host:$port is still not available after $retries attempts!"
  exit 1
}

wait_for_it db 5432

#wait_for_it postgres 5437
#sleep 100000

# Ожидаем запуска PostgreSQL
#echo "Waiting for PostgreSQL to start..."
#until nc -z -v -w30 postgres 5437; do
#  echo "Waiting for PostgreSQL connection..."
#  sleep 1
#done
#
#echo "PostgreSQL started, running migrations..."
python manage.py makemigrations
python manage.py migrate
#sleep 10000
exec uwsgi --ini /app/uwsgi.ini

