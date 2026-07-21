---
title: "[Solution] AWS Fargate Profile (EKS)"
description: "InvalidParameterException for fargate profile."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Fargate Profile (EKS)` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Selector doesn't match pods
- IAM role missing

## How to Fix

### List profiles

```bash
aws eks list-fargate-profiles --cluster my-cluster
```

## Examples

- Example scenario: selector doesn't match pods
- Example scenario: iam role missing

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
