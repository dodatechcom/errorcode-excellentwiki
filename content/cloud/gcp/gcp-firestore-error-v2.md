---
title: "[Solution] GCP Firestore — permission denied"
description: "Fix Firestore permission denied. Resolve Firestore access and IAM issues."
cloud: ["gcp"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gcp", "firestore", "permission", "denied", "access", "database", "security"]
weight: 5
---

A Firestore permission denied error means the caller lacks the required IAM role or Firestore security rule permissions to perform the requested operation on the database.

## What This Error Means

Firestore uses two layers of access control: IAM roles at the project/database level, and security rules for client-side access. A permission denied error occurs when the authenticated identity does not have the appropriate Firestore IAM role (e.g., `roles/datastore.user`) or when security rules deny the specific operation. For server-side SDKs (Admin SDK), IAM is the primary control. For client-side SDKs (Web, mobile), security rules determine access. The error message distinguishes between IAM-level and security rule-level denials.

## Common Causes

- Service account or user missing `roles/datastore.user` or `roles/datastore.admin`
- Security rules deny the read/write operation for the client identity
- Firestore API not enabled in the project
- Database mode (Native or Datastore) does not support the operation
- Document path or collection ID is incorrect
- Accessing a Firestore database in a different Google Cloud project

## How to Fix

### Check IAM Role

```bash
gcloud projects get-iam-policy my-project \
  --flatten="bindings[].members" \
  --format="table(bindings.role, bindings.members)" \
  --filter="bindings.role:datastore"
```

### Grant Firestore Role

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="user:admin@example.com" \
  --role="roles/datastore.user"
```

### Enable Firestore API

```bash
gcloud services enable firestore.googleapis.com --project=my-project
```

### Check Security Rules (Client SDK)

```javascript
// Firebase security rules example
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth.uid == userId;
    }
  }
}
```

### Test with Admin SDK

```python
from google.cloud import firestore

db = firestore.Client(project='my-project')
doc = db.collection('users').document('user1').get()
```

### Verify Database Mode

```bash
gcloud firestore databases list --project=my-project
```

### Check Project ID

```python
# Ensure you're using the correct project
db = firestore.Client(project='correct-project-id')
```

### Grant Datastore Role for Legacy

```bash
gcloud projects add-iam-policy-binding my-project \
  --member="serviceAccount:my-sa@my-project.iam.gserviceaccount.com" \
  --role="roles/datastore.user"
```

### Debug with Firebase CLI

```bash
firebase projects:list
firebase use my-project
firebase experiments:enable webframeworks
```

## Related Errors

- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error-v2" >}}) — permission denied
- [GCP Storage Error]({{< relref "/cloud/gcp/gcp-storage-error-v2" >}}) — bucket not found
- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error-v2" >}}) — dataset not found
