---
title: "[Solution] AWS SNS Publish Failed"
description: "Fix AWS SNS publish errors. Resolve SNS message delivery issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "sns", "publish", "notification", "topic"]
weight: 5
---

An AWS SNS publish failed error occurs when messages cannot be published to an SNS topic. This can be caused by topic configuration, permissions, or subscription issues.

## Common Causes

- Topic ARN is incorrect or topic does not exist
- IAM permissions not granted for sns:Publish
- Message is too large (256KB limit)
- Subscription protocol not configured correctly
- KMS key for encrypted topic not accessible

## How to Fix

### Check Topic Exists

```bash
aws sns list-topics
aws sns get-topic-attributes --topic-arn arn:aws:sns:us-east-1:123456789:my-topic
```

### Publish Test Message

```bash
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic \
  --message "Test message"
```

### Check Subscriptions

```bash
aws sns list-subscriptions-by-topic \
  --topic-arn arn:aws:sns:us-east-1:123456789:my-topic
```

### Verify Permissions

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/my-role \
  --action-names sns:Publish
```

## Examples

```bash
# Example 1: Topic not found
# InvalidParameter: Invalid parameter: Topic ARN
# Fix: verify topic ARN

# Example 2: Access denied
# AuthorizationError: User is not authorized to perform sns:Publish
# Fix: add sns:Publish permission
```

## Related Errors

- [AWS SQS Error]({{< relref "/cloud/aws/aws-sqs-error" >}}) — SQS send failed
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function error
