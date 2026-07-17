---
title: "Flask-Swagger/OpenAPI Error"
description: "Flask-Swagger raises errors when OpenAPI/Swagger specification generation or validation fails"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-Swagger errors occur when the OpenAPI specification cannot be generated correctly, when API documentation validation fails, or when the Swagger UI encounters issues rendering the API spec. These errors typically appear during documentation generation or when the spec is invalid.

## Common Causes

- Missing endpoint documentation or decorators
- Invalid schema definitions
- Route parameters not declared in spec
- Response schemas inconsistent with actual responses
- Swagger UI version mismatch

## How to Fix

Configure Flask-Swagger UI:

```python
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "My API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
```

Generate the Swagger spec:

```python
@app.route('/api/swagger.json')
def swagger_spec():
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "My API",
            "version": "1.0.0"
        },
        "paths": {
            "/api/users": {
                "get": {
                    "summary": "Get all users",
                    "responses": {
                        "200": {
                            "description": "A list of users"
                        }
                    }
                }
            }
        }
    }
    return jsonify(spec)
```

Use flask-restx for automatic documentation:

```python
from flask_restx import Api, Resource, fields

api = Api(app, version='1.0', title='My API')

user_model = api.model('User', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True),
    'email': fields.String(required=True),
})

ns = api.namespace('users', description='User operations')

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        return User.query.all()
```

Validate spec before serving:

```python
import yaml

@app.route('/api/swagger.yaml')
def swagger_yaml():
    with open('swagger.yaml', 'r') as f:
        spec = yaml.safe_load(f)
    return jsonify(spec)
```

## Examples

```python
@app.route('/api/data')
def data():
    return jsonify({'value': 42})
# Missing: API documentation decorators
```

```text
ValueError: Path parameter 'user_id' not declared in path '/api/users/{user_id}'
```

## Related Errors

- [RESTful API error]({{< relref "/frameworks/flask/flask-restful-error" >}})
- [Template error]({{< relref "/frameworks/flask/jinja-error" >}})
