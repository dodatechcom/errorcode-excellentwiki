---
title: "[Solution] AWS Elastic IP Limit Exceeded"
description: "ElasticIpLimitExceeded when the account EIP quota is reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Elastic IP Limit Exceeded` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Account Elastic IP quota exhausted
- Too many EIPs allocated across all regions
- EIPs not associated with running instances
- EC2-Classic Platform EIP limit restrictions
- Non-standard region EIP quota applies

## How to Fix

### Check current EIP usage

```bash
aws ec2 describe-addresses --region us-east-1
```

### Release unused EIPs

```bash
aws ec2 release-address --allocation-id eipalloc-0abc123
```

### Request quota increase

```bash
aws service-quotas request-service-quota-increase --service-code ec2 --quota-code L-0263D0A3 --desired-value 10
```

### Check quotas

```bash
aws service-quotas get-service-quota --service-code ec2 --quota-code L-0263D0A3
```

## Examples

- Example scenario: account elastic ip quota exhausted
- Example scenario: too many eips allocated across all regions
- Example scenario: eips not associated with running instances
- Example scenario: ec2-classic platform eip limit restrictions

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
