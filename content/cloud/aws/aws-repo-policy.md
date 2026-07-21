---
title: "[Solution] AWS Repo Policy"
description: "InvalidParameterException for ECR policy."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Repo Policy` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Policy > 20 KB
- Syntax invalid

## How to Fix

### Get repo policy

```bash
aws ecr get-repository-policy --repo my-repo
```

## Examples

- Example scenario: policy > 20 kb
- Example scenario: syntax invalid

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
