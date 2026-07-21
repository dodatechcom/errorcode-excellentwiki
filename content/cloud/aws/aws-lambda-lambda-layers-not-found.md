---
title: "[Solution] AWS Lambda Layers Not Found"
description: "ResourceNotFoundException for Lambda Layer references."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Layers Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Layer version ARN is incorrect
- Layer was deleted
- Layer is in wrong region
- Layer permission not granted to the account
- Layer version limit reached

## How to Fix

### List layers

```bash
aws lambda list-layers
```

### List layer versions

```bash
aws lambda list-layer-versions --layer-name my-layer
```

## Examples

- Example scenario: layer version arn is incorrect
- Example scenario: layer was deleted
- Example scenario: layer is in wrong region
- Example scenario: layer permission not granted to the account

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
