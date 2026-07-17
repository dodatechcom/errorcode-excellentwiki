---
title: "[Solution] AWS Lambda Function Error"
description: "Fix AWS Lambda function errors. Resolve Lambda execution and configuration issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "lambda", "function", "serverless", "execution"]
weight: 5
---

An AWS Lambda error occurs when a Lambda function fails to execute, times out, or encounters a configuration error.

## Common Causes

- Function handler does not exist or has wrong path
- Runtime timeout exceeded
- Insufficient IAM permissions for the execution role
- Memory limit too low
- Environment variables or layers misconfigured

## How to Fix

### Check Lambda Logs

```bash
aws logs tail /aws/lambda/my-function --since 1h
```

### Test Function

```bash
aws lambda invoke \
  --function-name my-function \
  --payload '{"key": "value"}' \
  response.json
```

### Check Execution Role

```bash
aws lambda get-function-configuration \
  --function-name my-function \
  --query 'Role'
```

### Increase Timeout

```bash
aws lambda update-function-configuration \
  --function-name my-function \
  --timeout 300
```

### Increase Memory

```bash
aws lambda update-function-configuration \
  --function-name my-function \
  --memory-size 512
```

## Examples

```bash
# Example 1: Handler not found
# Runtime.HandlerNotFound: index.handler
# Fix: check handler path and function name

# Example 2: Timeout
# Task timed out after 3 seconds
# Fix: increase timeout or optimize function
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
- [AWS API Gateway Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) — API Gateway error
