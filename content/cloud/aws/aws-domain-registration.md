---
title: "[Solution] AWS Domain Registration"
description: "InvalidDomainSummary."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Domain Registration` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Domain exists for other account
- Not available

## How to Fix

### List domains

```bash
aws route53domains list-domains
```

## Examples

- Example scenario: domain exists for other account
- Example scenario: not available

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
