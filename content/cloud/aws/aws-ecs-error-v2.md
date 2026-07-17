---
title: "[Solution] AWS ECS — CannotPullContainerError"
description: "Fix AWS ECS CannotPullContainerError. Resolve ECS container image pull failures."
cloud: ["aws"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["aws", "ecs", "cannot-pull", "container", "image", "pull", "ecr"]
weight: 5
---

A CannotPullContainerError means the ECS agent on the container instance cannot pull the specified container image from the registry. The task remains in PENDING state and never starts.

## What This Error Means

ECS tasks require container images to be available before the Docker/CRI-O runtime can start the container. The ECS agent attempts to pull the image from ECR or a public registry. If the pull fails — due to authentication issues, missing images, network problems, or registry errors — the task fails with `CannotPullContainerError`. This is an infrastructure-level failure, not an application error.

## Common Causes

- ECR authentication token expired (tokens last 12 hours)
- Image does not exist in the specified ECR repository
- IAM role on the EC2 instance lacks ECR pull permissions
- Network connectivity issue between instance and ECR
- Image tag does not match any available image
- ECR repository is in a different region than the ECS cluster
- Docker daemon is unresponsive on the container instance

## How to Fix

### Check Task Status

```bash
aws ecs describe-tasks \
  --cluster my-cluster \
  --tasks arn:aws:ecs:us-east-1:123456789012:task/my-cluster/xxx
```

### Check Container Instance

```bash
aws ecs describe-container-instances \
  --cluster my-cluster \
  --container-instances arn:aws:ecs:us-east-1:123456789012:container-instance/xxx
```

### Verify ECR Image Exists

```bash
aws ecr describe-images \
  --repository-name my-app \
  --image-ids imageTag=latest
```

### Get ECR Login Token

```bash
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
```

### Check Instance IAM Role

```bash
aws iam list-instance-profiles-for-role \
  --role-name ecsInstanceRole
```

### Add ECR Permissions

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "ecr:GetAuthorizationToken",
      "ecr:BatchCheckLayerAvailability",
      "ecr:GetDownloadUrlForLayer",
      "ecr:BatchGetImage"
    ],
    "Resource": "*"
  }]
}
```

### Test Image Pull

```bash
# On the ECS instance
docker pull 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
```

## Related Errors

- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error-v2" >}}) — EKS health check failed
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error-v2" >}}) — Lambda runtime error
- [Kubernetes ImagePullBackOff]({{< relref "/tools/kubernetes/k8s-image-pull-v2" >}}) — image pull failed
