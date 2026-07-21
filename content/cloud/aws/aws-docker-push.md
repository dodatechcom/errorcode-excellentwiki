---
title: "[Solution] AWS Docker push"
description: "Denied/DiskFull for Docker push."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Docker push` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Repo not exist
- Image size > 40GB
- Auth expired

## How to Fix

### Create repo

```bash
aws ecr create-repository --repo my-repo
```

## Examples

- Example scenario: repo not exist
- Example scenario: image size > 40gb
- Example scenario: auth expired

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
