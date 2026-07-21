---
title: "[Solution] AWS KMS Key Usage"
description: "ValidationException for key usage."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `KMS Key Usage` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Usage mismatch (ENCRYPT vs SIGN)
- Forbidden operation

## How to Fix

### Describe key

```bash
aws kms describe-key --key-id alias/my-key
```

## Examples

- Example scenario: usage mismatch (encrypt vs sign)
- Example scenario: forbidden operation

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
