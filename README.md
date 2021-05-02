# Install and Run
```
pip install -e .
celery -A pyramid_celery.celery_app worker --ini config.ini
```