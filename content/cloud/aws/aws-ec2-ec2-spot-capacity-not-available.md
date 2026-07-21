---
title: "[Solution] AWS EC2 Spot Capacity Not Available"
description: "SpotCapacityNotAvailable when Spot Instance capacity is temporarily exhausted."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Spot Capacity Not Available` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Temporarily high Spot Instance usage in the AZ
- Instance type-specific capacity constraints
- Region-level Spot capacity exhaustion
- Launch specification compatibility issues
- Spot allocation strategy misfit

## How to Fix

### Check Spot requests

```bash
aws ec2 describe-spot-instance-requests
```

### Use capacity-optimized strategy

```bash
aws ec2 request-spot-instances --instance-count 2 --type persistent --strategy capacity-optimized
```

### Specify multiple AZs

```bash
aws ec2 request-spot-instances --launch-specification file://launch-spec.json
```

### Try capacity-optimized-prioritized

```bash
aws ec2 request-spot-instances --instance-count 3 --strategy capacity-optimized-prioritized
```

### Fall back to On-Demand

```bash
aws ec2 run-instances --image-id ami-0abcdef --instance-type c5.xlarge --count 1
```

## Examples

- Example scenario: temporarily high spot instance usage in the az
- Example scenario: instance type-specific capacity constraints
- Example scenario: region-level spot capacity exhaustion
- Example scenario: launch specification compatibility issues

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
