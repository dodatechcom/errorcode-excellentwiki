---
title: "[Solution] AWS EC2 Instance Limit Exceeded"
description: "InstanceLimitExceeded when the account has reached the maximum number of running instances."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Instance Limit Exceeded` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Account vCPU limit for the instance family is reached
- On-Demand instance count limit exceeded
- Running Dedicated Host limit reached
- Reserved instance limits hit

## How to Fix

### Check current limits

```bash
aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --region us-east-1
```
### Request limit increase

```bash
aws service-quotas request-service-quota-increase --service-code ec2 --quota-code L-1216C47A --desired-value 500 --region us-east-1
```
### List running instances by type

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceType,State.Name]' --output json
```

## Examples

- Requesting 500 m5.large instances exceeds the default vCPU quota
- Running 5 p3.16xlarge exceeds GPU instance limits

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Insufficient Capacity]({{< relref "/cloud/aws/aws-ec2-insufficient-capacity" >}}) -- Capacity issues
