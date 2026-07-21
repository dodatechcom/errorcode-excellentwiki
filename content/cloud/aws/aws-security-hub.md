---
title: "[Solution] AWS Security Hub"
description: "AccessDeniedException for Security Hub."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Security Hub` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Not enabled
- Member not invited

## How to Fix

### Enable Security Hub

```bash
aws securityhub enable-security-hub
```

## Examples

- Example scenario: not enabled
- Example scenario: member not invited

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
