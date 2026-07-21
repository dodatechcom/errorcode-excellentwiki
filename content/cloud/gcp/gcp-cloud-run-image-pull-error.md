---
title: "[Solution] GCP Cloud Run Image Pull Error"
description: "Fix Cloud Run image pull errors. Resolve container image access, Artifact Registry, and image permission issues in Google Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Image Pull Error

The Cloud Run Image Pull error occurs when Cloud Run cannot pull the container image from the registry due to access or configuration issues.

## Common Causes

- Container image does not exist in the specified registry
- Service account lacks Artifact Registry Reader permission
- Image tag does not match the deployed version
- Artifact Registry is in a different region than Cloud Run
- Image was deleted or moved to a different path

## How to Fix

### 1. Verify image exists
```bash
gcloud artifacts docker images list PROJECT_ID/REPO \
  --include-tags --format="table(name,tags)"
```

### 2. Grant image access
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.reader"
```

### 3. Check image path
```bash
gcloud run deploy SERVICE_NAME \
  --image=LOCATION-docker.pkg.dev/PROJECT_ID/REPO/IMAGE:TAG \
  --region=REGION
```

### 4. Enable Artifact Registry API
```bash
gcloud services enable artifactregistry.googleapis.com --project=PROJECT_ID
```

## Examples

### List all images in repository
```bash
gcloud artifacts docker images list us-central1-docker.pkg.dev/my-project/my-repo
```

### Pull image locally for testing
```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
docker pull us-central1-docker.pkg.dev/my-project/my-repo/my-image:tag
```

## Related Errors

- [GCP Artifact Registry Error]({{< relref "/cloud/gcp/gcp-artifact-registry-error" >}})
- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
