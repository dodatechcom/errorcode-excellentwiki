---
title: "[Solution] AWS kubeconfig Error"
description: "AccessDenied for kubeconfig."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `kubeconfig Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Not configured for this cluster
- Role not authorized

## How to Fix

### Update kubeconfig

```bash
aws eks update-kubeconfig --region us-east-1 --name my-cluster
```

## Examples

- Example scenario: not configured for this cluster
- Example scenario: role not authorized

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
