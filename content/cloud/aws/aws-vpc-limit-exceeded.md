---
title: "[Solution] AWS VPC Limit Exceeded"
description: "VpcLimitExceeded when the account VPC limit reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPC Limit Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Default 5 VPCs per region exhausted
- Stacked from many projects

## How to Fix

### Count VPCs

```bash
aws ec2 describe-vpcs --query length(Vpcs)
```

### Delete unused

```bash
aws ec2 delete-vpc --vpc vpc-0abc
```

## Examples

- Example scenario: default 5 vpcs per region exhausted
- Example scenario: stacked from many projects

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
