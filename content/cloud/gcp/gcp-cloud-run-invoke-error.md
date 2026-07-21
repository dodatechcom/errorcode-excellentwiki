---
title: "[Solution] GCP Cloud Run Invoke Error"
description: "Fix Cloud Run service invocation errors. Resolve authentication, IAM, and service-to-service communication issues in Google Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Invoke Error

The Cloud Run Invoke error occurs when a client cannot invoke a Cloud Run service due to authentication, IAM, or networking issues.

## Common Causes

- Service does not allow unauthenticated invocations
- IAM binding is missing for the calling identity
- Service-to-service authentication token is invalid
- VPC connector is not configured for private services
- Maximum concurrent requests limit is reached

## How to Fix

### 1. Allow unauthenticated access
```bash
gcloud run services add-iam-policy-binding SERVICE_NAME \
  --member="allUsers" \
  --role="roles/run.invoker"
```

### 2. Grant invoke permission to a service account
```bash
gcloud run services add-iam-policy-binding SERVICE_NAME \
  --member="serviceAccount:CALLER_SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/run.invoker"
```

### 3. Check service URL
```bash
gcloud run services describe SERVICE_NAME \
  --region=REGION --format="value(status.url)"
```

### 4. Invoke with authentication
```bash
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  https://SERVICE_URL
```

## Examples

### Service-to-service invocation
```python
import requests
from google.auth.transport.requests import Request
from google.oauth2 import id_token

target_url = "https://SERVICE_URL"
id_token_request = id_token.fetch_id_token(Request(), audience=target_url)
response = requests.get(target_url, headers={"Authorization": f"Bearer {id_token_request}"})
```

### Update concurrency
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --concurrency=250 \
  --max-instances=100
```

## Related Errors

- [GCP Cloud Run Service]({{< relref "/cloud/gcp/gcp-cloud-run-service" >}})
- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
