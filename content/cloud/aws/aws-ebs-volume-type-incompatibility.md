---
title: "[Solution] AWS EBS Volume Type Incompatibility"
description: "VolumeTypeNotSupported when the volume type is incompatible."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EBS Volume Type Incompatibility` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- io1/io2 volume lacks provisioned IOPS
- Trying to attach sc1/st1 to unsupported instance type
- gp3 IOPS exceeds volume size limits
- Incompatible volume type migration

## How to Fix

### Check volume type

```bash
aws ec2 describe-volumes --volume-ids vol-0abc --query 'Volumes[*].[VolumeId,VolumeType,Iops,Size]'
```
### Modify volume type

```bash
aws ec2 modify-volume --volume-id vol-0abc --volume-type gp3 --iops 3000 --throughput 125
```
### Verify compatibility

```bash
aws ec2 describe-volume-status --volume-ids vol-0abc
```

## Examples

- Attaching sc1 to T2 instance that does not support Cold HDD
- io2 with 64000 IOPS on 100 GiB exceeds ratio limit

## Related Errors

- [EBS Volume Not Found]({{< relref "/cloud/aws/aws-ebs-volume-not-found" >}}) -- Volume not found
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
