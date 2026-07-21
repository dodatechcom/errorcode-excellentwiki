---
title: "[Solution] AWS REST API Not Found"
description: "NotFoundException for REST API."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `REST API Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- API ID incorrect
- API deleted
- Region missmatch

## How to Fix

### List APIs

```bash
aws apigateway get-rest-apis
```

## Examples

- Example scenario: api id incorrect
- Example scenario: api deleted
- Example scenario: region missmatch

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
