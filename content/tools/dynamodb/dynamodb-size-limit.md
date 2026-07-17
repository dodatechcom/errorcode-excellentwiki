---
title: "[Solution] DynamoDB Item Size Limit Exceeded - Fix 400KB Limit"
description: "Fix DynamoDB 400KB item size limit exceeded by compressing attribute values, storing large payloads in S3 with references, and splitting oversized items into ch"
tools: ["dynamodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A DynamoDB item size limit exceeded error occurs when a single item exceeds the maximum allowed size of 400KB. The error message is `Item size has exceeded the maximum allowed size` with HTTP status code 400.

## What This Error Means

DynamoDB enforces a hard limit of 400KB per item, including all attribute names and values. This limit applies to every item in a table or index, and indexes consume additional storage for the indexed attributes. The error is a `ValidationException` and cannot be resolved by retrying.

The 400KB limit applies to the item as stored, not the data you think you are writing. Binary data, Unicode characters, and nested documents all count toward this limit.

## Why It Happens

- Storing large text fields (e.g., HTML content, JSON blobs) as a single attribute
- Embedding related data as nested documents instead of using separate items
- Accumulating too many list or map attributes in a single item
- Binary data (images, files) stored directly in DynamoDB
- JSON payload from an API response stored without truncation
- Logging data or audit trails stored as item attributes growing over time

## How to Fix It

### 1. Check Item Size Before Writing

```python
import json

def estimate_item_size(item):
    serialized = json.dumps(item, default=str)
    size_bytes = len(serialized.encode('utf-8'))
    return size_bytes

item = {'id': '123', 'data': large_payload}
size = estimate_item_size(item)
if size > 400000:
    raise ValueError(f"Item is {size} bytes, exceeds 400KB limit")
```

### 2. Store Large Data in S3, Reference from DynamoDB

```python
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

# Store large file in S3
s3.upload_file('large-file.pdf', 'my-bucket', 'files/123.pdf')

# Store reference in DynamoDB
table.put_item(
    Item={
        'id': '123',
        'file_url': 's3://my-bucket/files/123.pdf',
        'file_size': 1048576,
        'metadata': {'name': 'large-file.pdf'}
    }
)
```

### 3. Split Large Items Across Multiple Items

```python
# Instead of one 500KB item, split into chunks
def split_item(item_id, data, chunk_size=350000):
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    for i, chunk in enumerate(chunks):
        table.put_item(
            Item={
                'id': f"{item_id}#{i}",
                'chunk_index': i,
                'total_chunks': len(chunks),
                'data': chunk
            }
        )
```

### 4. Use DynamoDB Streams + Lambda for Large Data

```python
# Store summary in DynamoDB, archive full data elsewhere
def handle_large_event(event):
    table.put_item(
        Item={
            'id': event['id'],
            'summary': event['summary'][:500],  # Truncate
            'full_event_s3_key': f"events/{event['id']}.json"
        }
    )
    s3.put_object(Bucket='events', Key=f"events/{event['id']}.json", Body=json.dumps(event))
```

### 5. Compress Attribute Values

```python
import gzip
import base64

def compress_attribute(data):
    compressed = gzip.compress(data.encode('utf-8'))
    return base64.b64encode(compressed).decode('ascii')
```

## Common Mistakes

- Assuming the 400KB limit applies only to the primary key (it applies to the entire item)
- Not accounting for attribute name lengths in the size calculation
- Storing binary data directly in DynamoDB instead of using S3
- Forgetting that LSI and GSI items also count toward the 400KB limit individually

## Related Pages

- [DynamoDB ValidationException](/tools/dynamodb/dynamodb-validation-error)
- [DynamoDB Item Not Found](/tools/dynamodb/dynamodb-item-not-found)
- [DynamoDB Type Error](/tools/dynamodb/dynamodb-type-error)
