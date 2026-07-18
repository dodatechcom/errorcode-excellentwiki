---
title: "[Solution] Python attrs Class Error — How to Fix"
description: "Fix Python attrs class errors. Resolve attribute initialization failures, converter issues, and frozen class problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python attrs Class Error

An `attrs.exceptions.ValidationError` or `AttributeError` occurs when attrs classes fail to initialize due to missing required attributes, converter functions raising exceptions, or attempts to modify frozen instances.

## Why It Happens

attrs provides class creation with automatic `__init__`, `__repr__`, and comparison methods. Errors arise when required attributes are not provided, type converters fail, frozen (immutable) instances are modified, or validators reject values during initialization.

## Common Error Messages

- `TypeError: __init__() missing 1 required positional argument: 'name'`
- `attrs.exceptions.ValidationError: 'age' must be >= 0`
- `attrs.exceptions.FrozenInstanceError: can't set attribute`
- `TypeError: 'NoneType' object is not iterable`

## How to Fix It

### Fix 1: Provide required attributes

```python
import attrs

@attrs.define
class User:
    name: str
    age: int
    email: str

# Wrong — missing required arguments
# user = User(name="Alice")  # TypeError

# Correct — provide all required attributes
user = User(name="Alice", age=25, email="alice@example.com")
print(user)

# Use defaults for optional fields
@attrs.define
class UserWithDefaults:
    name: str
    age: int = 0
    active: bool = True

user = UserWithDefaults(name="Bob")
print(user)
```

### Fix 2: Fix converter errors

```python
import attrs

def validate_age(value):
    if value < 0:
        raise ValueError("Age cannot be negative")
    return value

def convert_to_string(value):
    if value is None:
        return ""
    return str(value)

@attrs.define
class User:
    name: str = attrs.field(converter=convert_to_string)
    age: int = attrs.field(validator=attrs.validators.ge(0))

# Wrong — converter receives None and fails silently
# user = User(name=None, age=25)

# Correct — handle None in converter
user = User(name=None, age=25)
print(user)  # User(name='', age=25)

# Use complex converter
def parse_email(value):
    if "@" not in value:
        raise ValueError(f"Invalid email: {value}")
    return value.lower()

@attrs.define
class Contact:
    email: str = attrs.field(converter=parse_email)

contact = Contact(email="Alice@Example.com")
print(contact.email)  # alice@example.com
```

### Fix 3: Handle frozen instances

```python
import attrs

@attrs.define(frozen=True)
class Config:
    host: str
    port: int

config = Config(host="localhost", port=8080)

# Wrong — frozen instance cannot be modified
# config.port = 9090  # FrozenInstanceError

# Correct — create new instance for changes
new_config = attrs.evolve(config, port=9090)
print(new_config)
print(config)  # original unchanged

# Or use mutable class
@attrs.define
class MutableConfig:
    host: str
    port: int

m_config = MutableConfig(host="localhost", port=8080)
m_config.port = 9090  # works fine
print(m_config)
```

### Fix 4: Use slots and validators correctly

```python
import attrs

@attrs.define(slots=True)
class ValidatedUser:
    name: str = attrs.field()
    age: int = attrs.field()

    @name.validator
    def validate_name(self, attribute, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")

    @age.validator
    def validate_age(self, attribute, value):
        if not 0 <= value <= 150:
            raise ValueError(f"Age {value} is out of range")

# Wrong — empty name raises validation error
# user = ValidatedUser(name="", age=25)

# Correct — provide valid data
user = ValidatedUser(name="Alice", age=25)
print(user)

# slots=True prevents dynamic attributes
try:
    user.dynamic = "attribute"  # AttributeError
except AttributeError as e:
    print(f"Cannot set attribute: {e}")
```

## Common Scenarios

- **Missing required attrs** — Calling `__init__` without all required positional arguments causes TypeError.
- **Frozen modification** — Attempting to set an attribute on a frozen instance raises FrozenInstanceError.
- **Converter None handling** — Converters that do not handle None values fail when optional fields are omitted.

## Prevent It

- Always provide defaults for optional fields using `attrs.field(default=...)` to avoid missing argument errors.
- Use `attrs.evolve()` to create modified copies of frozen instances instead of direct assignment.
- Write validators that handle edge cases like empty strings and None values.

## Related Errors

- [TypeError](/languages/python/typeerror/) — missing required argument
- [ValueError](/languages/python/valueerror/) — invalid value for field
- [AttributeError](/languages/python/attributeerror/) — cannot set attribute on frozen instance
