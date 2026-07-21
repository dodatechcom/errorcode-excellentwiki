---
title: "[Solution] GCP Source Repositories Error -- repo push pull errors"
description: "Fix GCP Cloud Source Repositories errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 173
---

Cloud Source Repositories errors occur when there are issues with repository access, push/pull operations, or authentication.

## Common Causes
- Repository doesn't exist or access denied
- Git credentials not configured
- Push rejected due to permissions
- Repository size exceeds limits
- Source Repositories API not enabled

## How to Fix

### 1. Enable Source Repositories API
```bash
gcloud services enable sourcerepo.googleapis.com --project=PROJECT_ID
```

### 2. List repositories
```bash
gcloud repos list --project=PROJECT_ID
```

### 3. Create repository
```bash
gcloud repos create REPO_NAME --project=PROJECT_ID
```

### 4. Clone repository
```bash
gcloud repos clone REPO_NAME
```

### 5. Configure git credentials
```bash
git config --global credential.helper gcloud.sh
```

## Examples

### Create repo and push code
```bash
gcloud repos create my-app-repo
git init my-app
cd my-app
git remote add google https://source.developers.google.com/p/PROJECT/r/my-app-repo
echo "# My App" > README.md
git add .
git commit -m "Initial commit"
git push google master
```

### Set repository access
```bash
gcloud repos set-iam-policy REPO_NAME policy.yaml
```

## Related Errors
- [GCP Cloud Build Error](/cloud/gcp/gcp-cloud-build-error/)
- [GCP Cloud Shell Error](/cloud/gcp/gcp-cloud-shell-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)