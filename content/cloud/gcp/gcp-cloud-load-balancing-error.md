---
title: "[Solution] GCP Cloud Load Balancing Error — HTTP(S) TCP UDP LB backend errors"
description: "Fix GCP Cloud Load Balancing errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 102
---

Cloud Load Balancing errors occur when there are issues with load balancer configuration, backend health checks, or SSL certificate problems.

## Common Causes
- Backend instances not responding to health checks
- Invalid SSL certificates or expired certificates
- Misconfigured URL maps or forwarding rules
- Backend service quota limits exceeded
- Instance not in the same region as load balancer

## How to Fix

### 1. Check load balancer status
```bash
gcloud compute forwarding-rules list
gcloud compute target-http-proxies list
gcloud compute url-maps list
```

### 2. Verify backend health
```bash
gcloud compute backend-services get-health BACKEND_SERVICE_NAME --region=REGION
```

### 3. Check SSL certificate
```bash
gcloud compute ssl-certificates list
gcloud compute ssl-certificates describe CERTIFICATE_NAME
```

### 4. Update backend service
```bash
gcloud compute backend-services update BACKEND_SERVICE_NAME \
  --health-checks=HEALTH_CHECK_NAME \
  --protocol=HTTP \
  --port-name=http \
  --global
```

### 5. Create health check
```bash
gcloud compute health-checks create http HEALTH_CHECK_NAME \
  --port=80 \
  --request-path=/health \
  --check-interval=10 \
  --timeout=5 \
  --healthy-threshold=2 \
  --unhealthy-threshold=3
```

## Examples

### Fix unhealthy backends
```bash
gcloud compute backend-services remove-instances my-backend-service \
  --instances=instance1,instance2 \
  --instance-group=INSTANCE_GROUP \
  --region=us-central1

gcloud compute backend-services add-instances my-backend-service \
  --instances=instance1,instance2 \
  --instance-group=INSTANCE_GROUP \
  --region=us-central1
```

### Update SSL certificate
```bash
gcloud compute ssl-certificates update my-cert \
  --certificate=cert.pem \
  --private-key=key.pem
```

## Related Errors
- [GCP Compute Engine Error](/cloud/gcp/gcp-compute-error/)
- [GCP Cloud CDN Error](/cloud/gcp/gcp-cloud-cdn-error/)
- [GCP Cloud Armor Error](/cloud/gcp/gcp-cloud-armor-error/)