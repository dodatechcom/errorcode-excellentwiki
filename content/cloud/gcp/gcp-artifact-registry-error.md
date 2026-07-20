---
title: "[Solution] GCP Artifact Registry Error — repo docker auth cleanup errors"
description: "Fix GCP Artifact Registry errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 117
---

Artifact Registry errors occur when there are issues with repository creation, Docker authentication, or artifact cleanup policies.

## Common Causes
- Repository type mismatch with artifact format
- Docker authentication not configured
- Cleanup policy deleting required artifacts
- IAM permissions insufficient for repository access
- Artifact Registry API not enabled

## How to Fix

### 1. Enable Artifact Registry API
```bash
gcloud services enable artifactregistry.googleapis.com --project=PROJECT_ID
```

### 2. List repositories
```bash
gcloud artifacts repositories list --location=REGION
```

### 3. Create Docker repository
```bash
gcloud artifacts repositories create REPO_NAME \
  --repository-format=docker \
  --location=REGION \
  --description="Docker repository"
```

### 4. Configure Docker authentication
```bash
gcloud auth configure-docker REGION-docker.pkg.dev
```

### 5. Set cleanup policy
```bash
gcloud artifacts repositories update REPO_NAME \
  --location=REGION \
  --cleanup-policy-dry-run=false \
  --cleanup-policy-keep=3 \
  --cleanup-policy-untagged-delete
```

## Examples

### Push Docker image to Artifact Registry
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev

docker build -t us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/my-app:v1 .
docker push us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/my-app:v1
```

### Create Maven repository
```bash
gcloud artifacts repositories create maven-repo \
  --repository-format=maven \
  --location=us-central1 \
  --description="Java artifacts"
```

## Related Errors
- [GCP Cloud Build Error](/cloud/gcp/gcp-cloud-build-error/)
- [GCP GKE Error](/cloud/gcp/gcp-gke-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)