---
title: "[Solution] AWS Fargate Error — resource/timeout/startup failures"
description: "Fix AWS Fargate errors. Resolve Fargate task resource, timeout, and startup issues."
error-types: ["api-error"]
severities: ["error"]
weight: 102
---

An AWS Fargate error occurs when a Fargate task cannot start, runs out of resources, or times out during execution. This is often due to CPU/memory limits, networking issues, or IAM misconfiguration.

## Common Causes

- Task CPU or memory exceeds Fargate limits
- ENI (Elastic Network Interface) limit reached
- IAM task role lacks required permissions
- Container image pull failures or timeouts
- Service discovery or load balancer misconfiguration

## How to Fix

### Check Task Definition

```bash
aws ecs describe-task-definition \
  --task-definition my-task:1
```

### Check Running Tasks

```bash
aws ecs list-tasks \
  --cluster my-cluster \
  --service-name my-service \
  --desired-status RUNNING
```

### Check Task Failures

```bash
aws ecs describe-tasks \
  --cluster my-cluster \
  --tasks arn:aws:ecs:us-east-1:123456789012:task/my-cluster/abc123
```

### Check ENI Limits

```bash
aws ec2 describe-network-interfaces \
  --filters "Name=vpc-id,Values=vpc-xxx" \
  --query 'NetworkInterfaces[*].Status'
```

### Update Task with More Resources

```bash
aws ecs register-task-definition \
  --family my-task \
  --requires-compatibilities FARGATE \
  --cpu 1024 \
  --memory 2048 \
  --network-mode awsvpc
```

## Examples

```bash
# Example 1: Resource not found
# ResourceNotFoundException: Tasks in cluster my-cluster not found
# Fix: verify cluster name and task ARN

# Example 2: ENI limit
# CannotPullContainerError: network interface limit
# Fix: increase ENI limits or reduce tasks per AZ
```

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) — ECS service errors
- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error" >}}) — EKS cluster errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
