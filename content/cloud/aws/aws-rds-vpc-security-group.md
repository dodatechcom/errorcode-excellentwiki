---
title: "[Solution] AWS RDS VPC Security Group"
description: "AuthorizationNotFound for VPC SGs."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `RDS VPC Security Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Wrong VPC
- Region mismatch
- Inbound rule missing

## How to Fix

### Check rules

```bash
aws ec2 describe-security-groups --group-ids sg-abc --query IpPermissions
```

## Examples

- Example scenario: wrong vpc
- Example scenario: region mismatch
- Example scenario: inbound rule missing

## Related Errors

- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error" >}}) -- General rds errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
