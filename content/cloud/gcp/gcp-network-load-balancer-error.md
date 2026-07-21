---
title: "[Solution] GCP Network Load Balancer Error"
description: "Fix Network Load Balancer errors in GCP. Troubleshoot forwarding rules, health checks, and backend configuration for TCP/UDP LBs."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Network Load Balancer Error

The Network Load Balancer error occurs when TCP/UDP network load balancers fail to route traffic to backends due to configuration or health check issues.

## Common Causes

- Health check fails for all backend instances
- Forwarding rule points to wrong target pool or backend service
- Firewall rules block health check probe source IPs
- Backend instances are in a different region than the load balancer
- Session affinity settings cause uneven traffic distribution

## How to Fix

### 1. Verify health check status
```bash
gcloud compute health-checks list --format="table(name,region,status)"
```

### 2. Create TCP health check
```bash
gcloud compute health-checks create tcp TCP_HC \
  --port=80 \
  --check-interval=10s \
  --timeout=5s \
  --healthy-threshold=2 \
  --unhealthy-threshold=3
```

### 3. Allow health check source IPs
```bash
gcloud compute firewall-rules create allow-health-checks \
  --allow=tcp:80,tcp:443 \
  --source-ranges=35.191.0.0/16,130.211.0.0/22 \
  --target-tags=lb-backend
```

### 4. Fix forwarding rule target
```bash
gcloud compute forwarding-rules update FORWARDING_RULE_NAME \
  --region=REGION \
  --target-backend-service=BACKEND_SERVICE
```

## Examples

### Create a TCP load balancer
```bash
gcloud compute target-pools create my-target-pool \
  --region=us-central1 \
  --health-check=TCP_HC

gcloud compute forwarding-rules create my-forwarding-rule \
  --region=us-central1 \
  --target-pool=my-target-pool \
  --ports=80
```

### Check backend health
```bash
gcloud compute target-pools get-health my-target-pool \
  --region=us-central1 \
  --format="yaml(backendService)"
```

## Related Errors

- [GCP Cloud Load Balancing Error]({{< relref "/cloud/gcp/gcp-cloud-load-balancing-error" >}})
- [GCP Health Check]({{< relref "/cloud/gcp/gcp-health-check" >}})
