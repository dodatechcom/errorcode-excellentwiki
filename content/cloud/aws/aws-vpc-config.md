---
title: "[Solution] AWS VPC Config"
description: "InvalidParameterValue for VPC config."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPC Config` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- VPC deleted or non-existent
- Subnet belongs to wrong AZ
- SG in the wrong VPC

## How to Fix

### Check VPC config

```bash
aws lambda get-function-config --function my-function
```

### Update VPC

```bash
aws lambda update-function-config --function my-function --vpc SubnetIds=s1,s2,SecurityIds=sg-1
```

## Examples

- Example scenario: vpc deleted or non-existent
- Example scenario: subnet belongs to wrong az
- Example scenario: sg in the wrong vpc

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
