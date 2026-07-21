---
title: "[Solution] AWS Lambda VPC Config Error"
description: "InvalidParameterValueException for VPC configuration in Lambda."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda VPC Config Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- VPC ID references a deleted or non-existent VPC
- Subnet ID belongs to a different AZ than intended
- Security group belongs to wrong VPC
- Too many VPC subnets specified (max 16)
- Both subnets in same AZ when High Availability needed

## How to Fix

### Check VPC config

```bash
aws lambda get-function-configuration --function-name my-function
```

### Update VPC config

```bash
aws lambda update-function-configuration --function-name my-function --vpc-config SubnetIds=subnet-abc,subnet-def,SecurityGroupIds=sg-123
```

## Examples

- Example scenario: vpc id references a deleted or non-existent vpc
- Example scenario: subnet id belongs to a different az than intended
- Example scenario: security group belongs to wrong vpc
- Example scenario: too many vpc subnets specified (max 16)

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
