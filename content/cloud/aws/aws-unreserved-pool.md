---
title: "[Solution] AWS Unreserved pool"
description: "UnreservedConcurrentExecutions limit hit."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Unreserved pool` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Reserved concurrency uses all capacity
- No unreserved slot available

## How to Fix

### Check account settings

```bash
aws lambda get-account-settings
```

## Examples

- Example scenario: reserved concurrency uses all capacity
- Example scenario: no unreserved slot available

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
