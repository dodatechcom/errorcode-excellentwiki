---
title: "[Solution] AWS Layer Not Found"
description: "ResourceNotFoundException for Lambda Layer."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Layer Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Layer ARN incorrect
- Layer was deleted
- Layer in wrong region
- Permissions not granted

## How to Fix

### List layers

```bash
aws lambda list-layers
```

## Examples

- Example scenario: layer arn incorrect
- Example scenario: layer was deleted
- Example scenario: layer in wrong region
- Example scenario: permissions not granted

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
