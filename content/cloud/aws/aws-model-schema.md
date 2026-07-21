---
title: "[Solution] AWS Model/Schema"
description: "BadRequestException for schema."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Model/Schema` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Body doesn't match schema
- Required fields missing

## How to Fix

### Get model

```bash
aws apigateway get-model --rest-api abc123 --model MyModel
```

## Examples

- Example scenario: body doesn't match schema
- Example scenario: required fields missing

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
