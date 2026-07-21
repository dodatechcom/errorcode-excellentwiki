---
title: "[Solution] Flask App Factory Error"
description: "Fix Flask app factory errors when application factory pattern fails to create or configure the app."
frameworks: ["flask"]
error-types": ["configuration-error"]
severities: ["error"]
---

The Flask application factory pattern fails when extensions, blueprints, or configuration are not properly initialized during app creation.

## Common Causes

- Extensions initialized before the app is created
- Blueprints registered multiple times during testing
- Configuration not applied before extension initialization
- Circular imports between application modules
- Missing `create_app` function or wrong return type

## How to Fix

### Implement Proper App Factory

```python
from flask import Flask

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from .main import main_bp
    app.register_blueprint(main_bp)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
```

### Use Proper Configuration

```python
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///app.db")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

config = {
    "development": Config,
    "testing": TestingConfig,
}
```

## Examples

```python
from flask import Flask

# Bug -- extensions initialized outside factory
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)  # Too late -- db already created
    return app

# Fix -- initialize inside factory
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)  # Correct -- initialize with app
    return app
```
