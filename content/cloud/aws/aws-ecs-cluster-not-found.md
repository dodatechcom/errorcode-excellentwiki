---
title: "[Solution] AWS ECS Cluster Not Found"
description: "ClusterNotFoundException when the specified ECS cluster does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ECS Cluster Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Cluster name is incorrect
- Cluster was deleted
- Cluster in different region
- IAM role lacks ecs:DescribeClusters permission

## How to Fix

### List clusters

```bash
aws ecs list-clusters
```
### Describe cluster

```bash
aws ecs describe-clusters --clusters my-cluster
```
### Create cluster

```bash
aws ecs create-cluster --cluster-name my-cluster
```

## Examples

- Cluster my-cluster not found (check name)
- Cluster deleted but service still references it

## Related Errors

- [ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ECS errors
- [Service Not Stable]({{< relref "/cloud/aws/aws-ecs-service-not-stable" >}}) -- Service stability
