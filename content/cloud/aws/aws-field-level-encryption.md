---
title: "[Solution] AWS Field Level Encryption"
description: "NotFound for field-level encryption."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Field Level Encryption` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Config not found
- Profile not exist
- Key not configured

## How to Fix

### List field-level enc

```bash
aws cloudfront list-field-level-encryption-configs
```

## Examples

- Example scenario: config not found
- Example scenario: profile not exist
- Example scenario: key not configured

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
