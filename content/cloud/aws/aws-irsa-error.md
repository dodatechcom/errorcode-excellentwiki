---
title: "[Solution] AWS IRSA Error"
description: "AccessDenied for IAM roles for SA."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IRSA Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- SA annotation missing
- Trust policy misconfigured

## How to Fix

### Check SA

```bash
kubectl describe serviceaccount my-sa -n default
```

## Examples

- Example scenario: sa annotation missing
- Example scenario: trust policy misconfigured

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
