---
title: "[Solution] AWS EC2 Instance Insufficient Capacity"
description: "InsufficientInstanceCapacity when EC2 cannot launch due to AZ resource exhaustion."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Instance Insufficient Capacity` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Capacity not available in the specified Availability Zone
- Other workloads have consumed available resources in the AZ
- Instance type is temporarily constrained in the region
- AWS is experiencing high demand in the AZ
- On-Demand Capacity Reservations were not requested

## How to Fix

### Check capacity in other AZs

```bash
aws ec2 describe-availability-zones --region us-east-1
```

### Try different instance type

```bash
aws ec2 run-instances --image-id ami-0abcdef --instance-type c5a.xlarge --count 1
```

### Request Capacity Reservations

```bash
aws ec2 create-capacity-reservation --instance-type c5.xlarge --instance-count 1 --availability-zone us-east-1a
```

### Check existing reservations

```bash
aws ec2 describe-capacity-reservations
```

### Launch with capacity block

```bash
aws ec2 run-instances --image-id ami-0abcdef --capacity-reservation-specification CapacityReservationPreference=open
```

## Examples

- Example scenario: capacity not available in the specified availability zone
- Example scenario: other workloads have consumed available resources in the az
- Example scenario: instance type is temporarily constrained in the region
- Example scenario: aws is experiencing high demand in the az

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
