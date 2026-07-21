---
title: "[Solution] AWS Deployment Error"
description: "BadRequestException for deployment."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Deployment Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- ID already exists
- Stage not supported

## How to Fix

### Create deployment

```bash
aws apigateway create-deployment --rest-api abc123 --stage prod
```

## Examples

- Example scenario: id already exists
- Example scenario: stage not supported

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
