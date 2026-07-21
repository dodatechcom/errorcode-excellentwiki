---
title: "[Solution] GCP Firestore Realtime Listener Error"
description: "Fix Firestore realtime listener errors. Resolve onSnapshot, snapshot listener, and real-time data sync issues in Google Cloud Firestore."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Firestore Realtime Listener Error

The Firestore Realtime Listener error occurs when Firestore snapshot listeners fail to connect or receive real-time updates.

## Common Causes

- Listener is not properly attached to a collection or document
- Network interruption causes listener disconnection
- Listener callback throws unhandled exceptions
- Too many concurrent listeners exceed quota
- Security rules block read operations for the listener

## How to Fix

### 1. Add error handler to listener
```python
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f"Document: {doc.id}")

doc_ref = db.collection("users").document("user1")
doc_ref.on_snapshot(on_snapshot)
```

### 2. Handle listener errors
```javascript
const unsubscribe = db.collection('users').onSnapshot(
  (snapshot) => { /* handle data */ },
  (error) => { console.error('Listener error:', error); }
);
```

### 3. Check listener quota
```bash
gcloud logging read "resource.type=cloud_firestore_database \
  AND severity>=WARNING" \
  --limit=20
```

### 4. Verify security rules
```bash
gcloud firestore rules describe --project=PROJECT_ID
```

## Examples

### Collection group listener
```python
query = db.collection_group("comments")
query.on_snapshot(on_snapshot)
```

### Query-based listener
```python
query = db.collection("users").where("active", "==", True)
query.on_snapshot(on_snapshot)
```

## Related Errors

- [GCP Firestore Error]({{< relref "/cloud/gcp/gcp-firestore-error" >}})
- [GCP Firestore Connection Error]({{< relref "/cloud/gcp/gcp-firestore-connection-error" >}})
