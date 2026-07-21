---
title: "[Solution] AWS Canary Deployment"
description: "BadRequestException for canary."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Canary Deployment` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Canary not enabled
- Invalid traffic percentage

## How to Fix

### Get stage

```bash
aws apigateway get-stage --rest-api abc123 --stage prod
```

## Examples

- Example scenario: canary not enabled
- Example scenario: invalid traffic percentage

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
