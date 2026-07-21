---
title: "[Solution] AWS Volume Type Incompatibility"
description: "VolumeTypeNotSupported when the volume type is not compatible with the instance."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Volume Type Incompatibility` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Instance does not support io2 Block Express volumes
- Instance type lacks NVMe driver support
- Maximum throughput per volume exceeded
- Maximum IOPS per instance exceeded for volume type
- EBS-optimization not enabled on instance

## How to Fix

### Check EBS optimization

```bash
aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].EbsOptimized'
```

### Modify EBS optimization

```bash
aws ec2 modify-instance-attribute --instance-id i-0abc123 --ebs-optimized true
```

### Check supported volume types

```bash
aws ec2 describe-instance-types --instance-types c5.xlarge --query 'InstanceTypes[*].EbsInfo'
```

### Convert volume type

```bash
aws ec2 modify-volume --volume-id vol-0abc123 --volume-type gp3
```

### Create snapshot first

```bash
aws ec2 create-snapshot --volume-id vol-0abc123 --description Pre-migration
```

## Examples

- Example scenario: instance does not support io2 block express volumes
- Example scenario: instance type lacks nvme driver support
- Example scenario: maximum throughput per volume exceeded
- Example scenario: maximum iops per instance exceeded for volume type

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
