---
title: "[Solution] AWS Cloud9 Error — IDE environment/instance/port failures"
description: "Fix AWS Cloud9 errors. Resolve IDE environment, EC2 instance, and connection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 156
---

An AWS Cloud9 error occurs when environments fail to create, EC2 instances cannot be reached, or port forwarding breaks. Cloud9 provides cloud-based IDE but requires proper EC2 and networking configuration.

## Common Causes

- EC2 instance type no longer available
- Subnet has no internet connectivity
- IAM role lacks EC2 or SSM permissions
- Instance storage space exhausted
- VPC endpoint blocks Cloud9 traffic

## How to Fix

### List Environments

```bash
aws cloud9 list-environments \
  --query 'environmentIds'
```

### Describe Environment

```bash
aws cloud9 describe-environment-memberships \
  --environment-id env-xxx \
  --query 'memberships[*].{User:userId,Permission:permissions}'
```

### Create Environment

```bash
aws cloud9 create-environment-ec2 \
  --name my-ide \
  --instance-type t3.small \
  --subnet-id subnet-xxx \
  --description "My Cloud9 environment"
```

### Stop Environment

```bash
aws cloud9 stop-environment \
  --environment-id env-xxx
```

### Delete Environment

```bash
aws cloud9 delete-environment \
  --environment-id env-xxx
```

## Examples

```bash
# Example 1: Environment creation failed
# BadRequestException: Instance type not available
# Fix: try different instance type or region

# Example 2: Cannot connect
# Connection timed out to Cloud9 instance
# Fix: verify VPC has internet access via NAT gateway
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
