---
title: "[Solution] AWS GuardDuty"
description: "ResourceNotFoundException for GuardDuty."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GuardDuty` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Not enabled
- Detector ID not exist

## How to Fix

### List detectors

```bash
guardduty list-detectors
```

## Examples

- Example scenario: not enabled
- Example scenario: detector id not exist

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
