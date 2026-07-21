---
title: "[Solution] AWS EBS Volume Not Found"
description: "InvalidVolumeNotFound when the specified EBS volume does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EBS Volume Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The volume ID is incorrect
- The volume was deleted
- The volume exists in a different region
- The IAM role lacks ec2:DescribeVolumes permission

## How to Fix

### Describe volume

```bash
aws ec2 describe-volumes --volume-ids vol-0abc123 --region us-east-1
```
### List all volumes

```bash
aws ec2 describe-volumes --filters Name=status,Values=available --output table
```
### Check in correct region

```bash
aws ec2 describe-volumes --volume-ids vol-0abc --region us-west-2
```

## Examples

- Volume vol-deleted returns NotFound
- Volume in us-east-1 but API call targets us-west-2

## Related Errors

- [EBS Attach Error]({{< relref "/cloud/aws/aws-ec2-ebs-attach-error" >}}) -- Volume attach errors
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
