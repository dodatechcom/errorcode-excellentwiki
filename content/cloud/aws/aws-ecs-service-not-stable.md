---
title: "[Solution] AWS ECS Service Not Stable"
description: "ServiceNotStableException when ECS service is not in stable state."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ECS Service Not Stable` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Service is still being deployed
- Task count cannot be reached
- Deployment failed
- Auto scaling is in progress

## How to Fix

### Check service

```bash
aws ecs describe-services --cluster my-cluster --services my-service --query "services[*].{Status:status,Count:desiredCount,Running:runningCount}" --output table
```
### Wait for stable

```bash
aws ecs wait services-stable --cluster my-cluster --services my-service
```
### Update service

```bash
aws ecs update-service --cluster my-cluster --service my-service --desired-count 3
```

## Examples

- Service desired count is 5 but only 3 tasks running
- Deployment failed due to insufficient capacity

## Related Errors

- [ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) -- General ECS errors
- [Task Definition]({{< relref "/cloud/aws/aws-ecs-task-definition" >}}) -- Task definition
