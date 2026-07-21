---
title: "[Solution] AWS Volume type incompatible"
description: "VolumeTypeNotSupported for the EBS volume type."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Volume type incompatible` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Instance lacks NVMe driver
- io2 Block Express unsupported
- EBS optimization off

## How to Fix

### Check EBS optimization

```bash
aws ec2 describe-instances --instance i-0abc --query EbsOptimized
```

### Modify EBS optimization

```bash
aws ec2 modify-instance-attribute --instance i-0abc --ebs-optimized true
```

## Examples

- Example scenario: instance lacks nvme driver
- Example scenario: io2 block express unsupported
- Example scenario: ebs optimization off

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
