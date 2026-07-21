---
title: "[Solution] AWS Certificate Not Found"
description: "ResourceNotFoundException for ACM."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Certificate Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Certificate not exist
- Deleted
- Domain mismatch

## How to Fix

### List certificates

```bash
aws acm list-certificates
```

## Examples

- Example scenario: certificate not exist
- Example scenario: deleted
- Example scenario: domain mismatch

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
