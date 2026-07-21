---
title: "[Solution] Flask Request Validation Error"
description: "Fix Flask request validation errors when incoming data does not match expected schemas."
frameworks: ["flask"]
error-types: ["validation-error"]
severities: ["error"]
---

Request validation errors occur when incoming data does not match the expected format, type, or required fields.

## Common Causes

- Missing required fields in request body
- Wrong data types (string where int expected)
- Invalid email, URL, or UUID format
- Request body exceeds size limit
- Content-Type header does not match body format

## How to Fix

### Validate Request Data

```python
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    age = fields.Int(validate=validate.Range(min=0, max=150))

@app.route("/users", methods=["POST"])
def create_user():
    schema = UserSchema()
    errors = schema.validate(request.get_json())
    if errors:
        return jsonify({"errors": errors}), 400
    data = schema.load(request.get_json())
    # Create user
    return jsonify(data), 201
```

### Use Decorators for Validation

```python
from functools import wraps

def validate_json(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "Content-Type must be JSON"}), 415
        return f(*args, **kwargs)
    return decorated

@app.route("/data", methods=["POST"])
@validate_json
def process_data():
    data = request.get_json()
    return jsonify({"received": data})
```

## Examples

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Bug -- no validation
@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data)  # Accepts any data

# Fix -- validate input
@app.route("/user-fixed", methods=["POST"])
def create_user_fixed():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400
    return jsonify(data), 201
```
