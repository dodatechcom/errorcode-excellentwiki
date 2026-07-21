---
title: "[Solution] AWS EC2 Insufficient Capacity"
description: "InsufficientInstanceCapacity when EC2 cannot launch due to AZ resource exhaustion."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Insufficient Capacity` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Capacity not available in the specified AZ
- AZ resource exhaustion due to other workloads
- Instance type temporarily constrained
- AWS high demand in the AZ

## How to Fix

### Check capacity in other AZs

```bash
aws ec2 describe-availability-zones --region us-east-1
```

### Try different instance type

```bash
aws ec2 run-instances --image-id ami-0abcdef --instance-type c5a.xlarge --count 1
```

## Examples

- Example scenario: capacity not available in the specified az
- Example scenario: az resource exhaustion due to other workloads
- Example scenario: instance type temporarily constrained
- Example scenario: aws high demand in the az

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
