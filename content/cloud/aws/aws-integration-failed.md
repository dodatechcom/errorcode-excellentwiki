---
title: "[Solution] AWS Integration Failed"
description: "BadRequestException for integration."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Integration Failed` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Type not set
- Endpoint unreachable
- Timeout 29s

## How to Fix

### Get integration

```bash
aws apigateway get-integration --rest-api abc123 --resource def456 --http GET
```

## Examples

- Example scenario: type not set
- Example scenario: endpoint unreachable
- Example scenario: timeout 29s

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
