---
title: "[Solution] GCP reCAPTCHA Enterprise Error — key assessment site errors"
description: "Fix GCP reCAPTCHA Enterprise errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 167
---

reCAPTCHA Enterprise errors occur when there are issues with key management, risk assessment, or site configuration.

## Common Causes
- reCAPTCHA key not configured for site
- Assessment token expired or invalid
- Site key doesn't match domain
- reCAPTCHA Enterprise API not enabled
- Assessment threshold too restrictive

## How to Fix

### 1. Enable reCAPTCHA Enterprise API
```bash
gcloud services enable recaptchaenterprise.googleapis.com --project=PROJECT_ID
```

### 2. Create key
```bash
gcloud recaptcha keys create KEY_NAME \
  --display-name="My Site Key" \
  --web-settings-domains="example.com" \
  --type=SCORE
```

### 3. List keys
```bash
gcloud recaptcha keys list --format="table(name,displayName,type,create-time)"
```

### 4. Create assessment
```bash
curl -X POST \
  "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT/assessments" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"event":{"token":"USER_TOKEN","siteKey":"KEY_NAME","userAgent":"Mozilla/5.0"}}'
```

### 5. Get key details
```bash
gcloud recaptcha keys describe KEY_NAME
```

## Examples

### Create Android key
```bash
gcloud recaptcha keys create android-key \
  --display-name="Android App" \
  --android-settings="allowed-package-names=com.example.app"
```

### Check assessment result
```bash
curl -X POST \
  "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT/assessments" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"event":{"token":"TOKEN","siteKey":"KEY"},"reasons":["AUTOMATION"]}'
```

## Related Errors
- [GCP IAP Error](/cloud/gcp/gcp-iap-error/)
- [GCP Cloud Armor Error](/cloud/gcp/gcp-cloud-armor-error/)
- [GCP API Gateway Error](/cloud/gcp/gcp-api-gateway-error/)