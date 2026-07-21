---
title: "[Solution] GCP Dataform Error -- repository workflow compilation errors"
description: "Fix GCP Dataform errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 133
---

Dataform errors occur when there are issues with repository management, workflow compilation, or SQLX execution.

## Common Causes
- Repository branch not configured
- Workflow compilation fails due to SQL syntax
- Dataform API not enabled
- Secret manager reference invalid
- Workspace conflicts with published files

## How to Fix

### 1. Enable Dataform API
```bash
gcloud services enable dataform.googleapis.com --project=PROJECT_ID
```

### 2. List repositories
```bash
gcloud dataform repositories list --location=REGION
```

### 3. Create repository
```bash
gcloud dataform repositories create REPO_NAME \
  --location=REGION \
  --default-branch=main
```

### 4. Create workflow release
```bash
gcloud dataform repositories releases create RELEASE_NAME \
  --repository=REPO_NAME \
  --location=REGION \
  --target=refs/heads/main \
  --code-compile-config-warn-if-compiled-dataforms-diff-enabled
```

### 5. List workflow configs
```bash
gcloud dataform repositories workflow-configs list \
  --repository=REPO_NAME \
  --location=REGION
```

## Examples

### Create workspace for development
```bash
gcloud dataform repositories workspaces create dev-workspace \
  --repository=my-repo \
  --location=us-central1 \
  --branch=dev-branch
```

### Describe repository
```bash
gcloud dataform repositories describe my-repo \
  --location=us-central1 \
  --format="yaml(name,defaultBranch,workspaceCompilationOverrides)"
```

## Related Errors
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP Secret Manager Error](/cloud/gcp/gcp-secret-manager-error/)
- [GCP Cloud Build Error](/cloud/gcp/gcp-cloud-build-error/)