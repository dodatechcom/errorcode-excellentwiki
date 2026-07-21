---
title: "[Solution] AWS Method Not Defined"
description: "NotFoundException for method."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Method Not Defined` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Method not enabled
- Not in API def

## How to Fix

### Get method

```bash
aws apigateway get-method --rest-api abc123 --resource def456 --http POST
```

## Examples

- Example scenario: method not enabled
- Example scenario: not in api def

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
