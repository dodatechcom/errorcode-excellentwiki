---
title: "[Solution] AWS CodeArtifact Error — domain/repo/auth failures"
description: "Fix AWS CodeArtifact errors. Resolve domain, repository, and authentication issues."
error-types: ["api-error"]
severities: ["error"]
weight: 155
---

An AWS CodeArtifact error occurs when domains cannot be created, repositories fail to publish packages, or authentication tokens expire. CodeArtifact provides managed artifact repositories for package management.

## Common Causes

- Domain name already taken across all AWS accounts
- Repository upstream connection fails
- Authentication token expired (default 12 hours)
- Package name conflicts with public repository
- IAM user lacks codeartifact:* permissions

## How to Fix

### List Domains

```bash
aws codeartifact list-domains \
  --query 'domains[*].{Name:name,ARN:arn,Status:status}'
```

### Get Authorization Token

```bash
aws codeartifact get-authorization-token \
  --domain my-domain \
  --duration-seconds 3600
```

### Create Repository

```bash
aws codeartifact create-repository \
  --domain my-domain \
  --repository-name my-repo \
  --description "My package repository"
```

### Publish Package

```bash
aws codeartifact publish-package-version \
  --domain my-domain \
  --repository my-repo \
  --format npm \
  --package my-package \
  --package-version 1.0.0
```

### List Packages

```bash
aws codeartifact list-packages \
  --domain my-domain \
  --repository my-repo
```

## Examples

```bash
# Example 1: Domain name conflict
# ValidationException: Domain name already exists
# Fix: choose a different domain name (globally unique)

# Example 2: Auth token expired
# UnauthorizedException: Authorization token expired
# Fix: run get-authorization-token to refresh
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 artifact errors
- [AWS CodeBuild Error]({{< relref "/cloud/aws/aws-codebuild-error" >}}) — CodeBuild errors
