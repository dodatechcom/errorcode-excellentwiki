---
title: "[Solution] AWS EC2 Spot Capacity Not Available"
description: "SpotCapacityNotAvailable Spot request capacity exhausted."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Spot Capacity Not Available` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Temporarily high Spot usage in AZ
- Instance constraints
- Spot allocation strategy

## How to Fix

### Check Spot requests

```bash
aws ec2 describe-spot-instance-requests
```

### Use capacity-optimized

```bash
aws ec2 request-spot-instances --type persistent --strategy capacity-optimized
```

## Examples

- Example scenario: temporarily high spot usage in az
- Example scenario: instance constraints
- Example scenario: spot allocation strategy

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
