---
title: "ImportError in Flask Application"
description: "Flask raises ImportError when a required module or extension cannot be found or loaded"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An ImportError in Flask occurs when the application cannot find or load a required Python module. This commonly happens when Flask extensions are not installed, or when circular imports exist between application modules.

## Common Causes

- Flask extension not installed (`pip install` missing)
- Circular imports between application modules
- Typo in module or function name
- Virtual environment not activated
- Incorrect import path for application factory

## How to Fix

Ensure all dependencies are installed:

```bash
pip install flask flask-sqlalchemy flask-migrate flask-login
```

Avoid circular imports by restructuring your application factory:

```python
# Correct: extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

# Correct: __init__.py
from flask import Flask
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    login_manager.init_app(app)
    return app
```

Use lazy imports for modules that may cause circular dependencies:

```python
# Correct: lazy import inside function
def create_blueprint():
    from .models import User
    bp = Blueprint('main', __name__)

    @bp.route('/')
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)
    return bp
```

Verify your virtual environment is active:

```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## Examples

```python
from flask_sqlalchemy import SQLAlchemy  # ImportError if flask-sqlalchemy not installed
```

```text
ModuleNotFoundError: No module named 'flask_sqlalchemy'
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [SQLAlchemy error]({{< relref "/frameworks/flask/sqlalchemy-error" >}})
