---
title: "[Solution] AWS Multivalue Answer"
description: "InvalidChangeBatch for multivalue."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Multivalue Answer` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Multiple records with same name required

## How to Fix

### Check multivalue

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: multiple records with same name required

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
