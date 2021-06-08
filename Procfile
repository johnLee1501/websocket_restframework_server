release: python manage.py migrate
web: daphne websocket_server.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=websocket_server.settings -v2