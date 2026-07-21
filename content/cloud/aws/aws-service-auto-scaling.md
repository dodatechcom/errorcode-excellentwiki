---
title: "[Solution] AWS Service Auto Scaling"
description: "ServiceAutoScalingError."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Auto Scaling` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- IAM role misconfigured
- Min > max tasks

## How to Fix

### Describe targets

```bash
aws app-autoscaling describe-scalable-targets --service ecs
```

## Examples

- Example scenario: iam role misconfigured
- Example scenario: min > max tasks

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
