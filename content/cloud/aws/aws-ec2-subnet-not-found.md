---
title: "[Solution] AWS EC2 Subnet Not Found"
description: "InvalidSubnet.NotFound when the specified subnet does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Subnet Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The subnet ID is incorrect
- The subnet was deleted
- The subnet is in a different VPC
- The subnet is in a different region

## How to Fix

### Describe subnet

```bash
aws ec2 describe-subnets --subnet-ids subnet-0abc123 --region us-east-1
```
### List subnets in VPC

```bash
aws ec2 describe-subnets --filters Name=vpc-id,Values=vpc-0abc123 --query 'Subnets[*].[SubnetId,CidrBlock,AvailabilityZone]' --output table
```
### Create subnet

```bash
aws ec2 create-subnet --vpc-id vpc-0abc123 --cidr-block 10.0.3.0/24 --availability-zone us-east-1c
```

## Examples

- Subnet in VPC-1 but instance in VPC-2
- Subnet deleted but still referenced in launch template

## Related Errors

- [VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) -- VPC errors
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
