---
title: "[Solution] Flask Configuration Loading Error — How to Fix"
description: "Fix Flask configuration errors. Resolve config loading, environment variable, and settings issues in Flask."
frameworks: ["flask"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask configuration loading error occurs when the application fails to load settings from the expected source, when configuration keys are missing, or when the config object is improperly structured. Configuration is critical for Flask applications.

## Why It Happens

Flask loads configuration from multiple sources: `config.py`, environment variables, instance config, and command-line options. Errors occur when the config file doesn't exist, when environment variables override expected values, when config classes are missing required attributes, or when the config is loaded before the app is created.

## Common Error Messages

```
ModuleNotFoundError: No module named 'config'
```

```
AttributeError: 'Config' object has no attribute 'SECRET_KEY'
```

```
KeyError: 'DATABASE_URI'
```

```
FileNotFoundError: Instance config not found
```

## How to Fix It

### 1. Use a Configuration Class

Define configuration in a dedicated module:

```python
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
```

### 2. Load Configuration in the App Factory

```python
# app.py
from flask import Flask
from config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Override with instance config if it exists
    app.config.from_pyfile('instance/config.py', silent=True)

    # Override with environment variables
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', app.config['SECRET_KEY'])

    return app
```

### 3. Access Configuration Safely

Use defensive access patterns:

```python
from flask import current_app

def get_database_url():
    # Option 1: Direct access (raises KeyError if missing)
    return current_app.config['DATABASE_URL']

    # Option 2: With default value
    return current_app.config.get('DATABASE_URL', 'sqlite:///default.db')

    # Option 3: Validate on startup
    required = ['SECRET_KEY', 'DATABASE_URL']
    for key in required:
        if key not in current_app.config:
            raise RuntimeError(f"Missing required config: {key}")
```

### 4. Use Environment Variables for Secrets

Never commit secrets to version control:

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or raise ValueError("SECRET_KEY not set")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
```

## Common Scenarios

**Scenario 1: Configuration works in development but fails in production.**
Production environments typically don't have the `.env` file. Ensure all required environment variables are set in the deployment environment.

**Scenario 2: Secret key is visible in source code.** Never hardcode secrets in `config.py`. Always use environment variables and add `config.py` to `.gitignore` if it contains development secrets.

**Scenario 3: Config values are not available in blueprints.** Use `current_app.config` inside request context, or pass config values explicitly to blueprint extensions during registration.

## Prevent It

1. **Use `python-dotenv`** to manage environment variables in development. Create a `.env.example` file documenting required variables.

2. **Validate configuration on app startup** with a function that checks all required keys are present.

3. **Keep configuration classes simple** — avoid importing application code in config modules, as this creates circular dependencies.
