web: gunicorn config.wsgi:application
worker: celery worker --app=cookie.taskapp --loglevel=info
