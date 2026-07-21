---
title: "[Solution] AWS Lambda handler not found"
description: "HandlerNotFound for Lambda function."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda handler not found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Handler export name does not match
- File extension missing (.py/.js)
- Handler in subdirectory

## How to Fix

### Check config

```bash
aws lambda get-function-config --function my-function
```

### Set handler

```bash
aws lambda update-function-config --function my-function --handler index.handler
```

## Examples

- Example scenario: handler export name does not match
- Example scenario: file extension missing (.py/.js)
- Example scenario: handler in subdirectory

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
