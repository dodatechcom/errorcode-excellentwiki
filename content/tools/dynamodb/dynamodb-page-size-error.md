---
title: "[Solution] DynamoDB Page Size Limit Exceeded — How to Fix"
description: "Fix DynamoDB page size limit issues when query or scan results exceed 1MB by using pagination with LastEvaluatedKey, limiting result sets, or optimizing filter patterns."
tools: ["dynamodb"]
error-types: ["page-size-error"]
severities: ["error"]
weight: 5
comments: true
---

A page size issue in DynamoDB occurs when a single query or scan response exceeds 1MB. DynamoDB returns a paginated result set with a `LastEvaluatedKey` that must be used to fetch the next page. While not strictly an error, misinterpreting pagination leads to incomplete data or application bugs.

## What This Error Means

DynamoDB limits the amount of data returned in a single query or scan response to 1MB. When the result set exceeds this limit, DynamoDB returns a subset of the data along with a `LastEvaluatedKey` token. Your application must use this token to request the next page. Failure to paginate results in missing data.

This applies to both query and scan operations. The 1MB limit is calculated before any filter expression is applied, so a filter expression does not reduce the data read from the table.

## Why It Happens

- Query or scan returns more than 1MB of data in a single response
- Application does not implement pagination logic
- The `Limit` parameter is set higher than the effective page size
- Filter expression is used as a substitute for proper pagination
- The page size is exceeded due to large items (close to 400KB each)
- Inefficient scan operations on large tables without proper segmentation
- The application ignores the `LastEvaluatedKey` in the response

## Common Error Messages

```
The page size limit of 1MB was exceeded. Use LastEvaluatedKey to paginate.
# or
Scan operation results exceed the 1MB limit. Use pagination to retrieve all data.
# or
Query response is too large. Please paginate using the LastEvaluatedKey.
# or
Result set is truncated. LastEvaluatedKey is provided for pagination.
```

## How to Fix It

### 1. Implement Proper Pagination

```python
import boto3

client = boto3.client('dynamodb')

def query_all_pages(table_name, key_condition, expression_values):
    items = []
    last_evaluated_key = None
    
    while True:
        params = {
            'TableName': table_name,
            'KeyConditionExpression': key_condition,
            'ExpressionAttributeValues': expression_values
        }
        
        if last_evaluated_key:
            params['ExclusiveStartKey'] = last_evaluated_key
        
        response = client.query(**params)
        items.extend(response.get('Items', []))
        
        last_evaluated_key = response.get('LastEvaluatedKey')
        if not last_evaluated_key:
            break
    
    return items
```

### 2. Use Limit Parameter Effectively

```python
import boto3

client = boto3.client('dynamodb')

def query_with_limit(table_name, key_condition, expression_values, page_size=100):
    """Query with explicit page size."""
    items = []
    last_evaluated_key = None
    
    while True:
        params = {
            'TableName': table_name,
            'KeyConditionExpression': key_condition,
            'ExpressionAttributeValues': expression_values,
            'Limit': page_size
        }
        
        if last_evaluated_key:
            params['ExclusiveStartKey'] = last_evaluated_key
        
        response = client.query(**params)
        items.extend(response.get('Items', []))
        
        last_evaluated_key = response.get('LastEvaluatedKey')
        if not last_evaluated_key:
            break
    
    return items
```

### 3. Parallel Scan with Segment Support

```python
import boto3
from concurrent.futures import ThreadPoolExecutor

client = boto3.client('dynamodb')

def scan_segment(table_name, total_segments, segment, limit=1000):
    items = []
    last_evaluated_key = None
    
    while True:
        params = {
            'TableName': table_name,
            'TotalSegments': total_segments,
            'Segment': segment,
            'Limit': limit
        }
        
        if last_evaluated_key:
            params['ExclusiveStartKey'] = last_evaluated_key
        
        response = client.scan(**params)
        items.extend(response.get('Items', []))
        
        last_evaluated_key = response.get('LastEvaluatedKey')
        if not last_evaluated_key:
            break
    
    return items

def parallel_scan(table_name, total_segments=4):
    with ThreadPoolExecutor(max_workers=total_segments) as executor:
        futures = [
            executor.submit(scan_segment, table_name, total_segments, i)
            for i in range(total_segments)
        ]
        results = []
        for future in futures:
            results.extend(future.result())
    return results
```

### 4. Use Projection Expressions to Reduce Page Size

```python
import boto3

client = boto3.client('dynamodb')

# Reduce page size by returning only needed attributes
response = client.query(
    TableName='my-table',
    KeyConditionExpression='pk = :pk',
    ProjectionExpression='pk, sk, status, created_at',
    ExpressionAttributeValues={':pk': {'S': 'user#123'}}
)

# Fewer attributes per item means more items fit in each 1MB page
items = response.get('Items', [])
last_evaluated_key = response.get('LastEvaluatedKey')
```

### 5. Use Filter Expression After Pagination

```python
import boto3

client = boto3.client('dynamodb')

# Filter expression does NOT reduce page count - it filters after reading
# Always paginate even with filter expressions

def query_with_filter(table_name, key_condition, expression_values, filter_expr):
    items = []
    last_evaluated_key = None
    
    while True:
        params = {
            'TableName': table_name,
            'KeyConditionExpression': key_condition,
            'FilterExpression': filter_expr,
            'ExpressionAttributeValues': expression_values
        }
        
        if last_evaluated_key:
            params['ExclusiveStartKey'] = last_evaluated_key
        
        response = client.query(**params)
        items.extend(response.get('Items', []))
        
        last_evaluated_key = response.get('LastEvaluatedKey')
        if not last_evaluated_key:
            break
    
    return items
```

### 6. Handle Pagination in DynamoDB Streams

```python
import boto3

client = boto3.client('dynamodbstreams')

def process_stream_all_shards(stream_arn, iterator_type='TRIM_HORIZON'):
    response = client.describe_stream(StreamArn=stream_arn)
    shards = response['StreamDescription']['Shards']
    
    for shard in shards:
        shard_id = shard['ShardId']
        shard_iterator = client.get_shard_iterator(
            StreamArn=stream_arn,
            ShardId=shard_id,
            ShardIteratorType=iterator_type
        )['ShardIterator']
        
        while shard_iterator:
            records_response = client.get_records(
                ShardIterator=shard_iterator,
                Limit=1000
            )
            records = records_response.get('Records', [])
            process_records(records)
            
            shard_iterator = records_response.get('NextShardIterator')
            if not shard_iterator or not records:
                break
```

## Common Scenarios

### Exporting an Entire Table for Analytics

A data pipeline runs a scan without pagination to export the entire table. The scan returns only the first 1MB of data, causing incomplete exports. The fix is to implement full pagination using `LastEvaluatedKey`, or use DynamoDB Export to S3 for large datasets.

### Real-Time Dashboard with Incomplete Data

A monitoring dashboard queries the last 24 hours of data without checking `LastEvaluatedKey`. The dashboard shows incomplete results when traffic exceeds 1MB. The fix is to either paginate all results or set an appropriate `Limit` parameter.

### Batch Processing with Large Items

An ETL job processes items one page at a time using `Limit`. When items are large (300KB+), a page of 10 items quickly exceeds 1MB, causing early truncation. Reduce the `Limit` value so each page stays well under 1MB.

## Prevent It

- Always check for `LastEvaluatedKey` in every query and scan response
- Implement robust pagination logic in all data access layers
- Use the `Limit` parameter to keep page sizes manageable
- Prefer query over scan whenever possible
- Use parallel scan for full-table operations on large tables
- Monitor `ReturnedItemCount` and `ScannedCount` CloudWatch metrics
- Set up alerts for scan operations that return partial results
- Use DynamoDB Export to S3 for data analytics workloads instead of full scans

## Related Pages

- [DynamoDB Filter Expression Error](/tools/dynamodb/dynamodb-filter-error)
- [DynamoDB Projection Expression Error](/tools/dynamodb/dynamodb-projection-error)
- [DynamoDB Throughput Error](/tools/dynamodb/dynamodb-throughput-error)
