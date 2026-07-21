---
title: "[Solution] AWS ECR Auth"
description: "AccessDenied for ECR."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ECR Auth` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Login expired
- IAM user no permissions

## How to Fix

### Get login

```bash
aws ecr get-login-password --region us-east-1
```

## Examples

- Example scenario: login expired
- Example scenario: iam user no permissions

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
