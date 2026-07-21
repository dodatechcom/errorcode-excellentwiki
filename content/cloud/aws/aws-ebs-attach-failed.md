---
title: "[Solution] AWS EBS attach failed"
description: "VolumeAttachmentError when an EBS volume cannot attach."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EBS attach failed` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Volume already attached elsewhere
- Volume and instance in different AZ
- Volume in the wrong state

## How to Fix

### Describe volume

```bash
aws ec2 describe-volumes --volume-ids vol-0abc
```

### Attach

```bash
aws ec2 attach-volume --vol vol-0abc --ins i-0abc --dev /dev/xvdf
```

### Detach first

```bash
aws ec2 detach-volume --vol vol-0abc
```

## Examples

- Example scenario: volume already attached elsewhere
- Example scenario: volume and instance in different az
- Example scenario: volume in the wrong state

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
