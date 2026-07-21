---
title: "[Solution] Flask Celery Integration Error"
description: "Fix Flask Celery integration errors when background tasks fail to execute or results are lost."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Integrating Celery with Flask requires proper broker configuration and application context management. Misconfigurations cause tasks to silently fail.

## Common Causes

- Celery broker URL not configured or unreachable
- Flask application context not available inside Celery tasks
- Task serialization format (pickle vs JSON) mismatch
- Result backend not configured
- Flask extensions not initialized in Celery worker

## How to Fix

### Configure Celery with Flask

```python
from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/1"

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)
```

### Use Application Context in Tasks

```python
@celery.task
def process_order(order_id):
    with app.app_context():
        order = Order.query.get(order_id)
        # Process order
        db.session.commit()
```

### Configure Task Serialization

```python
celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    result_expires=3600,
)
```

## Examples

```python
from flask import Flask
from celery import Celery

app = Flask(__name__)

# Bug -- no application context
@celery.task
def broken_task(user_id):
    user = User.query.get(user_id)  # Fails -- no app context
    return user.name

# Fix -- use app context
@celery.task
def working_task(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        return user.name
```
