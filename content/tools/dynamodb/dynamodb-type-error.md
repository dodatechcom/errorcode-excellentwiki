---
title: "[Solution] DynamoDB TypeError - Fix Expression Attribute Values"
description: "Fix DynamoDB TypeError in expressions by ensuring correct DynamoDB-native attribute types, using proper TypeSerializer serialization, and avoiding empty string "
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB TypeError occurs when an expression attribute value has an incorrect or unsupported data type. The error message is `SerializationException: Start of structure or map found where not expected` or `One or more parameter values were invalid`.

## What This Error Means

DynamoDB requires specific data types for expression attribute values. Each value must be wrapped in a type descriptor (e.g., `{'S': 'value'}` for strings, `{'N': '123'}` for numbers). When a value is provided in the wrong format or an unsupported type is used, DynamoDB returns a `SerializationException` or `TypeError`.

This is distinct from `ValidationException` because it specifically relates to the serialization format of the attribute values, not the logical validity of the request.

## Why It Happens

- Passing a Python int where DynamoDB expects a string (or vice versa)
- Using `None` as an attribute value (not supported in DynamoDB)
- Providing a list where a map is expected
- Using nested expressions without proper type descriptors
- Mixing DynamoDB JSON and JavaScript Object Notation formats
- Forgetting to convert Python types to DynamoDB format in the SDK
- Passing empty strings (not supported for keys)

## How to Fix It

### 1. Use DynamoDB Type Objects

```python
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

serializer = TypeSerializer()

# Correct serialization
value = serializer.serialize('hello')  # {'S': 'hello'}
value = serializer.serialize(123)       # {'N': '123'}
value = serializer.serialize(True)      # {'BOOL': True}
```

### 2. Use the Table Resource Instead of Client

```python
# Table resource handles type conversion automatically
table = dynamodb.Table('my-table')
table.put_item(Item={
    'id': '123',          # String
    'count': 42,           # Number
    'active': True,        # Boolean
    'tags': ['a', 'b'],    # List
})

# Client requires manual type descriptors
client = boto3.client('dynamodb')
client.put_item(
    TableName='my-table',
    Item={
        'id': {'S': '123'},
        'count': {'N': '42'},
        'active': {'BOOL': True},
        'tags': {'L': [{'S': 'a'}, {'S': 'b'}]}
    }
)
```

### 3. Check for Empty Strings

```python
# DynamoDB does not allow empty strings in keys
# Use a placeholder or null instead
item = {
    'id': '123',
    'description': ''  # This is OK for non-key attributes
}

# For keys, use a sentinel value
item = {
    'id': '123',
    'sk': 'NONE'  # Instead of empty string
}
```

### 4. Validate Types Before Sending

```python
def validate_dynamodb_item(item):
    for key, value in item.items():
        if value is None:
            raise TypeError(f"Attribute '{key}' cannot be None")
        if isinstance(value, str) and len(value) == 0:
            if key in ('id', 'sk'):  # If it's a key
                raise TypeError(f"Key attribute '{key}' cannot be empty string")
```

### 5. Use the Correct Format for Expression Values

```python
# Correct: ExpressionAttributeValues must use type descriptors
response = table.query(
    KeyConditionExpression='pk = :pk',
    ExpressionAttributeValues={':pk': '123'}  # SDK converts this automatically
)

# Manual format (if using the client directly)
response = client.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ExpressionAttributeValues={':pk': {'S': '123'}}
)
```

## Common Mistakes

- Using the low-level client without wrapping values in type descriptors
- Passing `None` or `null` as an attribute value (use `{'NULL': True}` instead)
- Not converting Decimal to int/float before sending to DynamoDB
- Using Python boolean `True` in expression values when using the raw client

## Related Pages

- [DynamoDB ValidationException](/tools/dynamodb/dynamodb-validation-error)
- [DynamoDB Size Limit](/tools/dynamodb/dynamodb-size-limit)
- [DynamoDB Item Not Found](/tools/dynamodb/dynamodb-item-not-found)
