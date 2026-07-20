---
title: "[Solution] GCP Workload Identity Error — federation pool provider errors"
description: "Fix GCP Workload Identity errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 165
---

Workload Identity errors occur when there are issues with workload identity pools, provider configuration, or federation setup.

## Common Causes
- Workload identity pool not created
- Provider OIDC configuration invalid
- Service account not linked to workload identity
- Token exchange fails due to claim mismatch
- Workload Identity Federation API not enabled

## How to Fix

### 1. Enable Workload Identity Federation API
```bash
gcloud services enable iamcredentials.googleapis.com --project=PROJECT_ID
```

### 2. Create workload identity pool
```bash
gcloud iam workload-identity-pools create POOL_NAME \
  --location=global \
  --display-name="My Pool"
```

### 3. Create provider
```bash
gcloud iam workload-identity-pools providers create-oidc PROVIDER_NAME \
  --workload-identity-pool=POOL_NAME \
  --location=global \
  --issuer-uri="https://token.actions.githubusercontent.com" \
  --allowed-audiences="https://github.com/ORG"
```

### 4. Grant workload identity user role
```bash
gcloud iam service-accounts add-iam-policy-binding SA_NAME@PROJECT.iam.gserviceaccount.com \
  --role=roles/iam.workloadIdentityUser \
  --member="principalSet://iam.googleapis.com/projects/PROJECT/locations/global/workloadIdentityPools/POOL/attribute.repository/ORG/REPO"
```

### 5. Exchange token for access token
```bash
gcloud iam workload-identity-pools create-cred-config \
  --workload-identity-pool=POOL_NAME \
  --workload-identity-pool-provider=PROVIDER_NAME \
  --service-account=SA_NAME@PROJECT.iam.gserviceaccount.com \
  --credential-file-type=external_account \
  --output-file=config.json
```

## Examples

### Configure for GitHub Actions
```bash
gcloud iam workload-identity-pools providers create-oidc github-provider \
  --workload-identity-pool=github-pool \
  --location=global \
  --issuer-uri="https://token.actions.githubusercontent.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository"
```

### Test workload identity
```bash
gcloud iam workload-identity-pools describe POOL_NAME --location=global
```

## Related Errors
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
- [GCP GKE Error](/cloud/gcp/gcp-gke-error/)
- [GCP Cloud Build Error](/cloud/gcp/gcp-cloud-build-error/)