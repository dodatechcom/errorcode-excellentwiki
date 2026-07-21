---
title: "[Solution] AWS EC2 Security Group Not Found"
description: "InvalidGroup.NotFound when the specified security group does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Security Group Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The security group ID is incorrect
- The security group was deleted
- The security group is in a different VPC
- Using name instead of ID

## How to Fix

### Describe security group

```bash
aws ec2 describe-security-groups --group-ids sg-0abc123 --region us-east-1
```
### List all security groups

```bash
aws ec2 describe-security-groups --query 'SecurityGroups[*].[GroupId,GroupName,VpcId]' --output table
```
### Create new security group

```bash
aws ec2 create-security-group --group-name my-sg --description 'My security group' --vpc-id vpc-0abc123
```

## Examples

- Using sg-deleted instead of current security group
- SG in VPC-1 but instance in VPC-2

## Related Errors

- [VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) -- VPC errors
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
