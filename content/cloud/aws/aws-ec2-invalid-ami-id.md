---
title: "[Solution] AWS EC2 Invalid AMI ID"
description: "InvalidAMIID.Malformed when the AMI ID format is incorrect."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Invalid AMI ID` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- AMI ID does not follow ami-xxxxxxxxx format
- AMI ID contains invalid characters
- AMI ID prefix wrong for the region
- Copy-paste error in AMI ID

## How to Fix

### Verify AMI format

```bash
aws ec2 describe-images --image-ids ami-invalid --region us-east-1
```
### List available AMIs

```bash
aws ec2 describe-images --owners amazon --query 'Images[0:5].[ImageId,Name]' --output table
```
### Get latest Amazon Linux

```bash
aws ec2 describe-images --owners amazon --filters Name=name,Values=amzn2-ami-hvm-2.0.*-x86_64-gp2 --query 'sort_by(Images,&CreationDate)[-1].ImageId' --output text
```

## Examples

- Using ami-12345 instead of ami-0123456789abcdef0
- Typo: ami-0abCDef12 instead of ami-0abcdef12

## Related Errors

- [AMI Not Found]({{< relref "/cloud/aws/aws-ec2-ami-not-found" >}}) -- AMI not found
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
