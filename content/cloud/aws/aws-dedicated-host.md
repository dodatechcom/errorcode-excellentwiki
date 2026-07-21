---
title: "[Solution] AWS Dedicated Host"
description: "DedicatedHostError when allocation fails."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dedicated Host` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Host limit per region reached
- Insufficient capacity for instance
- Host in wrong state

## How to Fix

### Check hosts

```bash
aws ec2 describe-hosts
```

### Allocate host

```bash
aws ec2 allocate-hosts --quantity 1 --az us-east-1a --instance c5.xlarge
```

## Examples

- Example scenario: host limit per region reached
- Example scenario: insufficient capacity for instance
- Example scenario: host in wrong state

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
