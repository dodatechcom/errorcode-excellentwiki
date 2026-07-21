---
title: "[Solution] AWS Invalid AMI ID"
description: "InvalidAMIID.NotFound for the AMI identifier."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Invalid AMI ID` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Typo in the AMI ID
- AMI belongs to other region
- AMI deregistered by owner
- Wrong AMI format

## How to Fix

### Verify AMI

```bash
aws ec2 describe-images --image-ids ami-0abc
```

### Search AMIs

```bash
aws ec2 describe-images --owners self amazon --query Images[*].ImageId
```

## Examples

- Example scenario: typo in the ami id
- Example scenario: ami belongs to other region
- Example scenario: ami deregistered by owner
- Example scenario: wrong ami format

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
