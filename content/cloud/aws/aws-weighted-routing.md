---
title: "[Solution] AWS Weighted Routing"
description: "InvalidChangeBatch for weighted."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Weighted Routing` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Sum of weights zero
- Identifier missing

## How to Fix

### List records

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: sum of weights zero
- Example scenario: identifier missing

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
