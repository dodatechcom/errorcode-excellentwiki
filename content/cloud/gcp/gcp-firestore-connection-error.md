---
title: "[Solution] GCP Firestore Connection Error"
description: "Fix Firestore connection errors. Resolve network, SDK, and API configuration issues when connecting to Google Cloud Firestore."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Firestore Connection Error

The Firestore Connection error occurs when applications cannot connect to Firestore due to network, authentication, or SDK misconfiguration.

## Common Causes

- Firestore API is not enabled in the GCP project
- Network firewall rules block Firestore traffic on port 443
- Service account lacks Firestore permissions
- SDK configuration points to wrong project or database
- VPC Service Controls block Firestore access

## How to Fix

### 1. Enable Firestore API
```bash
gcloud services enable firestore.googleapis.com --project=PROJECT_ID
```

### 2. Verify service account permissions
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/datastore.user"
```

### 3. Configure network access
```bash
gcloud compute firewall-rules create allow-firestore \
  --allow=tcp:443 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=firestore-client
```

### 4. Check Firestore location
```bash
gcloud firestore databases list --project=PROJECT_ID
```

## Examples

### Initialize Firestore client
```python
from google.cloud import firestore
db = firestore.Client(project="my-project")
```

### Test connectivity
```bash
gcloud firestore documents list --collection-path=test \
  --project=PROJECT_ID --limit=1
```

## Related Errors

- [GCP Firestore Error]({{< relref "/cloud/gcp/gcp-firestore-error" >}})
- [GCP Database Firestore]({{< relref "/cloud/gcp/gcp-database-(firestore)" >}})
