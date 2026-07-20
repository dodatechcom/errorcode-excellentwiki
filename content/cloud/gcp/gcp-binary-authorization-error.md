---
title: "[Solution] GCP Binary Authorization Error — policy attestation errors"
description: "Fix GCP Binary Authorization errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 163
---

Binary Authorization errors occur when there are issues with policy configuration, attestation verification, or deploy rules.

## Common Causes
- Policy blocks deployment without matching attestation
- Attestor key verification fails
- Deploy rule doesn't match container registry
- Binary Authorization API not enabled
- Attestation format invalid

## How to Fix

### 1. Enable Binary Authorization API
```bash
gcloud services enable binaryauthorization.googleapis.com --project=PROJECT_ID
```

### 2. List policies
```bash
gcloud container binauthz policy list
```

### 3. Create attestation note
```bash
gcloud container binauthz attestation-notes create NOTE_NAME \
  --attestor-public-key=KEY_FILE \
  --attestor-note=NOTE_NAME
```

### 4. Create policy
```bash
gcloud container binauthz policy import policy.yaml
```

### 5. Create attestor
```bash
gcloud container binauthz attestors create ATTESTOR_NAME \
  --project=PROJECT_ID
```

## Examples

### Create allowlist policy
```bash
cat > policy.yaml <<EOF
defaultAdmissionRule:
  evaluationMode: ALWAYS_ALLOW
  enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
EOF
gcloud container binauthz policy import policy.yaml
```

### Add attestation to allow deployment
```bash
gcloud container binauthz attestors sign-image \
  --artifact-url=us-central1-docker.pkg.dev/PROJECT/REPO/IMAGE:TAG \
  --attestor=projects/PROJECT/attestors/ATTESTOR
```

## Related Errors
- [GCP Cloud Build Error](/cloud/gcp/gcp-cloud-build-error/)
- [GCP Artifact Registry Error](/cloud/gcp/gcp-artifact-registry-error/)
- [GCP GKE Error](/cloud/gcp/gcp-gke-error/)