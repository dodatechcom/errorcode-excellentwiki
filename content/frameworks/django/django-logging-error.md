---
title: "[Solution] Django Logging Configuration Error — How to Fix"
description: "Fix Django logging configuration errors. Resolve logging setup, handler errors, and log output issues."
frameworks: ["django"]
error-types: ["configuration-error"]
severities: ["warning"]
weight: 5
comments: true
---

A Django logging configuration error occurs when the logging system is misconfigured, causing log messages to be lost, duplicated, or causing the application to crash on the first log call. Python's logging module has strict configuration requirements.

## Why It Happens

Django uses Python's `logging` module with a dictionary-based configuration in `LOGGING`. Errors arise when handler names don't match logger references, when log file paths are not writable, when circular imports occur in formatters, or when the configuration uses invalid keys. The most common cause is typos in handler or logger names.

## Common Error Messages

```
ValueError: Unable to configure handler 'file': [Errno 13] Permission denied
```

```
KeyError: 'formatters'
```

```
logging.error: No handlers could be found for logger "myapp.views"
```

```
ValueError: Unable to configure handler 'console': 'StreamHandler' object has no attribute 'stream'
```

## How to Fix It

### 1. Set Up Complete Logging Configuration

Define all required sections in the `LOGGING` dictionary:

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
        },
        'myapp': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### 2. Ensure Log Directory Exists

Create the log directory before the application starts:

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    # ... (as above)
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'django.log',
        },
    },
}
```

### 3. Use Logging in Views and Models

Apply the logging configuration throughout the application:

```python
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug("Processing request: %s", request.path)

    try:
        result = some_operation()
        logger.info("Operation completed: %s", result)
    except ValueError as e:
        logger.error("Operation failed: %s", e, exc_info=True)
        return HttpResponseServerError("Internal error")
    except Exception as e:
        logger.critical("Unexpected error: %s", e, exc_info=True)
        raise

    return JsonResponse({'status': 'ok'})
```

### 4. Configure Logging per Environment

Use environment-specific logging settings:

```python
# settings/production.py
LOGGING['handlers']['file']['filename'] = '/var/log/django/production.log'
LOGGING['handlers']['file']['level'] = 'WARNING'
LOGGING['loggers']['django']['level'] = 'WARNING'

# settings/development.py
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['loggers']['myapp']['level'] = 'DEBUG'
```

## Common Scenarios

**Scenario 1: Logs appear in console but not in file.**
Check that the log file path is correct and writable, that the handler's `level` is not set higher than the logger's level, and that `disable_existing_loggers` is not set to `True` (which is the default).

**Scenario 2: Logging causes circular import errors.**
If a logging formatter or filter imports from a module that also uses logging, you can get circular imports. Keep logging configuration self-contained and avoid importing application code in the `LOGGING` dict.

**Scenario 3: All loggers output to the same file.**
When using Django's default logging, all logs go to the console. To route different apps to different files, configure separate handlers and assign them to specific loggers.

## Prevent It

1. **Start with Django's default logging and add handlers incrementally.** Begin with console logging and add file or remote handlers one at a time to isolate issues.

2. **Test logging configuration early.** Add a test that imports the logging config and verifies handlers can be instantiated.

3. **Use structured logging for production.** Consider using `python-json-logger` for machine-readable logs that integrate with monitoring tools.
