import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shore_phase2.settings")

app = Celery("shore_phase2")
# app.config_from_object("django.conf:settings", namespace="CELERY2")
app.autodiscover_tasks()