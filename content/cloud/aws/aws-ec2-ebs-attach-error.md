---
title: "[Solution] AWS EC2 EBS Volume Attach Error"
description: "IncorrectState or VolumeInUse when attaching an EBS volume."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 EBS Volume Attach Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The volume is already attached to another instance
- The instance is not in the same AZ as the volume
- The volume is in a FAILED state
- Attachment limits exceeded

## How to Fix

### Check volume state

```bash
aws ec2 describe-volumes --volume-ids vol-0abc123
```
### Detach volume

```bash
aws ec2 detach-volume --volume-id vol-0abc123 --instance-id i-0abc --force
```
### Attach volume

```bash
aws ec2 attach-volume --volume-id vol-0abc123 --instance-id i-0abc123 --device /dev/sdf
```
### Verify AZ match

```bash
aws ec2 describe-volumes --volume-ids vol-0abc123 --query 'Volumes[*].[VolumeId,AvailabilityZone]'
```

## Examples

- Volume already attached to instance i-old and trying to attach to i-new
- Volume in us-east-1b but instance in us-east-1a

## Related Errors

- [EBS Volume Not Found]({{< relref "/cloud/aws/aws-ebs-volume-not-found" >}}) -- Volume not found
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
