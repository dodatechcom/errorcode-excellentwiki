---
title: "[Solution] AWS Custom Key Store"
description: "CustomKeyStoreNotFoundException for CloudHSM."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Custom Key Store` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- HSM cluster not active
- Store ID invalid
- Proxy auth failed

## How to Fix

### List custom stores

```bash
aws kms list-custom-key-stores
```

## Examples

- Example scenario: hsm cluster not active
- Example scenario: store id invalid
- Example scenario: proxy auth failed

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
