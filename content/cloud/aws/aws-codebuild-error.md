---
title: "[Solution] AWS CodeBuild Error — build/project/env/artifact failures"
description: "Fix AWS CodeBuild errors. Resolve build, project, environment, and artifact issues."
error-types: ["api-error"]
severities: ["error"]
weight: 152
---

An AWS CodeBuild error occurs when builds fail, projects cannot be created, or artifacts fail to upload. CodeBuild provides managed CI/CD but requires correct buildspec and environment configuration.

## Common Causes

- Buildspec.yml syntax errors or missing
- IAM role lacks S3 or ECR permissions
- Environment image not available in ECR
- Build timeout exceeded (default 60 minutes)
- VPC configuration blocks internet access

## How to Fix

### List Projects

```bash
aws codebuild list-projects \
  --query 'projects'
```

### Get Build Details

```bash
aws codebuild batch-get-builds \
  --ids build-xxx
```

### Start Build

```bash
aws codebuild start-build \
  --project-name my-project \
  --environment-variables-override name=ENV,value=production
```

### Create Project

```bash
aws codebuild create-project \
  --name my-build-project \
  --source type=CODECOMMIT,location=arn:aws:codecommit:us-east-1:123456789012:my-repo \
  --artifacts type=NO_ARTIFACTS \
  --environment type=LINUX_CONTAINER,computeType=BUILD_GENERAL1_MEDIUM,image=aws/codebuild/standard:7.0 \
  --service-role arn:aws:iam::123456789012:role/CodeBuildRole
```

### Get Build Logs

```bash
aws logs get-log-events \
  --log-group-name /aws/codebuild/my-project \
  --log-stream-name build-xxx
```

## Examples

```bash
# Example 1: Build failed
# BUILD_FAILED: Phase BUILD failed with exit code 1
# Fix: check buildspec.yml and application build errors

# Example 2: Artifact upload failed
# InvalidArtifactException: S3 access denied
# Fix: add s3:PutObject permission to CodeBuild role
```

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 artifact errors
- [AWS ECR Error]({{< relref "/cloud/aws/aws-ecr-error" >}}) — ECR container errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
