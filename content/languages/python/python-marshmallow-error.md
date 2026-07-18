---
title: "[Solution] Python Marshmallow Schema Error — How to Fix"
description: "Fix Python Marshmallow schema errors. Resolve field validation failures, serialization issues, and nested schema problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Marshmallow Schema Error

A `marshmallow.ValidationError` or `marshmallow.exceptions.ValidationError` occurs when data fails schema validation, fields are missing required values, or nested schemas receive incompatible data structures.

## Why It Happens

Marshmallow validates and serializes data using schema definitions. Errors arise when input data does not match the schema's field types, required fields are missing, custom validators reject values, or nested schemas encounter unexpected data shapes.

## Common Error Messages

- `ValidationError: {'name': ['Missing data for required field.']}`
- `ValidationError: {'age': ['Not a valid integer.']}`
- `ValidationError: {'email': ['Not a valid email address.']}`
- `ValidationError: {'address': ['Invalid value']}`

## How to Fix It

### Fix 1: Handle missing required fields

```python
from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    email = fields.Email(required=True)

# Wrong — missing fields cause validation error
# data = {"name": "Alice"}
# result = UserSchema().load(data)  # ValidationError

# Correct — provide all required fields or use defaults
class UserSchemaOptional(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=False, load_default=0)
    email = fields.Email(required=True)

schema = UserSchemaOptional()
try:
    result = schema.load({"name": "Alice", "email": "alice@example.com"})
    print(result)
except ValidationError as err:
    print(f"Errors: {err.messages}")
```

### Fix 2: Fix type conversion errors

```python
from marshmallow import Schema, fields, ValidationError

class EventSchema(Schema):
    name = fields.Str()
    count = fields.Int()
    active = fields.Bool()

# Wrong — string where int expected
# schema.load({"name": "test", "count": "abc"})

# Correct — validate and convert types explicitly
schema = EventSchema()

try:
    result = schema.load({
        "name": "test",
        "count": "42",  # marshmallow converts string to int
        "active": "true",  # marshmallow converts string to bool
    })
    print(result)
except ValidationError as err:
    print(f"Errors: {err.messages}")
    # {'count': ['Not a valid integer.']}

# Use strict type checking
class StrictEventSchema(Schema):
    name = fields.Str()
    count = fields.Int(strict=True)  # rejects "42" string
```

### Fix 3: Handle nested schemas correctly

```python
from marshmallow import Schema, fields, ValidationError

class AddressSchema(Schema):
    street = fields.Str(required=True)
    city = fields.Str(required=True)

class UserSchema(Schema):
    name = fields.Str(required=True)
    address = fields.Nested(AddressSchema, required=True)

# Wrong — nested data is flat
# schema.load({"name": "Alice", "address": "123 Main St"})

# Correct — provide nested structure
schema = UserSchema()

try:
    result = schema.load({
        "name": "Alice",
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
        },
    })
    print(result)
except ValidationError as err:
    print(f"Errors: {err.messages}")

# Allow None for optional nested
class UserOptionalSchema(Schema):
    name = fields.Str()
    address = fields.Nested(AddressSchema, allow_none=True, load_default=None)
```

### Fix 4: Custom validation with error messages

```python
from marshmallow import Schema, fields, validates, ValidationError

class RegistrationSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    age = fields.Int(required=True)

    @validates("username")
    def validate_username(self, value):
        if len(value) < 3:
            raise ValidationError("Username must be at least 3 characters.")

    @validates("age")
    def validate_age(self, value):
        if value < 18:
            raise ValidationError("Must be at least 18 years old.")

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters.")

schema = RegistrationSchema()

try:
    result = schema.load({
        "username": "ab",
        "password": "short",
        "age": 15,
    })
except ValidationError as err:
    print(err.messages)
    # {'username': ['Username must be at least 3 characters.'],
    #  'password': ['Password must be at least 8 characters.'],
    #  'age': ['Must be at least 18 years old.']}
```

## Common Scenarios

- **Missing required fields** — API requests omit fields marked as `required=True` in the schema.
- **Type mismatch in nested objects** — Flat strings sent where nested objects are expected.
- **Strict type mode rejects strings** — Using `strict=True` on Int fields rejects valid string representations like "42".

## Prevent It

- Always wrap `schema.load()` calls in try/except `ValidationError` blocks to handle validation failures gracefully.
- Use `load_default` and `dump_default` parameters to provide sensible defaults for optional fields.
- Test schemas with both valid and invalid data to catch validation issues early.

## Related Errors

- [ValidationError](/languages/python/validation-error/) — data validation failed
- [TypeError](/languages/python/typeerror/) — type mismatch during conversion
- [KeyError](/languages/python/keyerror/) — required field missing
