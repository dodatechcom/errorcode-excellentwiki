---
title: "[Solution] Python ImportError: No module named 'redbeat' — Fix"
description: "Fix Python ImportError: No module named 'redbeat'. Install celery-redbeat with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 311
---

# Python ImportError: No module named 'redbeat'

The `ModuleNotFoundError: No module named 'redbeat'` error occurs when Python cannot locate the celery-redbeat package, which provides a Celery beat scheduler backed by Redis.

## Common Causes

```python
# Cause 1: celery-redbeat not installed
from redbeat import RedBeatSchedulerEntry  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version or virtual environment
import redbeat  # ModuleNotFoundError

# Cause 3: Package name vs import name mismatch
# pip install celery-redbeat → import redbeat
```

```python
# Cause 4: Celery and Redis installed but redbeat missing
# pip install celery[redis] does not include celery-redbeat

# Cause 5: Redis connection not configured
# redbeat requires REDIS_URL or REDBEAT_REDIS_URL
```

## How to Fix

### Fix 1: Install celery-redbeat with pip

```bash
pip install celery-redbeat

# Verify installation
python -c "import redbeat; print('OK')"
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install celery-redbeat
python -c "from redbeat import RedBeatSchedulerEntry; print('OK')"
```

### Fix 3: Add to project requirements

```bash
# requirements.txt
celery
redis
celery-redbeat

# Install
pip install -r requirements.txt
```

## Examples

```python
# celery.py
from celery import Celery
from redbeat import RedBeatSchedulerEntry
from datetime import timedelta

app = Celery("myapp")
app.conf.redbeat_redis_url = "redis://localhost:6379/0"

# Create periodic task entry
entry = RedBeatSchedulerEntry(
    name="myapp.tasks.process_data",
    task="myapp.tasks.process_data",
    schedule=timedelta(hours=1),
    app=app,
)
entry.save()
```

```python
# settings.py — Celery beat configuration
CELERY_BEAT_SCHEDULER = "redbeat.RedBeatScheduler"
REDBEAT_REDIS_URL = "redis://localhost:6379/0"
```

## Related Errors

- {{< relref "importerror-celery" >}} — ImportError: celery
- {{< relref "importerror-redis-py" >}} — ImportError: redis
- {{< relref "importerror-celery2" >}} — ImportError: celery
