---
title: "[Solution] AWS EC2 Insufficient Capacity"
description: "InsufficientInstanceCapacity error when AWS cannot fulfill the instance launch request."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Insufficient Capacity` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The selected Availability Zone does not have enough capacity
- Demand is higher than available capacity in the AZ
- Requesting a large number of instances simultaneously
- Specific instance types with limited capacity

## How to Fix

### Try a different AZ

```bash
aws ec2 run-instances --instance-type m5.large --availability-zone us-east-1b --image-id ami-0abcdef12
```
### Use Capacity Reservations

```bash
aws ec2 create-capacity-reservation --instance-type m5.large --availability-zone us-east-1a --instance-count 10
```
### Try a different instance type

```bash
aws ec2 describe-instance-type-offerings --location-type availability-zone --filters Name=instance-type,Values=m5.* --output table
```
### Use Spot Instances

```bash
aws ec2 request-spot-instances --spot-price 0.05 --instance-count 2 --type one-time --launch-specification file://spec.json
```

## Examples

- Launching 100 x m5.24xlarge in a single AZ fails
- GPU instance p4d.24xlarge not available in us-west-2b

## Related Errors

- [EC2 Instance Limit]({{< relref "/cloud/aws/ec2-instance-limit" >}}) -- Instance limits
- [Spot Instance Error]({{< relref "/cloud/aws/aws-ec2-spot-error" >}}) -- Spot instances
