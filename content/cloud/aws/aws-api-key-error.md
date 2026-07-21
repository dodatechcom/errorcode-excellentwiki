---
title: "[Solution] AWS API Key Error"
description: "Forbidden for API key issues."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `API Key Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Key missing
- Key deactivated
- Plan mismatch

## How to Fix

### List API keys

```bash
aws apigateway get-api-keys
```

## Examples

- Example scenario: key missing
- Example scenario: key deactivated
- Example scenario: plan mismatch

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
