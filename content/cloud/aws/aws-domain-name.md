---
title: "[Solution] AWS Domain Name"
description: "NotFoundException for custom domain."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Domain Name` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Domain not set up
- ACM cert mismatch

## How to Fix

### List domains

```bash
aws apigateway get-domain-names
```

## Examples

- Example scenario: domain not set up
- Example scenario: acm cert mismatch

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
