---
title: "[Solution] AWS Failover Routing"
description: "InvalidChangeBatch for failover."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Failover Routing` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Must have PRIMARY and SECONDARY
- Duplicate entries

## How to Fix

### Get failover records

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: must have primary and secondary
- Example scenario: duplicate entries

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
