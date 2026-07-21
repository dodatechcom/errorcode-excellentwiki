---
title: "[Solution] AWS NS Delegation"
description: "InvalidChangeBatch for NS."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `NS Delegation` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Less than 2 NS records
- TTL mismatch

## How to Fix

### Get NS records

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123 --filter Type=NS
```

## Examples

- Example scenario: less than 2 ns records
- Example scenario: ttl mismatch

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
