---
title: "[Solution] AWS EKS Node Group"
description: "ResourceNotFoundException for node groups."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EKS Node Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Node group not in cluster
- Node group in DELETE state

## How to Fix

### List node groups

```bash
aws eks list-nodegroups --cluster my-cluster
```

## Examples

- Example scenario: node group not in cluster
- Example scenario: node group in delete state

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
