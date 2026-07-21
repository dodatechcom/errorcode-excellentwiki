---
title: "[Solution] AWS KMS Key Pending Deletion"
description: "KMSInvalidStateException for pending key."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `KMS Key Pending Deletion` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Key is pending deletion

## How to Fix

### Cancel deletion

```bash
aws kms cancel-key-deletion --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
```

## Examples

- Example scenario: key is pending deletion

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
