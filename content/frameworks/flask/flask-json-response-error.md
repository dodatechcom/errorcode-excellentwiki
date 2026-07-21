---
title: "[Solution] Flask JSON Response Error"
description: "Fix Flask JSON response errors when jsonify fails to serialize data or returns incorrect format."
frameworks: ["flask"]
error-types: ["serialization-error"]
severities: ["error"]
---

JSON response errors occur when `jsonify` cannot serialize the data or when the response format does not match client expectations.

## Common Causes

- Data contains non-serializable objects (datetime, UUID)
- Nesting level too deep
- Circular references in data structure
- Response size too large
- Content-Type not set to application/json

## How to Fix

### Use Custom JSON Encoder

```python
import json
from datetime import datetime
from uuid import UUID
from flask import Flask, jsonify

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, UUID):
            return str(obj)
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
```

### Serialize Data Before Returning

```python
@app.route("/users")
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": u.id,
        "name": u.name,
        "created_at": u.created_at.isoformat(),
    } for u in users])
```

### Handle Large Responses

```python
from flask import Response
import json

@app.route("/large-data")
def large_data():
    data = generate_large_dataset()
    return Response(
        json.dumps(data),
        mimetype="application/json",
    )
```

## Examples

```python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Bug -- datetime not serializable
@app.route("/time")
def get_time():
    return jsonify({"time": datetime.now()})  # TypeError

# Fix -- convert to string
@app.route("/time-fixed")
def get_time_fixed():
    return jsonify({"time": datetime.now().isoformat()})
```
