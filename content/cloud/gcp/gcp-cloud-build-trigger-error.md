---
title: "[Solution] GCP Cloud Build Trigger Error"
description: "Fix Cloud Build trigger errors. Resolve trigger creation failures, build configuration, and source repository issues in GCP Cloud Build."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Build Trigger Error

The Cloud Build Trigger error occurs when build triggers cannot be created, updated, or executed due to source, configuration, or permission issues.

## Common Causes

- Source repository is not connected to Cloud Build
- cloudbuild.yaml has syntax errors or invalid steps
- Service account lacks permissions to the source repo
- Trigger region does not match build region
- Substitution variables reference undefined values

## How to Fix

### 1. Check trigger status
```bash
gcloud builds triggers list --location=REGION
```

### 2. Create a trigger
```bash
gcloud builds triggers create github \
  --name=TRIGGER_NAME \
  --repo-name=REPO_NAME \
  --repo-owner=OWNER \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml
```

### 3. Grant Cloud Build access to source
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com" \
  --role="roles/source.reader"
```

### 4. Manually run a build
```bash
gcloud builds submit --config=cloudbuild.yaml .
```

## Examples

### Trigger with substitutions
```bash
gcloud builds triggers create github \
  --name=deploy-trigger \
  --repo-name=my-app \
  --repo-owner=my-org \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml \
  --substitutions=_REGION=us-central1,_SERVICE=my-service
```

### Check build logs
```bash
gcloud builds log BUILD_ID --location=REGION
```

## Related Errors

- [GCP Cloud Build Error]({{< relref "/cloud/gcp/gcp-cloud-build-error" >}})
- [GCP Cloudbuild Build Failed]({{< relref "/cloud/gcp/cloudbuild-build-failed" >}})
