---
title: "[Solution] AWS Secret Key Mismatch"
description: "SignatureDoesNotMatch for wrong secret key."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Secret Key Mismatch` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Access key and secret mismatch
- Old secret cached

## How to Fix

### Create new pair

```bash
aws iam create-access-key
```

## Examples

- Example scenario: access key and secret mismatch
- Example scenario: old secret cached

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
