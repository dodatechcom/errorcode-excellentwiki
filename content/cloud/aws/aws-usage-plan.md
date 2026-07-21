---
title: "[Solution] AWS Usage Plan"
description: "BadRequestException for usage plan."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Usage Plan` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- API not in plan
- Throttle/Quota exceeded

## How to Fix

### List plans

```bash
aws apigateway get-usage-plans
```

## Examples

- Example scenario: api not in plan
- Example scenario: throttle/quota exceeded

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
