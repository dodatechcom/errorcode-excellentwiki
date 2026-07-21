---
title: "[Solution] Flask Before First Request Error"
description: "Fix Flask before first request errors when initialization code fails or is not properly configured."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Flask `before_first_request` errors occur when initialization code raises exceptions or depends on resources not yet available.

## Common Causes

- Database connection not available during first request
- External service not running when initialization code executes
- Missing environment variables needed for initialization
- Initialization code depends on request context
- Multiple `before_first_request` functions conflict

## How to Fix

### Use Proper Initialization

```python
from flask import Flask

app = Flask(__name__)

@app.before_first_request
def initialize():
    app.logger.info("Initializing application...")
    # Initialize database connections, caches, etc.
```

### Use App Context for Initialization

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    with app.app_context():
        db.create_all()
        # Initialize extensions

    return app
```

### Handle Initialization Errors

```python
@app.before_first_request
def safe_initialize():
    try:
        initialize_database()
        app.logger.info("Database initialized")
    except Exception as e:
        app.logger.error(f"Initialization failed: {e}")
        # Graceful degradation
```

## Examples

```python
from flask import Flask

app = Flask(__name__)

# Bug -- accessing request in before_first_request
@app.before_first_request
def broken_init():
    print(request.method)  # No request context

# Fix -- don't access request here
@app.before_first_request
def working_init():
    app.logger.info("App initialized")
```
