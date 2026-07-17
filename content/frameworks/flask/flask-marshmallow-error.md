---
title: "Flask-Marshmallow Serialization Error"
description: "Flask-Marshmallow raises ValidationError or marshalling errors when serialization or deserialization fails"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-Marshmallow errors occur when serialization (object to JSON) or deserialization (JSON to object) fails due to schema mismatches, missing fields, or validation errors. These errors manifest as `ValidationError` or `MarshallingError` during schema operations.

## Common Causes

- Missing required fields during deserialization
- Field type mismatch (string provided for integer field)
- Schema does not match model structure
- Nested schema configuration errors
- Missing `load` or `dump` configuration

## How to Fix

Define schemas with proper validation:

```python
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
```

Handle serialization errors:

```python
from marshmallow import ValidationError

@app.route('/api/users', methods=['POST'])
def create_user():
    json_data = request.get_json()
    try:
        data = user_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201
```

Handle nested schemas:

```python
class PostSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Nested(UserSchema, only=('id', 'name'))
```

## Examples

```python
schema = UserSchema()
result = schema.load({'name': ''})  # Missing required email, empty name
```

```text
marshmallow.exceptions.ValidationError: {'email': ['Missing data for required field.'], 'name': ['Shorter than minimum length 1.']}
```

## Related Errors

- [RESTful API error]({{< relref "/frameworks/flask/flask-restful-error" >}})
- [Template error]({{< relref "/frameworks/flask/jinja-error" >}})
