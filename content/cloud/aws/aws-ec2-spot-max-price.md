---
title: "[Solution] AWS EC2 Spot Instance Max Price Error"
description: "SpotMaxPriceTooLow error when the specified max price is below the current spot price."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Spot Instance Max Price Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The bid price is lower than the current spot market price
- Spot price has risen above the configured max price
- The instance type has extremely high demand
- Max price was set too conservatively

## How to Fix

### Check current spot price

```bash
aws ec2 describe-spot-price-history --instance-types m5.large --product-descriptions Linux/UNIX --start-time $(date -u +%Y-%m-%dT%H:%M:%SZ) --output table
```
### Set higher max price

```bash
aws ec2 request-spot-instances --spot-price 0.15 --instance-count 1 --type one-time --launch-specification file://spec.json
```
### Use allocation strategy

```bash
aws ec2 request-spot-instances --spot-price 0.15 --type one-time --allocation-strategy lowest-price --launch-specification file://spec.json
```

## Examples

- Spot price for p3.2xlarge spiked to $3.50 but bid was $2.00
- m5.large spot price rose to $0.08 but bid was $0.05

## Related Errors

- [Spot Capacity]({{< relref "/cloud/aws/aws-ec2-spot-capacity" >}}) -- Spot capacity
- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
