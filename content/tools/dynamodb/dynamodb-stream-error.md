---
title: "[Solution] DynamoDB Stream Error - Fix DynamoDB Streams Read Error"
description: "Fix DynamoDB Streams read errors. Resolve shard iterator, stream access, and lambda trigger issues for DynamoDB Streams."
tools: ["dynamodb"]
error-types: ["stream-error"]
severities: ["error"]
weight: 5
---

This error means DynamoDB Streams cannot be read or the stream iterator has expired. Streams record item-level changes but have strict iterator and access requirements.

## What This Error Means

When reading from DynamoDB Streams fails, you see:

```
ExpiredIteratorException: Shard iterator has expired
# or
ResourceNotFoundException: Stream not found
# or
ProvisionedThroughputExceededException: Rate exceeded for stream
```

Stream iterators expire after 24 hours. If you do not read records within that window, you lose access to unread records.

## Why It Happens

- The shard iterator has expired (older than 24 hours)
- Streams are not enabled on the table
- The IAM role lacks `dynamodb:GetRecords` permission
- The stream ARN is incorrect or points to a deleted stream
- The read capacity for the stream is throttled
- A Lambda trigger is not processing records fast enough

## How to Fix It

### Check if streams are enabled

```python
import boto3

dynamodb = boto3.client('dynamodb')
response = dynamodb.describe_table(TableName='my-table')
stream_spec = response['Table'].get('StreamSpecification', {})
print(stream_spec)  # {'StreamEnabled': True, 'StreamViewType': 'NEW_AND_OLD_IMAGES'}
```

### Enable streams on the table

```python
dynamodb.update_table(
    TableName='my-table',
    StreamSpecification={
        'StreamEnabled': True,
        'StreamViewType': 'NEW_AND_OLD_IMAGES'
    }
)
```

### Get a fresh shard iterator

```python
streams = boto3.client('dynamodbstreams')
response = streams.describe_stream(StreamArn='arn:aws:dynamodb:...')
stream_id = response['StreamDescription']['StreamArn']

shard_id = response['StreamDescription']['Shards'][0]['ShardId']
response = streams.get_shard_iterator(
    StreamArn=stream_id,
    ShardId=shard_id,
    ShardIteratorType='TRIM_HORIZON'
)
```

### Read records from the stream

```python
iterator = response['ShardIterator']
while iterator:
    response = streams.get_records(ShardIterator=iterator, Limit=100)
    for record in response['Records']:
        print(record['eventName'], record['dynamodb'])
    iterator = response.get('NextShardIterator')
```

### Check Lambda trigger logs

```bash
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/my-stream-processor
```

Lambda triggers on DynamoDB Streams must handle shard iteration.

### List available streams

```python
response = streams.list_streams(TableName='my-table')
for stream in response['Streams']:
    print(stream['StreamArn'], stream['StreamViewType'])
```

### Handle shard splits and merges

```python
# Check for child shards
response = streams.get_shard_iterator(
    StreamArn=stream_arn,
    ShardId='shardId-000000000000',
    ShardIteratorType='LATEST'
)
```

## Common Mistakes

- Not processing stream records within the 24-hour iterator window
- Forgetting to enable streams when creating a table
- Not monitoring Lambda trigger errors on stream processing
- Using TRIM_HORIZON which reads from the beginning of the stream
- Assuming streams are automatically enabled (they are not)

## Related Pages

- [DynamoDB Query Error]({{< relref "/tools/dynamodb/dynamodb-query-error" >}}) -- query issues
- [DynamoDB Access Denied]({{< relref "/tools/dynamodb/dynamodb-access-denied" >}}) -- permission errors
- [DynamoDB Validation Error]({{< relref "/tools/dynamodb/dynamodb-validation-error" >}}) -- validation issues
