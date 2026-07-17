---
title: "[Solution] AWS ECS Task Failed to Start"
description: "Fix AWS ECS task failed errors. Resolve ECS task provisioning issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS ECS task failed to start error occurs when ECS cannot launch or run tasks in a cluster. This can be caused by resource, permission, or configuration issues.

## Common Causes

- Task execution role lacks required permissions
- Container image cannot be pulled from ECR
- Resource limits (CPU/memory) exceed container instance capacity
- Port mappings conflict with existing tasks
- Health check failures cause task replacement

## How to Fix

### Check Task Status

```bash
aws ecs describe-tasks \
  --cluster my-cluster \
  --tasks arn:aws:ecs:us-east-1:123456789:task/my-cluster/abc123
```

### Check Task Definition

```bash
aws ecs describe-task-definition --task-definition my-task:1
```

### Verify Execution Role

```bash
aws iam get-role --role-name ecsTaskExecutionRole
```

### Check Service Events

```bash
aws ecs describe-services \
  --cluster my-cluster \
  --services my-service
```

### Pull Image Manually

```bash
aws ecr get-login-password | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
docker pull 123456789.dkr.ecr.us-east-1.amazonaws.com/my-image:latest
```

## Examples

```bash
# Example 1: Image pull failure
# CannotPullContainerError: pull access denied
# Fix: verify ECR image and execution role

# Example 2: Resource limits
# Resource: ContainerInstance has insufficient resources
# Fix: add more container instances or reduce task resources
```

## Related Errors

- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error" >}}) — EKS cluster error
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function error
