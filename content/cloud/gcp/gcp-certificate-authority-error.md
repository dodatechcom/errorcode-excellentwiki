---
title: "[Solution] GCP Certificate Authority Error — pool cert revoke errors"
description: "Fix GCP Certificate Authority errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 160
---

Certificate Authority errors occur when there are issues with CA pools, certificate issuance, or certificate revocation.

## Common Causes
- CA pool not initialized
- Certificate template doesn't allow requested key type
- CA quota exceeded
- Revocation list publish location invalid
- Certificate Authority API not enabled

## How to Fix

### 1. Enable Certificate Authority API
```bash
gcloud services enable privateca.googleapis.com --project=PROJECT_ID
```

### 2. List certificate authorities
```bash
gcloud privateca locations list
gcloud privateca pools list --location=LOCATION
```

### 3. Create CA pool
```bash
gcloud privateca pools create POOL_NAME \
  --location=LOCATION \
  --tier=BASIC
```

### 4. Issue certificate
```bash
gcloud privateca certificates create CERT_NAME \
  --issuer-pool=POOL_NAME \
  --location=LOCATION \
  --subject="CN=example.com,O=My Org" \
  --subject-alt-name=dns=example.com,dns=www.example.com
```

### 5. Revoke certificate
```bash
gcloud privateca certificates revoke CERT_NAME \
  --issuer-pool=POOL_NAME \
  --location=LOCATION \
  --reason=key_compromise
```

## Examples

### Create subordinate CA
```bash
gcloud privateca roots create subordinate-ca \
  --ca-pool=ca-pool \
  --location=us-central1 \
  --subject="CN=Sub CA,O=My Org" \
  --is-ca=true \
  --max-chain-length=2
```

### Download issued certificate
```bash
gcloud privateca certificates describe CERT_NAME \
  --pool=ca-pool \
  --location=us-central1 \
  --format="value(pemCertificateChain)"
```

## Related Errors
- [GCP Cloud KMS Error](/cloud/gcp/gcp-cloud-kms-error/)
- [GCP IAP Error](/cloud/gcp/gcp-iap-error/)
- [GCP Load Balancing Error](/cloud/gcp/gcp-cloud-load-balancing-error/)