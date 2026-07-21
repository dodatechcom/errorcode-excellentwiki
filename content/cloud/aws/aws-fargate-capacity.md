---
title: "[Solution] AWS Fargate Capacity"
description: "FargateCapacityExhaustion."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Fargate Capacity` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Regional capacity limit hit
- Spot exhausted

## How to Fix

### Check Fargate usage

```bash
aws service-quotas get-service-quota --service-code fargate --quota-code L-2FA1B95F
```

## Examples

- Example scenario: regional capacity limit hit
- Example scenario: spot exhausted

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
