---
title: "[Solution] AWS CloudHSM"
description: "CloudHsmAccessDenied."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `CloudHSM` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- HSM not provisioned
- Client IP not authorized

## How to Fix

### List clusters

```bash
cloudhsm list-clusters
```

## Examples

- Example scenario: hsm not provisioned
- Example scenario: client ip not authorized

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
