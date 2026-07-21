---
title: "[Solution] GCP IAM Token Expired Error"
description: "Fix IAM token expired errors in GCP. Resolve authentication token, credential, and access token lifecycle issues in Google Cloud IAM."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP IAM Token Expired Error

The IAM Token Expired error occurs when application credentials or access tokens have expired and need to be refreshed to continue making authenticated API calls.

## Common Causes

- Default compute engine credentials expired after 1 hour
- Service account key was manually rotated without updating consumers
- Application Default Credentials cache is stale
- Token refresh endpoint is unreachable
- Organization policy restricts token lifetime

## How to Fix

### 1. Regenerate access token
```bash
gcloud auth application-default login
```

### 2. Refresh service account token
```bash
gcloud iam service-accounts keys create new-key.json \
  --iam-account=SA@PROJECT_ID.iam.gserviceaccount.com
```

### 3. Set up workload identity
```bash
gcloud iam service-accounts add-iam-policy-binding SA@PROJECT_ID.iam.gserviceaccount.com \
  --role=roles/iam.workloadIdentityUser \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[K8S_SA]"
```

### 4. Verify token validity
```bash
gcloud auth print-access-token
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones
```

## Examples

### Fetch and check token expiry
```bash
ACCESS_TOKEN=$(gcloud auth print-access-token)
curl -s https://oauth2.googleapis.com/tokeninfo?access_token=$ACCESS_TOKEN
```

### Rotate keys for a service account
```bash
OLD_KEY_ID=$(gcloud iam service-accounts keys list \
  --iam-account=SA@PROJECT_ID.iam.gserviceaccount.com \
  --format="value(name)" | head -1)
gcloud iam service-accounts keys disable $OLD_KEY_ID \
  --iam-account=SA@PROJECT_ID.iam.gserviceaccount.com
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}})
- [GCP Service Account Key]({{< relref "/cloud/gcp/gcp-service-account-key" >}})
