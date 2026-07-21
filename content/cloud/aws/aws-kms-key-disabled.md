---
title: "[Solution] AWS KMS Key Disabled"
description: "DisabledException for disabled key."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `KMS Key Disabled` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Admin disabled the key
- Scheduled for deletion

## How to Fix

### Enable key

```bash
aws kms enable-key --key-id alias/MyKey
```

## Examples

- Example scenario: admin disabled the key
- Example scenario: scheduled for deletion

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
