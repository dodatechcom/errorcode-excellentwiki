---
title: "[Solution] DynamoDB Item Size Exceeds 400KB Limit — How to Fix"
description: "Fix DynamoDB ValidationException when item size exceeds the 400KB limit by compressing attributes, splitting items, using S3 for large objects, or reducing attribute count."
tools: ["dynamodb"]
error-types: ["item-size-error"]
severities: ["error"]
weight: 5
comments: true
---

A `ValidationException` with the message "Item size has exceeded the maximum allowed size" occurs when you attempt to write an item larger than 400KB to a DynamoDB table. This is a hard limit that cannot be increased.

## What This Error Means

DynamoDB enforces a maximum item size of 400KB, including both the attribute names and values. The size is calculated as the sum of the lengths of all attribute names and their values in UTF-8 bytes. This limit applies to the base table and all Global Secondary Indexes. If any item exceeds 400KB, the write operation fails.

Unlike throttling errors, this is a validation error that occurs regardless of capacity. The item must be restructured to fit within the limit.

## Why It Happens

- Storing large blobs, images, or files directly in DynamoDB items
- Accumulating too many attributes on a single item over time
- Using long attribute names that inflate item size
- Storing large JSON documents as a single string attribute
- Including redundant or duplicate data across attributes
- Appending data to list or map attributes without size checks
- Exceeding the 400KB limit due to nested attribute structures

## Common Error Messages

```
ValidationException: Item size has exceeded the maximum allowed size of 400KB
# or
Item size has exceeded the maximum allowed size for this table
# or
One or more parameter values were invalid: Item size has exceeded the maximum allowed size
# or
The item size exceeds the 400KB limit for DynamoDB. Consider compressing or splitting the item.
```

## How to Fix It

### 1. Compress Large Attributes

```python
import boto3
import zlib
import json

def compress_and_store(client, table_name, key, large_data):
    compressed = zlib.compress(json.dumps(large_data).encode('utf-8'))
    item = {
        'pk': {'S': key},
        'data_compressed': {'B': compressed},
        'compressed_size': {'N': str(len(compressed))}
    }
    client.put_item(TableName=table_name, Item=item)
```

Compression can reduce attribute size by 5-10x for text data. Use binary (B) type for compressed blobs.

### 2. Store Large Objects in S3

```python
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

def store_large_item(table_name, pk, large_data, bucket):
    s3_key = f"dynamodb-large/{pk}/{hash(large_data)}"
    s3.put_object(Bucket=bucket, Key=s3_key, Body=large_data)
    
    dynamodb.put_item(TableName=table_name, Item={
        'pk': {'S': pk},
        's3_bucket': {'S': bucket},
        's3_key': {'S': s3_key},
        'metadata': {'S': 'item stored in S3'}
    })
```

Move large payloads to S3 and store the S3 reference in DynamoDB. Querying is fast and storage costs are lower.

### 3. Split the Item Across Multiple Rows

```python
import boto3

client = boto3.client('dynamodb')

def split_and_store(table_name, pk, data_chunks):
    for i, chunk in enumerate(data_chunks):
        client.put_item(TableName=table_name, Item={
            'pk': {'S': pk},
            'sk': {'S': f"chunk#{i:04d}"},
            'data': {'S': chunk}
        })
```

Use a composite sort key to store item fragments. Query with `pk` and `begins_with` on sort key to reassemble. Each fragment must stay under 400KB.

### 4. Shorten Attribute Names

```python
# Instead of this:
item = {
    'pk': {'S': key},
    'user_profile_picture_base64': {'S': long_string},
    'user_account_creation_timestamp': {'N': timestamp}
}

# Use shorter attribute names:
item = {
    'pk': {'S': key},
    'pic': {'S': long_string},  # Was: user_profile_picture_base64
    'cts': {'N': timestamp}     # Was: user_account_creation_timestamp
}
```

Attribute names count toward the 400KB limit. Shortening names from 30+ characters to 3-5 saves significant space, especially on items with many attributes.

### 5. Remove Redundant Attributes

```python
# Remove computed or redundant values that can be derived
# Instead of storing full_name, first_name, and last_name, store only first_name and last_name
```

Audit item attributes for derived or redundant data. Store only the minimal set of attributes needed for your access patterns.

## Common Scenarios

### Storing User-Uploaded Images in DynamoDB

A social media app stores profile pictures as Base64-encoded strings directly in DynamoDB items. The images are typically 200-500KB, causing items to exceed the limit. The solution is to store images in S3 and keep only the S3 key in DynamoDB.

### Accumulating Audit Logs as Item Attributes

A system appends audit log entries to a list attribute on each item. Over time, the audit trail grows beyond 400KB. The fix is to store audit logs in a separate table with one log entry per item, rather than appending to a single item.

### Large JSON Configuration Documents

A configuration service stores JSON config documents (300-700KB) as a single string attribute. These frequently exceed the limit. Compress the JSON before storage or split the configuration across multiple items keyed by category.

## Prevent It

- Set a maximum item size check in your application code before writing to DynamoDB
- Monitor item sizes using CloudWatch and log warnings for items exceeding 300KB
- Store blobs and files in S3 with DynamoDB metadata references
- Use short attribute names (3-5 characters) in your data model
- Compress large text attributes before storage
- Implement item size validation in write operations
- Regularly audit and purge unnecessary attributes
- Consider using a relational database like RDS for items that naturally exceed 400KB

## Related Pages

- [DynamoDB Provisioned Throughput Error](/tools/dynamodb/dynamodb-throughput-error)
- [DynamoDB Conditional Check Error](/tools/dynamodb/dynamodb-condcheck-error)
- [DynamoDB Type Mismatch Error](/tools/dynamodb/dynamodb-type-error)
