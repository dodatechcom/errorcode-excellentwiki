---
title: "[Solution] AWS Latency Routing"
description: "InvalidChangeBatch for latency."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Latency Routing` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Alias must include region
- Invalid region ID

## How to Fix

### List records

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: alias must include region
- Example scenario: invalid region id

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
