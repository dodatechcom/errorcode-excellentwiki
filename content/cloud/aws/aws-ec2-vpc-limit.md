---
title: "[Solution] AWS EC2 VPC Limit Exceeded"
description: "MaxVpcLimitExceeded when VPC resource limits are reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 VPC Limit Exceeded` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Maximum VPCs per region reached (default 5)
- Subnets per VPC limit reached
- Security groups per VPC limit reached
- Route tables per VPC limit reached

## How to Fix

### Check VPC count

```bash
aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,CidrBlock]' --output table
```
### Request VPC limit increase

```bash
aws service-quotas request-service-quota-increase --service-code ec2 --quota-code L-F678F1CE --desired-value 10 --region us-east-1
```
### Delete unused VPCs

```bash
aws ec2 delete-vpc --vpc-id vpc-unused
```

## Examples

- 5 VPCs in us-east-1 and tries to create 6th
- Subnet limit of 200 per VPC reached

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Subnet Not Found]({{< relref "/cloud/aws/aws-ec2-subnet-not-found" >}}) -- Subnet errors
