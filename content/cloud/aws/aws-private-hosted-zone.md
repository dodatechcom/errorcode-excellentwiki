---
title: "[Solution] AWS Private Hosted Zone"
description: "InvalidVPCId for private zones."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Private Hosted Zone` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- No VPC associated
- Private zone not for this VPC

## How to Fix

### List by VPC

```bash
aws route53 list-hosted-zones-by-vpc --vpc vpc-abc
```

## Examples

- Example scenario: no vpc associated
- Example scenario: private zone not for this vpc

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
