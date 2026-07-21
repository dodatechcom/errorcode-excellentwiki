---
title: "[Solution] Flask Config Loading Error"
description: "Fix Flask configuration loading errors when config files or environment variables fail to load."
frameworks: ["flask"]
error-types: ["configuration-error"]
severities: ["error"]
---

Configuration loading errors occur when Flask cannot load configuration from files, environment variables, or configuration objects.

## Common Causes

- Config file not found or wrong path
- Environment variable not set
- Config object missing required attributes
- Circular import in config module
- Config values have wrong types

## How to Fix

### Load Configuration Properly

```python
from flask import Flask
import os

app = Flask(__name__)

# From environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")
app.config["DATABASE_URL"] = os.environ.get("DATABASE_URL", "sqlite:///app.db")

# From Python file
app.config.from_pyfile("config.py")

# From object
app.config.from_object("config.Config")
```

### Use Config Classes

```python
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key")
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}

app = Flask(__name__)
app.config.from_object(config[os.environ.get("FLASK_ENV", "development")])
```

### Handle Missing Config

```python
from flask import Flask

app = Flask(__name__)

try:
    app.config.from_pyfile("config.py")
except FileNotFoundError:
    app.config.from_mapping({"SECRET_KEY": "fallback-key"})
```

## Examples

```python
import os
from flask import Flask

app = Flask(__name__)

# Bug -- environment variable not set
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]  # KeyError

# Fix -- use get with default
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")
```
