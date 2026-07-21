---
title: "[Solution] GCP Secret Manager Version Error"
description: "Fix Secret Manager version errors. Resolve secret version, access, and rotation issues in Google Cloud Secret Manager."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Secret Manager Version Error

The Secret Manager Version error occurs when accessing or managing secret versions fails due to permissions, naming, or version state issues.

## Common Causes

- Secret version does not exist or has been destroyed
- Application is using latest version alias incorrectly
- Secret Manager API is not enabled
- IAM permissions do not cover the specific version
- Secret was destroyed but code still references old version

## How to Fix

### 1. List secret versions
```bash
gcloud secrets versions list SECRET_NAME --format="table(name,state,createTime)"
```

### 2. Access secret version
```bash
gcloud secrets versions access latest --secret=SECRET_NAME
```

### 3. Enable Secret Manager API
```bash
gcloud services enable secretmanager.googleapis.com --project=PROJECT_ID
```

### 4. Grant version access
```bash
gcloud secrets add-iam-policy-binding SECRET_NAME \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

## Examples

### Create new version
```bash
echo -n "new-password" | \
  gcloud secrets versions add SECRET_NAME --data-file=-
```

### Destroy old version
```bash
gcloud secrets versions destroy VERSION_NAME --secret=SECRET_NAME
```

## Related Errors

- [GCP Secret Manager Error]({{< relref "/cloud/gcp/gcp-secret-manager-error" >}})
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}})
