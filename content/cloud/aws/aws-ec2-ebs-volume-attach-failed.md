---
title: "[Solution] AWS EBS Volume Attach Failed"
description: "VolumeAttachmentError when an EBS volume cannot be attached to an EC2 instance."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EBS Volume Attach Failed` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Volume is already attached to another instance
- Instance and volume are in different Availability Zones
- Volume is in a different account or region
- Volume is in wrong state (creating, deleted)
- Instance does not support the volume type

## How to Fix

### Describe volume status

```bash
aws ec2 describe-volumes --volume-ids vol-0abc123
```

### Attach volume

```bash
aws ec2 attach-volume --volume-id vol-0abc123 --instance-id i-0abc123 --device /dev/xvdf
```

### Detach first if attached

```bash
aws ec2 detach-volume --volume-id vol-0abc123
```

### Check instance compatibility

```bash
aws ec2 describe-instance-types --instance-types c5.xlarge
```

### Confirm same AZ

```bash
aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].Placement.AvailabilityZone'
```

## Examples

- Example scenario: volume is already attached to another instance
- Example scenario: instance and volume are in different availability zones
- Example scenario: volume is in a different account or region
- Example scenario: volume is in wrong state (creating, deleted)

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
