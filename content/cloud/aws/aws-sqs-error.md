---
title: "[Solution] AWS SQS Message Send Failed"
description: "Fix AWS SQS message send failures. Resolve SQS queue issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS SQS message send failed error occurs when messages cannot be sent to an SQS queue. This can be caused by queue configuration, permissions, or throttling.

## Common Causes

- Queue does not exist or wrong region
- Message exceeds maximum size (256KB)
- IAM permissions not granted for sqs:SendMessage
- Queue is encrypted and KMS key is not accessible
- Message group ID required but not provided (FIFO queue)

## How to Fix

### Check Queue Exists

```bash
aws sqs get-queue-queue-url --queue-name my-queue
```

### Send Test Message

```bash
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue \
  --message-body "test message"
```

### Check Queue Attributes

```bash
aws sqs get-queue-attributes \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789/my-queue \
  --attribute-names All
```

### Use Large Message Support

```bash
# For messages > 256KB, use S3
aws s3 cp large-payload.json s3://my-bucket/
aws sqs send-message \
  --queue-url $QUEUE_URL \
  --message-body '{"s3_key": "large-payload.json"}'
```

## Examples

```bash
# Example 1: Queue not found
# AWS.SimpleQueueService.NonExistentQueue
# Fix: verify queue name and region

# Example 2: Message too large
# The request include a message body that exceeds the allowed size
# Fix: use S3 for large payloads
```

## Related Errors

- [AWS SNS Error]({{< relref "/cloud/aws/aws-sns-error" >}}) — SNS publish failed
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function error
