---
title: "[Solution] AWS EC2 Instance Launch Failed"
description: "Fix AWS EC2 instance launch errors. Resolve EC2 provisioning issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS EC2 instance launch failed error occurs when AWS cannot create or start an EC2 instance. This can be caused by resource limits, configuration issues, or network problems.

## Common Causes

- Instance limit exceeded for the instance type
- Insufficient EBS volume capacity
- Subnet has no available IP addresses
- Security group rules block required traffic
- IAM instance profile does not exist or has wrong permissions

## How to Fix

### Check Instance Limits

```bash
aws service-quotas get-service-quota \
  --service-code ec2 \
  --quota-code L-1216C47A \
  --region us-east-1
```

### Check Subnet Available IPs

```bash
aws ec2 describe-subnets --subnet-ids subnet-xxx \
  --query 'Subnets[*].AvailableIpAddressCount'
```

### Verify Security Group

```bash
aws ec2 describe-security-groups --group-ids sg-xxx
```

### Check Instance Launch History

```bash
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=stopped"
```

## Examples

```bash
# Example 1: Instance limit
# InstanceLimitExceeded: You have exceeded your instances
# Fix: request limit increase

# Example 2: No available IPs
# InsufficientFreeAddressesInSubnet
# Fix: use a different subnet or increase CIDR range
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function error
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) — RDS connection error
