---
title: "[Solution] AWS CloudWatch Logs Error — ingestion/retention/subscription failures"
description: "Fix AWS CloudWatch Logs errors. Resolve log ingestion, retention, and subscription filter issues."
error-types: ["api-error"]
severities: ["error"]
weight: 128
---

An AWS CloudWatch Logs error occurs when logs fail to ingest, retention policies break, or subscription filters stop forwarding. CloudWatch Logs collects and monitors log data from AWS resources and applications.

## Common Causes

- Log group retention set to 0 (never expire) causing storage growth
- Subscription filter destination not accessible
- Log stream not created or already deleted
- Ingestion throttling from too many concurrent writers
- Kinesis Data Firehose delivery stream not configured

## How to Fix

### List Log Groups

```bash
aws logs describe-log-groups \
  --query 'logGroups[*].{Name:logGroupName,Retention:retentionInDays,StoredBytes:storedBytes}'
```

### Check Log Streams

```bash
aws logs describe-log-streams \
  --log-group-name /aws/myapp/errors \
  --order-by LastEventTime \
  --descending
```

### Set Retention Period

```bash
aws logs put-retention-policy \
  --log-group-name /aws/myapp/errors \
  --retention-in-days 30
```

### Create Subscription Filter

```bash
aws logs put-subscription-filter \
  --log-group-name /aws/myapp/errors \
  --filter-name my-filter \
  --filter-pattern "ERROR" \
  --destination-arn arn:aws:firehose:us-east-1:123456789012:deliverystream/my-stream
```

### Get Log Events

```bash
aws logs get-log-events \
  --log-group-name /aws/myapp/errors \
  --log-stream-name my-stream \
  --limit 10
```

## Examples

```bash
# Example 1: Subscription filter destination not found
# ResourceNotFoundException: Destination not found
# Fix: verify Firehose delivery stream ARN is correct

# Example 2: Log ingestion throttled
# ThrottlingException: Rate exceeded
# Fix: reduce log write frequency or use batch publishing
```

## Related Errors

- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) — CloudWatch metric/alarm errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS Kinesis Error]({{< relref "/cloud/aws/aws-kinesis-error" >}}) — Kinesis stream errors
