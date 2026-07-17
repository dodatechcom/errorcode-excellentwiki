---
title: "Blueprint registration error"
description: "Flask raises an error when a Blueprint is registered with an invalid name or URL prefix"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Flask fails to register a Blueprint because of invalid naming, missing `url_prefix`, or conflicts with existing route registrations.

## Common Causes

- Blueprint name conflicts with another registered blueprint
- URL prefix is missing or duplicates another blueprint's prefix
- Blueprint is registered before the Flask app is fully initialized
- Route names clash when multiple blueprints define the same endpoint name

## How to Fix

1. Give each blueprint a unique name:

```python
from flask import Blueprint

user_bp = Blueprint('users', __name__)
admin_bp = Blueprint('admin', __name__)
```

2. Specify unique URL prefixes:

```python
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(admin_bp, url_prefix='/admin')
```

3. Use the `name` parameter to avoid module conflicts:

```python
app.register_blueprint(user_bp, name='user_module')
```

4. Prevent endpoint name collisions with the `name` parameter:

```python
from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/status')
def status():
    return {"status": "ok"}
```

## Examples

```python
app = Flask(__name__)

bp1 = Blueprint('api', __name__)
bp2 = Blueprint('api', __name__)  # same name

app.register_blueprint(bp1, url_prefix='/api/v1')
app.register_blueprint(bp2, url_prefix='/api/v1')
# ValueError: The name 'api' is already registered
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
