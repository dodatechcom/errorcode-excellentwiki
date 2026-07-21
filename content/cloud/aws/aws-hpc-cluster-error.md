---
title: "[Solution] AWS HPC Cluster Error"
description: "HPCClusterError for High Performance Computing."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `HPC Cluster Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- EFA attachment limit exceeded
- Slurm node failure
- EFA security rules misconfigured

## How to Fix

### Check EFA

```bash
aws ec2 describe-network-interfaces --filter description,EFA-*
```

### Verify EFA status

```bash
aws ec2 describe-instance-types --p4d.24xlarge --query NetworkInfo
```

## Examples

- Example scenario: efa attachment limit exceeded
- Example scenario: slurm node failure
- Example scenario: efa security rules misconfigured

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
