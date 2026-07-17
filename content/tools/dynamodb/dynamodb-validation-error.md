---
title: "[Solution] DynamoDB ValidationException - Fix Invalid Request Parameters"
description: "Fix DynamoDB ValidationException by checking item size limits, validating attribute types against the table schema, fixing expression syntax, and using attribut"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB `ValidationException` occurs when a request contains invalid parameters. The error message describes the specific validation failure, such as incorrect attribute types, malformed expressions, or item size violations.

## What This Error Means

DynamoDB validates every request parameter before processing. The `ValidationException` is a client-side error (HTTP 400) indicating that the request does not conform to the DynamoDB API specification. Unlike throughput errors, this error cannot be resolved by retrying; the request itself must be fixed.

Common validation failures include incorrect key conditions, missing required attributes, invalid expression syntax, and attribute type mismatches.

## Why It Happens

- Item exceeds the 400KB size limit
- Required key attributes are missing from the request
- Expression attribute names or values do not match the expression
- Invalid comparison operator for the key type
- Using reserved words as attribute names without expression aliases
- Malformed filter or condition expressions
- Attribute type mismatch (e.g., providing a string for a number key)

## How to Fix It

### 1. Check Item Size

```python
import boto3
import json

def check_item_size(item):
    size = len(json.dumps(item, default=str).encode('utf-8'))
    if size > 400000:  # 400KB limit
        raise ValueError(f"Item size {size} bytes exceeds 400KB limit")
    return size
```

### 2. Use Expression Attribute Names for Reserved Words

```python
# Instead of referencing "status" directly (reserved word)
response = table.query(
    KeyConditionExpression=Key('id').eq('123'),
    FilterExpression='#s = :val',
    ExpressionAttributeNames={'#s': 'status'},
    ExpressionAttributeValues={':val': 'active'}
)
```

### 3. Fix Expression Syntax

```python
# Correct expression with proper attribute values
response = table.update_item(
    Key={'id': '123'},
    UpdateExpression='SET #a = :val1, #b = :val2',
    ExpressionAttributeNames={'#a': 'name', '#b': 'age'},
    ExpressionAttributeValues={':val1': 'Alice', ':val2': 30},
    ReturnValues='ALL_NEW'
)
```

### 4. Verify Key Conditions

```python
# GSI query must use the GSI key
response = table.query(
    IndexName='my-gsi',
    KeyConditionExpression=Key('gsi_key').eq('value')
)
```

### 5. Check Attribute Types

```python
# DynamoDB types must match the schema
# If the key is a Number, provide a number, not a string
response = table.put_item(
    Item={
        'id': 123,           # Number type
        'name': 'Alice',     # String type
        'active': True       # Boolean type
    }
)
```

### 6. Validate Before Sending

```python
from boto3.dynamodb.types import TypeSerializer

def validate_item(item):
    serializer = TypeSerializer()
    for key, value in item.items():
        try:
            serializer.serialize(value)
        except (TypeError, OverflowError) as e:
            raise ValueError(f"Invalid attribute {key}: {e}")
```

## Common Mistakes

- Forgetting to include `ExpressionAttributeValues` for every `:` placeholder in an expression
- Using `:` in `ExpressionAttributeValues` without matching it in the expression
- Mixing up `ExpressionAttributeNames` and `ExpressionAttributeValues`
- Not checking that the item size stays under 400KB after adding new attributes

## Related Pages

- [DynamoDB Item Not Found](/tools/dynamodb/dynamodb-item-not-found)
- [DynamoDB Size Limit](/tools/dynamodb/dynamodb-size-limit)
- [DynamoDB Type Error](/tools/dynamodb/dynamodb-type-error)
