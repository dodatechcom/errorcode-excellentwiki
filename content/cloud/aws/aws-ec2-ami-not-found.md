---
title: "[Solution] AWS EC2 AMI Not Found"
description: "InvalidAMIID.NotFound when the specified AMI does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 AMI Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The AMI ID is incorrect or deregistered
- The AMI is in a different region
- The AMI was shared and sharing revoked
- Third party AMI no longer available

## How to Fix

### Describe AMI

```bash
aws ec2 describe-images --image-ids ami-0abcdef12 --region us-east-1
```
### List owned AMIs

```bash
aws ec2 describe-images --owners self --query 'Images[*].[ImageId,Name,State]' --output table
```
### Copy AMI from another region

```bash
aws ec2 copy-image --source-image-id ami-0abc --source-region us-west-2 --name my-copied-ami --region us-east-1
```

## Examples

- Using ami-deleted123 deregistered last month
- AMI shared by another account but sharing revoked

## Related Errors

- [Invalid AMI ID]({{< relref "/cloud/aws/aws-ec2-invalid-ami-id" >}}) -- Invalid AMI
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
