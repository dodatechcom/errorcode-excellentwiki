---
title: "[Solution] Terraform VPC Limit Exceeded"
description: "Fix Terraform VPC limit exceeded errors when the account VPC quota is reached."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

VPC limit exceeded errors occur when you hit the account VPC quota:

```
Error: Error creating VPC: VpcLimitExceeded

The maximum number of VPCs has been reached.
```

## Common Causes

- Account VPC limit reached.
- Old VPCs not cleaned up.

## How to Fix

**Check current VPC count:**

```bash
aws ec2 describe-vpcs --query 'Vpcs[*].{ID:VpcId,Name:Tags[?Key==`Name`].Value|[0]}' --output table
```

**Request a quota increase:**

```bash
aws service-quotas request-service-quota-increase   --service-code ec2   --quota-code L-0263D0A6   --desired-value 10
```

**Clean up unused VPCs:**

```bash
aws ec2 describe-vpcs --query 'Vpcs[*].VpcId' --output text
terraform destroy -target=aws_vpc.unused
```

## Examples

```bash
aws service-quotas get-service-quota --service-code ec2 --quota-code L-0263D0A6
```
