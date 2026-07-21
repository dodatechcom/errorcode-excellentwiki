---
title: "[Solution] AWS Stage Not Found"
description: "NotFoundException for stage."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Stage Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Stage name incorrect
- Deleted

## How to Fix

### List stages

```bash
aws apigateway get-stages --rest-api abc123
```

## Examples

- Example scenario: stage name incorrect
- Example scenario: deleted

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
