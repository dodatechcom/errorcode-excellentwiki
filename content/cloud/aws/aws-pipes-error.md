---
title: "[Solution] AWS EventBridge Pipes Error — source/filter/enrichment failures"
description: "Fix AWS EventBridge Pipes errors. Resolve pipe source, filter, and enrichment issues."
error-types: ["api-error"]
severities: ["error"]
weight: 150
---

An AWS EventBridge Pipes error occurs when pipes fail to process events, filters return empty results, or enrichment functions encounter errors. Pipes connect event sources to targets with filtering and enrichment.

## Common Causes

- Source and target ARN mismatch or inaccessible
- Event pattern filter returns zero matches
- Enrichment Lambda function timeout
- IAM role lacks permissions for source/target
- Pipe in CREATING state not yet ready

## How to Fix

### List Pipes

```bash
aws pipes list-pipes \
  --query 'pipes[*].{Name:Name,State:CurrentState,Source:Source}'
```

### Describe Pipe

```bash
aws pipes describe-pipe \
  --name my-pipe
```

### Create Pipe

```bash
aws pipes create-pipe \
  --name my-pipe \
  --source arn:aws:sqs:us-east-1:123456789012:my-queue \
  --target arn:aws:lambda:us-east-1:123456789012:function:my-function \
  --role-arn arn:aws:iam::123456789012:role/PipesRole \
  --source-parameters '{"sqsQueueParameters":{"BatchSize":10}}'
```

### Update Pipe

```bash
aws pipes update-pipe \
  --name my-pipe \
  --source-parameters '{"sqsQueueParameters":{"BatchSize":25}}'
```

### Start Pipe

```bash
aws pipes start-pipe --name my-pipe
```

## Examples

```bash
# Example 1: Source not accessible
# ServiceQuotaExceededException: Source not found
# Fix: verify source ARN and IAM role permissions

# Example 2: Enrichment timeout
# EnrichmentTimeoutException: Lambda timed out
# Fix: increase Lambda timeout or simplify enrichment logic
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS SQS Error]({{< relref "/cloud/aws/aws-sqs-error" >}}) — SQS queue errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
