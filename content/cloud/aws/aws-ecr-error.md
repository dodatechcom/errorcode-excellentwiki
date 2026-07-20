---
title: "[Solution] AWS ECR Error — push/pull/auth failures"
description: "Fix AWS ECR errors. Resolve Elastic Container Registry push, pull, and authentication issues."
error-types: ["api-error"]
severities: ["error"]
weight: 101
---

An AWS ECR error occurs when you cannot push, pull, or authenticate with Elastic Container Registry. This can be due to expired tokens, IAM permissions, or repository configuration issues.

## Common Causes

- Expired or invalid ECR authorization token
- IAM policy does not grant ECR access
- Repository does not exist or wrong region
- Docker image tag already exists (immutable tag violation)
- Network connectivity issues to ECR endpoint

## How to Fix

### Get ECR Login Token

```bash
aws ecr get-login-password --region us-east-1 \
  --registry-ids 123456789012
```

### Create Repository

```bash
aws ecr create-repository \
  --repository-name my-app \
  --region us-east-1
```

### Check Repository Policy

```bash
aws ecr get-repository-policy \
  --repository-name my-app
```

### Push Image

```bash
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
docker tag my-app:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
```

### Set Repository Immutable Tags

```bash
aws ecr put-image-tag-mutability \
  --repository-name my-app \
  --image-tag-mutability IMMUTABLE
```

## Examples

```bash
# Example 1: Expired token
# no basic authentication credentials
# Fix: run aws ecr get-login-password

# Example 2: Image already exists
# ImageAlreadyExistsException
# Fix: use unique tags or set MUTABLE tag mutability
```

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) — ECS service errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS EKS Error]({{< relref "/cloud/aws/aws-eks-error" >}}) — EKS cluster errors
