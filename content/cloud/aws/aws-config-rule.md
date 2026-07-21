---
title: "[Solution] AWS Config Rule"
description: "ResourceNotFoundException for Config."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Config Rule` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Rule not exist
- Recording not enabled

## How to Fix

### Describe config rules

```bash
aws configservice describe-config-rules
```

## Examples

- Example scenario: rule not exist
- Example scenario: recording not enabled

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
