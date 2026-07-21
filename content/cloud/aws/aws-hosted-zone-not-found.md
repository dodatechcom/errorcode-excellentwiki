---
title: "[Solution] AWS Hosted Zone Not Found"
description: "NoSuchHostedZone."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Hosted Zone Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Zone ID incorrect
- Deleted
- Different account

## How to Fix

### List zones

```bash
aws route53 list-hosted-zones
```

## Examples

- Example scenario: zone id incorrect
- Example scenario: deleted
- Example scenario: different account

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
