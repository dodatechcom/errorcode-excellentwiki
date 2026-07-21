---
title: "[Solution] GCP Cloud Storage Signed URL Error"
description: "Fix Cloud Storage signed URL errors. Resolve URL generation, expiration, signature, and access issues in Google Cloud Storage."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Storage Signed URL Error

The Cloud Storage Signed URL error occurs when generated signed URLs fail to allow access to GCS objects due to signature or configuration problems.

## Common Causes

- Signed URL has expired
- Service account does not have signBlob permission
- URL was signed with wrong key or method
- Object ACLs block the signed URL access
- Clock skew causes verification failure

## How to Fix

### 1. Generate signed URL with gsutil
```bash
gsutil signurl -d 1h -r us-central1 \
  service-account-key.json \
  gs://BUCKET/object.txt
```

### 2. Grant signBlob permission
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountTokenCreator"
```

### 3. Generate signed URL with Python
```python
from google.cloud import storage
client = storage.Client()
bucket = client.bucket("BUCKET")
blob = bucket.blob("object.txt")
url = blob.generate_signed_url(
    version="v4",
    expiration="1h",
    method="GET"
)
```

### 4. Set correct clock on client
```bash
sudo ntpdate ntp.ubuntu.com
```

## Examples

### Generate signed POST URL
```python
url = blob.generate_signed_url(
    version="v4",
    expiration="1h",
    method="POST",
    content_type="application/octet-stream"
)
```

### Verify signed URL access
```bash
curl -I "SIGNED_URL"
```

## Related Errors

- [GCP Storage Error]({{< relref "/cloud/gcp/gcp-storage-error" >}})
- [GCP Object Upload Error]({{< relref "/cloud/gcp/gcp-object-upload-error" >}})
