---
title: "[Solution] AWS EC2 Spot Instance Max Price"
description: "SpotMaxPriceTooLow when the bid price is below the Spot market price."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Spot Instance Max Price` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Spot price exceeds your maximum bid price
- Market demand increased Spot Instance pricing
- Instance type is in high demand on Spot market
- Region-specific Spot pricing dynamics
- Interruption threshold set too low

## How to Fix

### Check Spot price history

```bash
aws ec2 describe-spot-price-history --instance-type c5.xlarge --start-time 2025-01-01T00:00:00Z
```

### Request with higher max price

```bash
aws ec2 request-spot-instances --spot-price 0.50 --instance-count 1 --type one-time
```

### Use less popular instance type

```bash
aws ec2 describe-spot-price-history --instance-type t3.medium --start-time 2025-01-01T00:00:00Z
```

### Enable Capacity Rebalancing

```bash
aws ec2 request-spot-instances --spot-price 0.30 --instance-interruption-behavior stop
```

### Fall back to On-Demand

```bash
aws ec2 run-instances --image-id ami-0abcdef --instance-type c5.xlarge --count 1
```

## Examples

- Example scenario: spot price exceeds your maximum bid price
- Example scenario: market demand increased spot instance pricing
- Example scenario: instance type is in high demand on spot market
- Example scenario: region-specific spot pricing dynamics

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
