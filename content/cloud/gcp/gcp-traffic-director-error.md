---
title: "[Solution] GCP Traffic Director Error — mesh endpoint health errors"
description: "Fix GCP Traffic Director errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 107
---

Traffic Director errors occur when there are issues with service mesh configuration, endpoint health checks, or traffic management policies.

## Common Causes
- Service mesh configuration not properly attached to proxies
- Endpoint health check failures
- Traffic policy misconfiguration (retry, timeout, circuit breaking)
- Proxy-less gRPC service configuration issues
- Network services API not enabled

## How to Fix

### 1. Enable Network Services API
```bash
gcloud services enable networkservices.googleapis.com --project=PROJECT_ID
```

### 2. List network services
```bash
gcloud network-services http-routes list --global
gcloud network-services grpc-routes list --global
gcloud network-services tcp-routes list --global
```

### 3. Create HTTP route for Traffic Director
```bash
gcloud network-services http-routes create ROUTE_NAME \
  --global \
  --hosts="example.com" \
  --path-matches="/api/*" \
  --service=BACKEND_SERVICE_NAME \
  --action=WEBHOOK
```

### 4. Configure traffic policy
```bash
gcloud network-services http-routes update ROUTE_NAME \
  --global \
  --retry-policy="retry-on=5xx,per-try-timeout=2s,num-retries=3"
```

### 5. List endpoint backends
```bash
gcloud compute backend-services describe BACKEND_SERVICE_NAME --global --format="yaml(backends)"
```

## Examples

### Set up Traffic Director with service mesh
```bash
gcloud network-services http-routes create api-route \
  --global \
  --hosts="api.example.com" \
  --path-matches="/*" \
  --service=my-backend-service \
  --action=WEBHOOK

gcloud network-services http-routes update api-route \
  --global \
  --retry-policy="retry-on=reset,per-try-timeout=1s,num-retries=2" \
  --timeout=30s
```

### Verify proxy configuration
```bash
gcloud network-services proxies list --global
```

## Related Errors
- [GCP GKE Error](/cloud/gcp/gcp-gke-error/)
- [GCP Cloud Run Error](/cloud/gcp/gcp-cloud-run-error/)
- [GCP Cloud Load Balancing Error](/cloud/gcp/gcp-cloud-load-balancing-error/)