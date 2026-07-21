---
title: "[Solution] AWS SOA Record"
description: "InvalidChangeBatch for SOA."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SOA Record` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- TTL cannot be changed directly

## How to Fix

### Get SOA

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123 --filter Type=SOA
```

## Examples

- Example scenario: ttl cannot be changed directly

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
