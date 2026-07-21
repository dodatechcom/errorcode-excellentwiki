---
title: "[Solution] AWS Placement Group"
description: "PlacementGroupError constraints cannot be met."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Placement Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Capacity insufficient in the group
- Spread limit reached
- Single AZ groups only

## How to Fix

### Describe group

```bash
aws ec2 describe-placement-groups --names my-pg
```

## Examples

- Example scenario: capacity insufficient in the group
- Example scenario: spread limit reached
- Example scenario: single az groups only

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General ec2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
