---
title: "[Solution] AWS ECS Cluster Not Found"
description: "ClusterNotFoundException for ECS."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ECS Cluster Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Cluster name incorrect
- Cluster deleted
- Region mismatch

## How to Fix

### List clusters

```bash
aws ecs list-clusters
```

## Examples

- Example scenario: cluster name incorrect
- Example scenario: cluster deleted
- Example scenario: region mismatch

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ecs errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
