---
title: "[Solution] AWS Shield Advanced"
description: "AccessDenied for Shield."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Shield Advanced` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Subscription not active
- Resource ID invalid
- Protection not exist

## How to Fix

### List protections

```bash
shield list-protections
```

## Examples

- Example scenario: subscription not active
- Example scenario: resource id invalid
- Example scenario: protection not exist

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
