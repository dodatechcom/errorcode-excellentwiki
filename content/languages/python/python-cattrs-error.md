---
title: "Solved Python cattrs Error — How to Fix"
date: 2026-03-20T10:50:20+00:00
description: "Learn how to resolve Python cattrs structure and unstructure errors with custom converters."
categories: ["python"]
keywords: ["python cattrs", "cattrs error", "cattrs converter", "structure error", "attrs converter"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

cattrs errors occur when structuring or unstructuring attrs and dataclasses fails due to type mismatches, missing converters, or unsupported types. Custom converters often need explicit registration for complex nested types.

Common causes include:
- Missing converter registration for custom types
- Nested dataclass structures not automatically handled
- Union type resolution failing for ambiguous types
- Optional fields receiving incorrect None handling
- Frozen attrs classes causing assignment errors

## Common Error Messages

```python
import attrs
from cattrs import structure, unstructure

@attrs.define
class Config:
    name: str
    timeout: int

try:
    config = structure({"name": "test", "timeout": "not_int"}, Config)
except Exception as e:
    print(e)
# Cannot structure 'not_int' as int
```

```python
# KeyError for missing fields
@attrs.define
class Required:
    name: str
    value: int

structure({"name": "test"}, Required)
# KeyError: 'value'
```

## How to Fix It

### 1. Register Custom Converters

Create and register converters for custom types.

```python
import attrs
import datetime
from cattrs import Converter
from cattrs.gen import override

converter = Converter()

# Register datetime converter
def datetime_structure_hook(value, type_):
    if isinstance(value, str):
        return datetime.datetime.fromisoformat(value)
    return value

converter.register_structure_hook(datetime.datetime, datetime_structure_hook)

def datetime_unstructure_hook(value):
    return value.isoformat()

converter.register_unstructure_hook(datetime.datetime, datetime_unstructure_hook)

@attrs.define
class Event:
    name: str
    timestamp: datetime.datetime

# Now works
event = converter.structure({"name": "click", "timestamp": "2026-01-15T10:30:00"}, Event)
```

### 2. Handle Nested Structures

Configure structuring for deeply nested types.

```python
import attrs
from typing import Optional
from cattrs import Converter

@attrs.define
class Address:
    street: str
    city: str
    zip_code: str

@attrs.define
class User:
    name: str
    address: Optional[Address] = None

converter = Converter()

# Register nested hook
converter.register_structure_hook(
    Address,
    lambda d, _: Address(**d) if d else None
)

user = converter.structure(
    {"name": "John", "address": {"street": "123 Main", "city": "NYC", "zip_code": "10001"}},
    User
)

# With renames for API compatibility
converter.register_structure_hook(
    User,
    lambda d, _: User(
        name=d["name"],
        address=converter.structure(d.get("addr"), Address) if d.get("addr") else None
    )
)
```

### 3. Use Override for Field-Level Control

Custom per-field structuring behavior.

```python
import attrs
from cattrs import Converter
from cattrs.gen import override, make_dict_structure_fn, make_dict_unstructure_fn

@attrs.define
class ApiModel:
    user_name: str
    email_address: str
    is_active: bool = True

converter = Converter()

# Rename fields during conversion
structure_fn = make_dict_structure_fn(
    ApiModel,
    converter,
    renames={"user_name": "userName", "email_address": "emailAddress"}
)
converter.register_structure_hook(ApiModel, structure_fn)

unstructure_fn = make_dict_unstructure_fn(
    ApiModel,
    converter,
    renames={"user_name": "userName", "email_address": "emailAddress"}
)
converter.register_unstructure_hook(ApiModel, unstructure_fn)

# Now works with camelCase API
data = converter.structure({"userName": "john", "emailAddress": "j@x.com"}, ApiModel)
result = converter.unstructure(data)
# {"userName": "john", "emailAddress": "j@x.com", "isActive": True}
```

## Common Scenarios

### Scenario 1: API Response Parsing

Converting API responses to domain objects:

```python
import attrs
from cattrs import Converter

@attrs.define
class ApiResponse:
    status: int
    data: dict
    error: str | None = None

converter = Converter()

def api_structure(d, _):
    return ApiResponse(
        status=d["statusCode"],
        data=d.get("payload", {}),
        error=d.get("errorMessage")
    )

converter.register_structure_hook(ApiResponse, api_structure)

response = converter.structure({
    "statusCode": 200,
    "payload": {"users": []}
}, ApiResponse)
```

## Prevent It

- Use `make_dict_structure_fn` to auto-generate converters from attrs metadata
- Register converters for all custom types before structuring data
- Use `override` for field renaming when API fields differ from Python names
- Test converters with edge cases including None values and empty dicts
- Use `pipe` converters for validation alongside structuring