---
title: "[Solution] GCP GKE Pod Scheduling Error"
description: "Fix GKE pod scheduling errors. Resolve pending pods, resource requests, and node selector issues in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Pod Scheduling Error

The GKE Pod Scheduling error occurs when Kubernetes cannot place pods on nodes due to resource constraints, node selectors, or taint/toleration mismatches.

## Common Causes

- Insufficient CPU or memory on available nodes
- Pod resource requests exceed node capacity
- Node selector or affinity rules cannot be satisfied
- Taints on nodes have no matching tolerations
- PersistentVolumeClaim cannot be bound to a StorageClass

## How to Fix

### 1. Check pending pods
```bash
kubectl get pods --field-selector=status.phase=Pending
```

### 2. Inspect scheduling events
```bash
kubectl describe pod POD_NAME | grep -A 5 "Events"
```

### 3. Check node resource availability
```bash
kubectl describe nodes | grep -A 5 "Allocated resources"
```

### 4. Add node auto-provisioning
```bash
gcloud container clusters update CLUSTER_NAME \
  --enable-autoprovisioning \
  --min-cpu=4 --min-memory=16 \
  --max-cpu=100 --max-memory=400
```

### 5. Reduce resource requests
```yaml
resources:
  requests:
    cpu: "250m"
    memory: "512Mi"
  limits:
    cpu: "500m"
    memory: "1Gi"
```

## Examples

### Debug pod scheduling
```bash
kubectl get events --field-selector reason=FailedScheduling --sort-by=.lastTimestamp
```

### Add tolerations for tainted nodes
```yaml
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "ml-workload"
  effect: "NoSchedule"
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP GKE Autopilot]({{< relref "/cloud/gcp/gcp-gke-autopilot" >}})
