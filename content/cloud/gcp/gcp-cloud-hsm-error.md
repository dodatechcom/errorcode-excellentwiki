---
title: "[Solution] GCP Cloud HSM Error -- key partition quota errors"
description: "Fix GCP Cloud HSM errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 159
---

Cloud HSM errors occur when there are issues with HSM key creation, partition slots, or hardware security module quota.

## Common Causes
- HSM partition slots exhausted
- HSM quota limit exceeded for project
- Key algorithm not supported by HSM protection level
- Cloud HSM API not enabled
- Protection level mismatch between key and operation

## How to Fix

### 1. Enable Cloud KMS API (includes HSM)
```bash
gcloud services enable cloudkms.googleapis.com --project=PROJECT_ID
```

### 2. List HSM keys
```bash
gcloud kms keys list --keyring=KEYRING --location=LOCATION \
  --filter="protectionLevel=HSM"
```

### 3. Create HSM key
```bash
gcloud kms keys create HSM_KEY \
  --keyring=HSM_KEYRING \
  --location=LOCATION \
  --purpose=encrypt-decrypt \
  --default-algorithm=google_symmetric_encryption \
  --protection-level=hsm
```

### 4. Check HSM quota
```bash
gcloud services quota describe cloudkms.googleapis.com \
  --consumer=projects/PROJECT_ID
```

### 5. Create key with software fallback
```bash
gcloud kms keys create SW_KEY \
  --keyring=KEYRING \
  --location=LOCATION \
  --purpose=encrypt-decrypt \
  --protection-level=software
```

## Examples

### Generate asymmetric HSM key
```bash
gcloud kms keys create hsm-rsa-key \
  --keyring=hsm-ring \
  --location=us-central1 \
  --purpose=asymmetric-sign \
  --default-algorithm=rsa-sign-pkcs1-4096-sha256 \
  --protection-level=hsm
```

### List HSM key versions
```bash
gcloud kms keys versions list hsm-key \
  --keyring=hsm-ring \
  --location=us-central1
```

## Related Errors
- [GCP Cloud KMS Error](/cloud/gcp/gcp-cloud-kms-error/)
- [GCP Certificate Authority Error](/cloud/gcp/gcp-certificate-authority-error/)
- [GCP Secret Manager Error](/cloud/gcp/gcp-secret-manager-error/)