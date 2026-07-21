---
title: "[Solution] AWS DNSSEC"
description: "InvalidSigningStatus."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DNSSEC` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- KSK not created
- DNSSEC not enabled
- Key not ACTIVE

## How to Fix

### Check DNSSEC

```bash
aws route53 get-dnssec --hosted-zone ZONE123
```

## Examples

- Example scenario: ksk not created
- Example scenario: dnssec not enabled
- Example scenario: key not active

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
