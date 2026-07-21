---
title: "[Solution] Flask Logging Config Error"
description: "Fix Flask logging configuration errors when log messages are missing, duplicated, or incorrectly formatted."
frameworks: ["flask"]
error-types: ["configuration-error"]
severities: ["error"]
---

Flask logging configuration errors occur when log handlers are not properly set up, causing missing or duplicate log messages.

## Common Causes

- Default Flask logger overwrites custom configuration
- Multiple handlers added without checking for duplicates
- Log level not set correctly for different environments
- Custom formatter not applied to Flask logger
- Logging configuration reset on app reload

## How to Fix

### Configure Logging Properly

```python
import logging
from flask import Flask

app = Flask(__name__)

# Set up logging
handler = logging.FileHandler("app.log")
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
))

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
```

### Use dictConfig for Complex Setup

```python
import logging
from logging.config import dictConfig

dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s %(levelname)s: %(message)s",
        },
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "default",
            "level": "INFO",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["file", "console"],
    },
})

app = Flask(__name__)
```

## Examples

```python
import logging
from flask import Flask

app = Flask(__name__)

# Bug -- no handler configured
# app.logger has no handlers -- messages go nowhere

# Fix -- add handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

@app.route("/test")
def test():
    app.logger.info("Test endpoint called")
    return "OK"
```
