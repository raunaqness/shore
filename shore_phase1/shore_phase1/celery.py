import os
from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shore_phase1.settings")

app = Celery("shore_phase1")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()