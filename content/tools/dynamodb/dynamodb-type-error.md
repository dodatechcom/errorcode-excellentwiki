---
title: "[Solution] DynamoDB Type Mismatch in Attribute Value — How to Fix"
description: "Fix DynamoDB ValidationException for type mismatches by correcting attribute value types, matching schema expectations, and validating type conversions in application code."
tools: ["dynamodb"]
error-types: ["type-error"]
severities: ["error"]
weight: 5
comments: true
---

A `ValidationException` with a type mismatch error occurs when you provide an attribute value of the wrong DynamoDB type (String, Number, Binary, Boolean, Null, List, Map, or StringSet/NumberSet/BinarySet) for the operation being performed.

## What This Error Means

DynamoDB is a schema-on-read database, but it enforces strict type checking on attribute values. Each value must be wrapped in a type wrapper (e.g., `{'S': 'hello'}` for string, `{'N': '42'}` for number). If you provide a value in a different type than what the operation expects, or mix up the type wrappers, DynamoDB rejects the request.

Type errors can also occur in condition expressions, filter expressions, and update expressions where attribute types must be consistent.

## Why It Happens

- Passing a string value where a number is expected (or vice versa)
- Using the wrong type wrapper, e.g., `{'S': '123'}` instead of `{'N': '123'}` for arithmetic
- Comparing incompatible types in condition expressions
- Using `NULL` type where an actual value is required
- Mismatched set types (StringSet vs NumberSet)
- Providing a list where a map is expected in expression attribute values
- DynamoDB Streams records containing unexpected types from schema changes

## Common Error Messages

```
ValidationException: One or more parameter values were invalid: Type mismatch for number value
# or
Type mismatch for Index Key: AttributeValue has a type mismatch with the schema
# or
One or more parameter values were invalid: Type mismatch for attribute Status
# or
Expected: S, Received: N in ConditionExpression parameter
```

## How to Fix It

### 1. Use Correct Type Wrappers

```python
import boto3

client = boto3.client('dynamodb')

# Correct type wrappers
item_correct = {
    'pk': {'S': 'user#123'},        # String
    'age': {'N': '30'},             # Number (always as string!)
    'active': {'BOOL': True},       # Boolean
    'tags': {'SS': ['admin', 'user']},  # String Set
    'scores': {'NS': ['95', '87']},     # Number Set
    'address': {'M': {              # Map
        'city': {'S': 'NYC'},
        'zip': {'N': '10001'}
    }},
    'hobbies': {'L': [              # List
        {'S': 'reading'},
        {'S': 'coding'}
    ]}
}

client.put_item(TableName='my-table', Item=item_correct)
```

### 2. Validate Types Before Writing

```python
def validate_dynamodb_type(value):
    """Validate that the value uses correct DynamoDB type wrappers."""
    valid_types = {'S', 'N', 'B', 'BOOL', 'NULL', 'SS', 'NS', 'BS', 'L', 'M'}
    
    if not isinstance(value, dict) or len(value) != 1:
        return False
    
    key = next(iter(value))
    return key in valid_types

# Validate all attribute values
item = {
    'pk': {'S': 'user#123'},
    'count': 'wrong'  # Missing type wrapper
}

# This will fail - count should be {'N': '0'}
```

### 3. Convert Types Safely

```python
def safe_number(value):
    """Convert a number to DynamoDB number format."""
    try:
        return {'N': str(value)}
    except (TypeError, ValueError):
        return {'S': str(value)}

def safe_boolean(value):
    """Convert to DynamoDB boolean."""
    return {'BOOL': bool(value)}

# Use in item construction
item = {
    'pk': {'S': 'user#123'},
    'age': safe_number(30),
    'active': safe_boolean(True)
}
```

### 4. Fix Index Key Type Mismatches

```python
# If table has a Global Secondary Index (GSI) on 'status' with type String (S),
# you MUST use {'S': 'value'} for that attribute

# Correct for GSI key:
item = {
    'pk': {'S': 'user#123'},
    'status': {'S': 'active'}  # Must match GSI key type (S)
}

# Wrong - type mismatch:
item = {
    'pk': {'S': 'user#123'},
    'status': {'N': '1'}  # GSI expects String, not Number
}
```

### 5. Debug Type Mismatches in Expressions

```python
import boto3

client = boto3.client('dynamodb')

# Check expression attribute value types match the schema
# Example: UpdateExpression uses SET #age = :age
# :age must match the attribute's expected type

# Correct:
client.update_item(
    TableName='my-table',
    Key={'pk': {'S': 'user#123'}},
    UpdateExpression='SET #age = :age',
    ExpressionAttributeNames={'#age': 'age'},
    ExpressionAttributeValues={':age': {'N': '31'}}  # Number type
)

# Wrong - type mismatch:
client.update_item(
    TableName='my-table',
    Key={'pk': {'S': 'user#123'}},
    UpdateExpression='SET #age = :age',
    ExpressionAttributeNames={'#age': 'age'},
    ExpressionAttributeValues={':age': {'S': '31'}}  # Should be {'N': '31'}
)
```

## Common Scenarios

### Numeric IDs Stored as Strings

An application stores user IDs as numbers (`{'N': '12345'}`) in one table and as strings (`{'S': '12345'}`) in another. When performing cross-table lookups, the type mismatch causes errors. Standardize on a single type for IDs across all tables.

### Schema Migration Gone Wrong

During a schema migration, an attribute changes from Number to String. Existing code still writes Number values, causing errors. Implement a transition period where both types are accepted, or use a write-audit process to catch mismatches.

### Boolean vs String Confusion

A service that previously stored status as `{'S': 'true'}` is updated to use `{'BOOL': True}`. Downstream consumers that read the attribute fail to handle boolean values. Ensure all producers and consumers agree on the attribute type.

## Prevent It

- Define a schema validation layer that enforces attribute types before writing to DynamoDB
- Use DynamoDB typed value helpers to ensure consistent type wrappers
- Document the expected type for every attribute, especially index keys
- Run integration tests that verify type correctness for all write operations
- Use a DynamoDB mapper library that handles type serialization automatically
- Add pre-commit hooks that validate DynamoDB item structure
- Monitor for ValidationExceptions and alert when type mismatches increase

## Related Pages

- [DynamoDB Item Size Error](/tools/dynamodb/dynamodb-item-size-error)
- [DynamoDB Conditional Check Error](/tools/dynamodb/dynamodb-condcheck-error)
- [DynamoDB Filter Expression Error](/tools/dynamodb/dynamodb-filter-error)
