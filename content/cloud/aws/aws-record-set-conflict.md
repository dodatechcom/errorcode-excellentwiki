---
title: "[Solution] AWS Record Set Conflict"
description: "InvalidChangeBatch."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Record Set Conflict` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Record exists with same name/type
- CNAME at apex

## How to Fix

### List records

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: record exists with same name/type
- Example scenario: cname at apex

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
