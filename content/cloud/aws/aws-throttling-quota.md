---
title: "[Solution] AWS Throttling Quota"
description: "LimitExceededException for throttling."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Throttling Quota` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Account limit 10000 RPS
- Usage plan exceeded

## How to Fix

### Check plan

```bash
aws apigateway get-usage-plan --plan-id plan123
```

## Examples

- Example scenario: account limit 10000 rps
- Example scenario: usage plan exceeded

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
