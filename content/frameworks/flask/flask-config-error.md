---
title: "ConfigurationError in Flask"
description: "Flask raises ConfigurationError when application configuration is invalid or missing required settings"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["configuration", "config", "settings", "environment", "flask"]
weight: 5
---

## What This Error Means

A ConfigurationError in Flask occurs when the application's configuration dictionary contains invalid values, is missing required settings, or when an extension receives misconfigured parameters. This can happen during app initialization or when extensions read configuration.

## Common Causes

- Missing required configuration keys (e.g., `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`)
- Invalid configuration values (wrong type or format)
- Environment variables not loaded properly
- Configuration file not found or incorrectly formatted
- Extension-specific configuration errors

## How to Fix

Set configuration values explicitly in your application factory:

```python
import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
```

Load configuration from a Python file:

```python
# config.py
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# __init__.py
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app
```

Use environment-specific configuration:

```python
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

Validate required keys on startup:

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    required_keys = ['SECRET_KEY', 'SQLALCHEMY_DATABASE_URI']
    for key in required_keys:
        if key not in app.config:
            raise ValueError(f"Missing required configuration: {key}")

    return app
```

## Examples

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = None  # Invalid value
```

```text
ValueError: A secret key is required to use CSRF.
```

## Related Errors

- [Import error]({{< relref "/frameworks/flask/import-error" >}})
- [Jinja2 template error]({{< relref "/frameworks/flask/jinja-error" >}})
