---
title: "[Solution] AWS CodeCatalyst Error — project/dev-env/pipeline failures"
description: "Fix AWS CodeCatalyst errors. Resolve project, dev environment, and pipeline issues."
error-types: ["api-error"]
severities: ["error"]
weight: 157
---

An AWS CodeCatalyst error occurs when projects fail to create, dev environments cannot start, or Blueprints encounter errors. CodeCatalyst provides integrated DevOps but requires proper project and environment configuration.

## Common Causes

- Dev environment instance type not available
- Source repository connection to GitHub fails
- Pipeline action configuration invalid
- IAM user does not have CodeCatalyst access
- Project space storage quota exceeded

## How to Fix

### List Spaces

```bash
aws codecatalyst list-spaces \
  --query 'items[*].{Name:name,ARN:arn}'
```

### List Projects

```bash
aws codecatalyst list-projects \
  --space-name my-space \
  --query 'items[*].{Name:name,DisplayName:displayName}'
```

### Create Dev Environment

```bash
aws codecatalyst create-dev-environment \
  --space-name my-space \
  --project-name my-project \
  --idempotency-token unique-token-123
```

### Get Dev Environment

```bash
aws codecatalyst get-dev-environment \
  --space-name my-space \
  --project-name my-project \
  --id dev-env-xxx
```

### List Source Repositories

```bash
aws codecatalyst list-source-repositories \
  --space-name my-space \
  --project-name my-project
```

## Examples

```bash
# Example 1: Dev environment failed
# ServiceQuotaExceededException: Instance limit reached
# Fix: stop unused dev environments or request increase

# Example 2: Source connection failed
# ValidationException: GitHub token invalid
# Fix: regenerate GitHub personal access token
```

## Related Errors

- [AWS CodeBuild Error]({{< relref "/cloud/aws/aws-codebuild-error" >}}) — CodeBuild errors
- [AWS CodePipeline Error]({{< relref "/cloud/aws/aws-codepipeline-error" >}}) — CodePipeline errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
