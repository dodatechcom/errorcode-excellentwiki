---
title: "[Solution] Flask Exception Error"
description: "Fix Flask exception handling errors when unhandled exceptions cause 500 errors or debug information leaks."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Exception handling errors occur when Flask does not properly catch and handle exceptions, exposing sensitive information to users.

## Common Causes

- No custom error handlers registered
- Debug mode exposes stack traces to users
- Exception handlers do not return proper responses
- Database exceptions not caught
- External service failures not handled

## How to Fix

### Register Error Handlers

```python
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        "error": e.name,
        "description": e.description,
        "status_code": e.code,
    }), e.code

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Unhandled exception: {e}")
    return jsonify({"error": "Internal server error"}), 500
```

### Handle Database Exceptions

```python
from sqlalchemy.exc import SQLAlchemyError

@app.route("/users")
def get_users():
    try:
        users = User.query.all()
        return jsonify([u.to_dict() for u in users])
    except SQLAlchemyError as e:
        db.session.rollback()
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
```

## Examples

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Bug -- no error handler
@app.route("/risky")
def risky():
    raise ValueError("Something went wrong")  # 500 with stack trace

# Fix -- add error handler
@app.errorhandler(ValueError)
def handle_value_error(e):
    return jsonify({"error": str(e)}), 400

@app.route("/safe")
def safe():
    raise ValueError("Something went wrong")
```
