---
title: "[Solution] AWS KMS Key Not Found"
description: "NotFoundException for KMS key."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `KMS Key Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Key ID not exist
- Deleted or pending deletion
- Wrong account/region

## How to Fix

### List keys

```bash
aws kms list-keys
```

## Examples

- Example scenario: key id not exist
- Example scenario: deleted or pending deletion
- Example scenario: wrong account/region

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
