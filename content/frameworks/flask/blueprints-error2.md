---
title: "Blueprint conflict: endpoint already registered"
description: "Flask raises ValueError when two blueprints define the same endpoint name or URL rule"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["blueprint", "conflict", "endpoint", "route"]
weight: 5
---

This error occurs when two blueprints define a view function with the same name, or when URL rules conflict during registration. Flask requires unique endpoint names across the application.

## Common Causes

- Two blueprints have a function with the same name serving different routes
- Same route path registered by multiple blueprints
- Using `Blueprint.import_name` that causes module name collisions
- Copy-pasting blueprint code without renaming endpoints

## How to Fix

1. Use unique endpoint names with the `endpoint` parameter:

```python
api_v1 = Blueprint('api_v1', __name__)
api_v2 = Blueprint('api_v2', __name__)

@api_v1.route('/users')
def v1_users():
    return {"version": 1}

@api_v2.route('/users')
def v2_users():
    return {"version": 2}
```

2. Rename conflicting blueprints with different names:

```python
bp_users = Blueprint('users', __name__)
bp_admin_users = Blueprint('admin_users', __name__)
```

3. Check registered URL rules for conflicts:

```python
for rule in app.url_map.iter_rules():
    print(f"{rule.methods} {rule.rule} -> {rule.endpoint}")
```

4. Use `url_prefix` to isolate routes:

```python
app.register_blueprint(api_v1, url_prefix='/api/v1')
app.register_blueprint(api_v2, url_prefix='/api/v2')
```

## Examples

```python
bp1 = Blueprint('bp', __name__)
bp2 = Blueprint('bp', __name__)

@bp1.route('/home')
def home():
    return "v1"

@bp2.route('/home')
def home():
    return "v2"

app.register_blueprint(bp1)
app.register_blueprint(bp2)
# ValueError: The name 'home' is already registered
```

## Related Errors

- [Blueprint registration error]({{< relref "/frameworks/flask/blueprint-error" >}})
