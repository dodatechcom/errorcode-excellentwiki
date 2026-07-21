---
title: "[Solution] AWS EC2 Placement Group Error"
description: "PlacementGroupLimitExceeded or InvalidPlacementGroup."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Placement Group Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Maximum placement groups per account reached
- Launch in group from different AZ
- Cluster group spans incompatible instance types
- Partition group has too many partitions

## How to Fix

### List placement groups

```bash
aws ec2 describe-placement-groups --query 'PlacementGroups[*].[GroupName,State,Strategy]' --output table
```
### Create placement group

```bash
aws ec2 create-placement-group --group-name my-cluster --strategy cluster --region us-east-1a
```
### Delete placement group

```bash
aws ec2 delete-placement-group --group-name my-cluster
```

## Examples

- Spread group with more than 7 AZs
- Cluster group with 10 instances but only 5 fit per rack

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Instance Limit]({{< relref "/cloud/aws/aws-ec2-instance-limit-exceeded" >}}) -- Instance limits
