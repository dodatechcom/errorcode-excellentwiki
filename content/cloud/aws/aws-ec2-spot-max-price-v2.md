---
title: "[Solution] AWS EC2 Spot Max Price"
description: "SpotMaxPriceTooLow when the bid is below the Spot market price."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Spot Max Price` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Spot price exceeds the max bid
- Market demand increased pricing
- Instance type high demand on Spot

## How to Fix

### Check Spot price history

```bash
aws ec2 describe-spot-price-history --instance-type c5.xlarge -s 2025-01-01T00:00:00Z
```

### Higher max price

```bash
aws ec2 request-spot-instances --spot-price 0.50 --count 1
```

### Fall back to On-Demand

```bash
aws ec2 run-instances --image-id ami-0abcdef --count 1
```

## Examples

- Example scenario: spot price exceeds the max bid
- Example scenario: market demand increased pricing
- Example scenario: instance type high demand on spot

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
