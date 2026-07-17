---
title: "[Solution] AWS SNS — Topic does not exist"
description: "Fix AWS SNS Topic does not exist. Resolve SNS topic ARN and access issues."
cloud: ["aws"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["aws", "sns", "topic", "not-found", "arn", "publish", "subscribe"]
weight: 5
---

An SNS "Topic does not exist" error means the specified topic ARN cannot be found. The topic may have been deleted, the ARN may be incorrect, or the account may not have permission to view it.

## What This Error Means

Amazon SNS uses ARNs (Amazon Resource Names) to identify topics. When you publish or subscribe to a topic, SNS validates that the ARN exists in the specified account and region. If the topic was deleted, the ARN is mistyped, or you are querying a different region, SNS returns `NotFound` or `InvalidSecurity` for the topic. The error can also indicate cross-account access issues where the topic exists but is not shared with your account.

## Common Causes

- Topic ARN is incorrect (wrong account ID, region, or topic name)
- Topic was deleted and not recreated
- Cross-account publishing without a resource-based policy
- Wrong AWS region in the topic ARN
- IAM policy does not allow SNS operations on the topic
- Topic exists in a different account that hasn't granted access

## How to Fix

### List Available Topics

```bash
aws sns list-topics --region us-east-1
```

### Verify Topic ARN

```bash
aws sns get-topic-attributes \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic
```

### Create Topic if Missing

```bash
aws sns create-topic --name my-topic --region us-east-1
```

### Fix Cross-Account Publish

```bash
aws sns add-permission \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --label cross-account-publish \
  --aws-account-id 999888777666 \
  --action-name Publish
```

### Check Topic Exists in Correct Region

```bash
# List topics in all regions
for region in us-east-1 us-west-2 eu-west-1; do
  echo "=== $region ==="
  aws sns list-topics --region $region
done
```

### Subscribe to Topic

```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --protocol email \
  --notification-endpoint admin@example.com
```

### Verify Permissions

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/my-role \
  --action-names sns:Publish sns:Subscribe \
  --resource-arns arn:aws:sns:us-east-1:123456789012:my-topic
```

## Related Errors

- [AWS SQS Error]({{< relref "/cloud/aws/aws-sqs-error-v2" >}}) — SQS invalid token
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error-v2" >}}) — IAM access denied
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
