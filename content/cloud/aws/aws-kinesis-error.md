---
title: "[Solution] AWS Kinesis Error — stream/shard/consumer/iterator failures"
description: "Fix AWS Kinesis errors. Resolve stream, shard, consumer, and iterator issues."
error-types: ["api-error"]
severities: ["error"]
weight: 140
---

An AWS Kinesis error occurs when streams fail to create, shards cannot be split, or consumers encounter iterator errors. Kinesis Data Streams provides real-time data streaming but requires careful shard and consumer management.

## Common Causes

- Shard count insufficient for throughput
- Iterator expired or out of range (Trim Horizon issues)
- Producers exceed shard write capacity (5 MB/s per shard)
- Consumer poll timeout too short
- KMS encryption key not accessible

## How to Fix

### Describe Stream

```bash
aws kinesis describe-stream \
  --stream-name my-stream \
  --query 'StreamDescription.{Status:StreamStatus,Shards:Shards[*].ShardId}'
```

### Increase Shard Count

```bash
aws kinesis update-shard-count \
  --stream-name my-stream \
  --target-shard-count 4 \
  --scaling-type UNIFORM_SCALING
```

### Get Shard Iterator

```bash
aws kinesis get-shard-iterator \
  --stream-name my-stream \
  --shard-id shardId-000000000000 \
  --shard-iterator-type TRIM_HORIZON
```

### Get Records

```bash
aws kinesis get-records \
  --shard-iterator iterator-xxx \
  --limit 100
```

### Register Consumer

```bash
aws kinesis register-stream-consumer \
  --stream-arn arn:aws:kinesis:us-east-1:123456789012:stream/my-stream \
  --consumer-name my-consumer
```

## Examples

```bash
# Example 1: Provisioned throughput exceeded
# ProvisionedThroughputExceededException: Rate exceeded
# Fix: increase shard count or implement exponential backoff

# Example 2: Iterator expired
# ExpiredIteratorException: Iterator expired
# Fix: get new shard iterator from TRIM_HORIZON
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda consumer errors
- [AWS Firehose Error]({{< relref "/cloud/aws/aws-cloudwatch-logs-error" >}}) — Firehose delivery errors
