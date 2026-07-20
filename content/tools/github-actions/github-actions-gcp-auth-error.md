---
title: "[Solution] GitHub Actions GCP Auth Error"
description: "Fix GitHub Actions GCP authentication errors in CI workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

GCP auth errors occur when the workflow cannot authenticate with Google Cloud:

```
Error: ERROR: (gcloud.auth) No project detected
```

## Common Causes

- Workload Identity Federation not configured.
- Service account key not provided.

## How to Fix

**Use Workload Identity Federation:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: 'projects/123/locations/global/workloadIdentityPools/github-pool/providers/github'
      service_account: 'github-actions@my-project.iam.gserviceaccount.com'
  - run: gcloud compute instances list
```

## Examples

```yaml
steps:
  - uses: google-github-actions/auth@v2
    with:
      credentials_json: ${{ secrets.GCP_SA_KEY }}
```
