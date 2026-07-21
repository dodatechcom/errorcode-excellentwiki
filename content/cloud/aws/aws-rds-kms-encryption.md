---
title: "[Solution] AWS RDS KMS Encryption"
description: "KMS.KeyUnavailableException for RDS."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS KMS Encryption` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Key disabled
- Key policy denies RDS
- Region mismatch

## How to Fix

### Describe key

```bash
aws kms describe-key --key-id alias/rds-key
```

## Examples

- Example scenario: key disabled
- Example scenario: key policy denies rds
- Example scenario: region mismatch

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
