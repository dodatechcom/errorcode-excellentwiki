---
title: "[Solution] AWS VPC Limit Exceeded"
description: "VpcLimitExceeded when the account VPC limit has been reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPC Limit Exceeded` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Default VPC limit of 5 VPCs per region reached
- VPC limit is per-region quota
- Stacked VPCs from long-running projects
- Non-default VPCs not being cleaned up
- Organization-level VPC count restrictions

## How to Fix

### Check VPC count

```bash
aws ec2 describe-vpcs --region us-east-1
```

### Delete unused VPCs

```bash
aws ec2 delete-vpc --vpc-id vpc-0abc123
```

### Request VPC quota increase

```bash
aws service-quotas request-service-quota-increase --service-code vpc --quota-code L-F678F1CE --desired-value 10
```

### Check VPC quota

```bash
aws service-quotas get-service-quota --service-code vpc --quota-code L-F678F1CE
```

## Examples

- Example scenario: default vpc limit of 5 vpcs per region reached
- Example scenario: vpc limit is per-region quota
- Example scenario: stacked vpcs from long-running projects
- Example scenario: non-default vpcs not being cleaned up

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
