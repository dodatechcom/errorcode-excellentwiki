---
title: "[Solution] AWS Alias Target"
description: "InvalidChangeBatch for alias."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Alias Target` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Target not exist
- ELB/CF DNS mismatch

## How to Fix

### Get alias

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: target not exist
- Example scenario: elb/cf dns mismatch

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
