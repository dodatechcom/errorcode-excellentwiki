---
title: "[Solution] Flask-RESTful Resource Error"
description: "Fix Flask-RESTful resource errors when API resources fail to register or handle requests correctly."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Flask-RESTful resource errors occur when API resources are not properly registered, have conflicting routes, or incorrect method handlers.

## Common Causes

- Resource not registered with the API
- Duplicate route registrations for the same resource
- HTTP method handler not defined on the resource
- Request parser not configured correctly
- Response format does not match expected schema

## How to Fix

### Register Resources Correctly

```python
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {"id": user.id, "name": user.name}

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        user.name = request.json["name"]
        db.session.commit()
        return {"id": user.id, "name": user.name}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return "", 204

api.add_resource(UserResource, "/users/<int:user_id>")
```

### Use Proper Route Registration

```python
# Register resource with multiple routes
api.add_resource(UserResource, "/users", "/users/<int:user_id>")
```

### Handle Missing Resources

```python
from flask_restful import abort

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message=f"User {user_id} not found")
        return {"id": user.id, "name": user.name}
```

## Examples

```python
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class ItemResource(Resource):
    def get(self):
        return {"items": []}

# Bug -- duplicate route registration
api.add_resource(ItemResource, "/items")
api.add_resource(ItemResource, "/items")  # Conflicts

# Fix -- single registration
api.add_resource(ItemResource, "/items")
```
