---
title: "[Solution] AWS CodeCommit Error — repo/branch/push/pull failures"
description: "Fix AWS CodeCommit errors. Resolve repository, branch, push, and pull request issues."
error-types: ["api-error"]
severities: ["error"]
weight: 151
---

An AWS CodeCommit error occurs when repositories are inaccessible, pushes are rejected, or pull requests fail to create. CodeCommit provides managed Git hosting but requires proper credentials and branch permissions.

## Common Causes

- Git credentials expired or not configured
- Repository does not exist or was deleted
- Push to protected branch without approval
- IAM user lacks codecommit:* permissions
- Git clone URL format incorrect

## How to Fix

### List Repositories

```bash
aws codecommit list-repositories \
  --query 'repositories[*].{Name:repositoryName,ARN:repositoryArn}'
```

### Get Repository

```bash
aws codecommit get-repository \
  --repository-name my-repo
```

### List Branches

```bash
aws codecommit list-branches \
  --repository-name my-repo
```

### Create Repository

```bash
aws codecommit create-repository \
  --repository-name my-new-repo \
  --repository-description "My new repository"
```

### Get Clone URL

```bash
aws codecommit get-repository \
  --repository-name my-repo \
  --query 'repositoryMetadata.cloneUrlHttp'
```

## Examples

```bash
# Example 1: Access denied
# RepositoryDoesNotExistException: Repository not found
# Fix: verify repository name and region

# Example 2: Push rejected
# Push when not allowed: Cannot push to protected branch
# Fix: create pull request instead of direct push
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS CodeBuild Error]({{< relref "/cloud/aws/aws-codebuild-error" >}}) — CodeBuild errors
- [AWS CodePipeline Error]({{< relref "/cloud/aws/aws-codepipeline-error" >}}) — CodePipeline errors
