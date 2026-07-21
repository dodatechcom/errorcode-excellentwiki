---
title: "[Solution] AWS Resource Path"
description: "BadRequestException for path."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Resource Path` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Path not matched
- Param not defined

## How to Fix

### List resources

```bash
aws apigateway get-resources --rest-api abc123
```

## Examples

- Example scenario: path not matched
- Example scenario: param not defined

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
