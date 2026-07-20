---
title: "[Solution] GCP Service Directory Error — namespace service endpoint errors"
description: "Fix GCP Service Directory errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 105
---

Service Directory errors occur when there are issues with namespaces, services, or endpoints in the managed service discovery platform.

## Common Causes
- Namespace already exists or invalid name format
- Service registration conflicts with existing entries
- Endpoint resolution failures due to DNS misconfiguration
- IAM permissions insufficient for namespace management
- Service Directory API not enabled in project

## How to Fix

### 1. Enable Service Directory API
```bash
gcloud services enable servicedirectory.googleapis.com --project=PROJECT_ID
```

### 2. List namespaces and services
```bash
gcloud servicedirectory namespaces list --location=REGION
gcloud servicedirectory namespaces services list --namespace=NAMESPACE --location=REGION
```

### 3. Create a namespace
```bash
gcloud servicedirectory namespaces create NAMESPACE \
  --location=REGION \
  --description="My namespace"
```

### 4. Register a service with endpoint
```bash
gcloud servicedirectory namespaces services create SERVICE_NAME \
  --namespace=NAMESPACE \
  --location=REGION

gcloud servicedirectory namespaces services endpoints create ENDPOINT_NAME \
  --service=SERVICE_NAME \
  --namespace=NAMESPACE \
  --location=REGION \
  --address=10.0.0.1 \
  --port=8080
```

### 5. Set IAM policy for namespace
```bash
gcloud servicedirectory namespaces set-iam-policy NAMESPACE \
  --region=REGION \
  --policy-file=policy.yaml
```

## Examples

### Create complete service discovery setup
```bash
gcloud servicedirectory namespaces create production \
  --location=us-central1

gcloud servicedirectory namespaces services create api-server \
  --namespace=production \
  --location=us-central1

gcloud servicedirectory namespaces services endpoints create api-ep-1 \
  --service=api-server \
  --namespace=production \
  --location=us-central1 \
  --address=10.0.1.10 \
  --port=8080
```

### Resolve service endpoint via DNS
```bash
nslookup api-server.production.us-central1.servicedirectory.googleapis.internal
```

## Related Errors
- [GCP Cloud DNS Error](/cloud/gcp/gcp-cloud-dns-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)