pip install django-celery
pip install redis
celery -A core worker -l INFO
pip install django-celery-results
celery -A core beat -l info

https://docs.celeryq.dev/en/main/index.html
https://docs.celeryq.dev/en/main/userguide/periodic-tasks.html

pip install django-celery-beat
celery -A core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler