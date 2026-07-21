---
title: "[Solution] Flask JSON Encoder Error"
description: "Fix Flask JSON encoder errors when serializing non-JSON-serializable objects in responses."
frameworks: ["flask"]
error-types: ["serialization-error"]
severities: ["error"]
---

Flask raises `TypeError` when trying to serialize objects that are not JSON-serializable, such as datetime, UUID, or custom model instances.

## Common Causes

- Returning `datetime` objects directly in JSON responses
- Custom model instances not converted to dictionaries
- UUID objects not converted to strings
- Decimal numbers not handled by default encoder
- Nested objects contain non-serializable types

## How to Fix

### Use Custom JSON Encoder

```python
import json
from datetime import datetime, date
from uuid import UUID
from flask import Flask

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, UUID):
            return str(obj)
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
```

### Convert Objects Before Returning

```python
@app.route("/user/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    return {
        "id": user.id,
        "name": user.name,
        "created_at": user.created_at.isoformat(),
    }
```

### Use Flask's Built-in JSON Serialization

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data")
def get_data():
    return jsonify({
        "date": "2024-01-15",
        "value": 42,
    })
```

## Examples

```python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Bug -- returning datetime directly
@app.route("/time")
def get_time():
    return jsonify({"time": datetime.now()})  # TypeError

# Fix -- convert to string
@app.route("/time-fixed")
def get_time_fixed():
    return jsonify({"time": datetime.now().isoformat()})
```
