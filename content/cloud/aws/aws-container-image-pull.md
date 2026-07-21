---
title: "[Solution] AWS Container Image Pull"
description: "CannotPullContainerError."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Container Image Pull` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Image not in registry
- Registry URL wrong
- Credentials expired

## How to Fix

### Check image

```bash
aws ecr describe-images --repo my-repo
```

## Examples

- Example scenario: image not in registry
- Example scenario: registry url wrong
- Example scenario: credentials expired

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
