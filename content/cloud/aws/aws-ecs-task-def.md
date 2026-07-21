---
title: "[Solution] AWS ECS Task Def"
description: "InvalidParameterException for task def."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ECS Task Def` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Container image not exist
- Env vars > 4KB

## How to Fix

### List task defs

```bash
aws ecs list-task-definitions
```

## Examples

- Example scenario: container image not exist
- Example scenario: env vars > 4kb

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
