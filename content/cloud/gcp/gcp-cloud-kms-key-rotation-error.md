---
title: "[Solution] GCP Cloud KMS Key Rotation Error"
description: "Fix Cloud KMS key rotation errors. Resolve key version rotation, rotation schedule, and crypto key issues in Google Cloud KMS."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud KMS Key Rotation Error

The Cloud KMS Key Rotation error occurs when automatic or manual key rotation fails, leaving crypto keys without new versions.

## Common Causes

- Key rotation period has not elapsed since last rotation
- Service account lacks Cloud KMS Admin role
- Primary key version is destroyed before rotation
- Key ring is in a disabled or restricted state
- Rotation schedule references invalid cron expression

## How to Fix

### 1. Check key version status
```bash
gcloud kms keys versions list \
  --key=KEY_NAME \
  --keyring=KEY_RING \
  --location=LOCATION \
  --format="table(name,state,createTime)"
```

### 2. Manually rotate a key
```bash
gcloud kms keys versions create \
  --key=KEY_NAME \
  --keyring=KEY_RING \
  --location=LOCATION
```

### 3. Set rotation schedule
```bash
gcloud kms keys update KEY_NAME \
  --keyring=KEY_RING \
  --location=LOCATION \
  --rotation-period=7776000s \
  --next-rotation-time=2025-06-01T00:00:00Z
```

### 4. Grant KMS admin role
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudkms.admin"
```

## Examples

### List active key versions
```bash
gcloud kms keys versions list \
  --key=my-key \
  --keyring=my-ring \
  --location=global \
  --filter="state=ENABLED"
```

### Destroy old key version
```bash
gcloud kms keys versions destroy VERSION_NAME \
  --key=KEY_NAME \
  --keyring=KEY_RING \
  --location=LOCATION
```

## Related Errors

- [GCP Cloud KMS Error]({{< relref "/cloud/gcp/gcp-cloud-kms-error" >}})
- [GCP Secret Manager Error]({{< relref "/cloud/gcp/gcp-secret-manager-error" >}})
