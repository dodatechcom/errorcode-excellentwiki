---
title: "[Solution] GCP Cloud KMS Error -- key rotation version auth errors"
description: "Fix GCP Cloud KMS errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 158
---

Cloud KMS errors occur when there are issues with key management, rotation policies, version destruction, or authentication.

## Common Causes
- Key ring or key already exists
- Key version destroyed or disabled
- Rotation schedule misconfigured
- IAM permissions insufficient for key operations
- Cloud KMS API not enabled

## How to Fix

### 1. Enable Cloud KMS API
```bash
gcloud services enable cloudkms.googleapis.com --project=PROJECT_ID
```

### 2. List key rings and keys
```bash
gcloud kms keyrings list --location=LOCATION
gcloud kms keys list --keyring=KEYRING --location=LOCATION
```

### 3. Create key ring
```bash
gcloud kms keyrings create KEYRING --location=LOCATION
```

### 4. Create crypto key
```bash
gcloud kms keys create KEY_NAME \
  --keyring=KEYRING \
  --location=LOCATION \
  --purpose=encrypt-decrypt
```

### 5. Rotate key version
```bash
gcloud kms keys create VERSION_NAME \
  --keyring=KEYRING \
  --location=LOCATION \
  --key=KEY_NAME \
  --primary
```

## Examples

### Encrypt data with KMS key
```bash
gcloud kms encrypt \
  --key=KEY_NAME \
  --keyring=KEYRING \
  --location=LOCATION \
  --plaintext-file=secret.txt \
  --cipher-file=secret.enc
```

### Set key rotation policy
```bash
gcloud kms keys update KEY_NAME \
  --keyring=KEYRING \
  --location=LOCATION \
  --rotation-period=7776000s \
  --next-rotation-time=2025-01-01T00:00:00Z
```

## Related Errors
- [GCP Cloud HSM Error](/cloud/gcp/gcp-cloud-hsm-error/)
- [GCP Secret Manager Error](/cloud/gcp/gcp-secret-manager-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)