---
title: "[Solution] AWS Fargate Spot"
description: "FargateSpotCapacityUnavailable."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Fargate Spot` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Spot exhausted in region
- Platform version not supported

## How to Fix

### Use On-Demand

```bash
aws ecs run-task --launch FARGATE --cluster my-cluster
```

## Examples

- Example scenario: spot exhausted in region
- Example scenario: platform version not supported

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
