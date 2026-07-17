---
title: "AWS InstanceLimitExceeded / VpcLimitExceeded"
description: "InstanceLimitExceeded / VpcLimitExceeded — Fix AWS EC2 and VPC quota exceeded errors."
error-types: ["quota-error"]
severities: ["error"]
weight: 5
---

The `InstanceLimitExceeded` or `VpcLimitExceeded` error occurs when you try to create more EC2 instances or VPCs than your AWS account allows. Default limits are set per region and can be increased via a quota request.

## Common Causes

- The account has reached the default EC2 instance or VPC limit
- Previous instances are in `terminated` state but still count toward the limit
- VPC limit includes subnets, route tables, and internet gateways
- New AWS accounts have lower default quotas

## How to Fix

Check current EC2 instance limits:

```bash
aws service-quotas get-service-quota \
  --service-code ec2 \
  --quota-code L-0263D0A3 \
  --region us-east-1
```

Check VPC limits:

```bash
aws service-quotas get-service-quota \
  --service-code ec2 \
  --quota-code L-F678F1CE \
  --region us-east-1
```

Request a quota increase:

```bash
aws service-quotas request-service-quota-increase \
  --service-code ec2 \
  --quota-code L-0263D0A3 \
  --desired-value 200 \
  --region us-east-1
```

Clean up unused resources:

```bash
# List terminated instances (they still count)
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=terminated" \
  --query 'Reservations[].Instances[].InstanceId' \
  --output text

# Delete unused VPCs
aws ec2 describe-vpcs \
  --query 'Vpcs[?State==`available`].{VpcId:VpcId,Name:Tags[?Key==`Name`].Value|[0]}' \
  --output table
```

## Examples

- Auto Scaling group cannot launch new instances because the account limit of 5 instances is reached
- Creating a third VPC in an account with a default limit of 5 VPCs
- Terraform fails to create subnets because the VPC subnet limit is exhausted

## Related Errors

- [AWS Throttling]({{< relref "/cloud/aws/throttling" >}}) — API rate limiting.
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC configuration issues.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — GCP equivalent.
