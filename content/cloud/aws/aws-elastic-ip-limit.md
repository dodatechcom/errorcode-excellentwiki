---
title: "[Solution] AWS Elastic IP Limit"
description: "ElasticIpLimitExceeded when EIP quota reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Elastic IP Limit` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Account EIP quota exhausted
- Unassociated EIPs wasting limit

## How to Fix

### Check usage

```bash
aws ec2 describe-addresses
```

### Release unused

```bash
aws ec2 release-address --allocation-id eipalloc-0abc
```

## Examples

- Example scenario: account eip quota exhausted
- Example scenario: unassociated eips wasting limit

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
