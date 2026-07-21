---
title: "[Solution] AWS ELB Target Group"
description: "InvalidTargetException for ELB."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ELB Target Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Target group not exist
- Health check fails

## How to Fix

### List target groups

```bash
aws elbv2 describe-target-groups
```

## Examples

- Example scenario: target group not exist
- Example scenario: health check fails

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
