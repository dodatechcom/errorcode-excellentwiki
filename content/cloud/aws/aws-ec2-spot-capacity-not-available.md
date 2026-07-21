---
title: "[Solution] AWS EC2 Spot Capacity Not Available"
description: "InsufficientSpotCapacity when spot capacity is unavailable."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Spot Capacity Not Available` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- All spot capacity pools for the requested instance type are exhausted
- The AZ does not have spot capacity
- Spot capacity is highly variable
- Too many instances requested at once

## How to Fix

### Try different AZs

```bash
aws ec2 request-spot-instances --spot-price 0.10 --instance-count 1 --type one-time --launch-specification file://spec.json
```
### Use instance diversification

```bash
aws ec2 describe-instance-type-offerings --location-type availability-zone --filters Name=instance-type,Values='m5.*' --output json
```
### Set up Capacity Blocks

```bash
aws ec2 describe-capacity-reservation-fleet-offerings --max-results 10
```

## Examples

- All 3 AZs in us-east-1 have zero m5.large spot capacity
- Spot capacity for p4d.24xlarge exhausted across all regions

## Related Errors

- [Spot Max Price]({{< relref "/cloud/aws/aws-ec2-spot-max-price" >}}) -- Spot pricing
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
