---
title: "[Solution] AWS ECS Service Not Stable"
description: "ServiceNotActiveException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ECS Service Not Stable` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Minimum healthy percent not met
- Task exec changes break tasks

## How to Fix

### Describe service

```bash
aws ecs describe-services --services my-service --cluster my-cluster
```

## Examples

- Example scenario: minimum healthy percent not met
- Example scenario: task exec changes break tasks

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
