---
title: "[Solution] GCP GKE Pod Eviction Error"
description: "Fix GKE pod eviction errors. Resolve OOMKilled, node pressure, and resource-driven pod evictions in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Pod Eviction Error

The GKE Pod Eviction error occurs when pods are evicted from nodes due to resource pressure, OOMKilled, or node conditions.

## Common Causes

- Node memory pressure causes pods to be evicted
- Pods exceed their memory limits triggering OOMKilled
- Node disk pressure evicts pods to free space
- Pod disruption budgets prevent graceful eviction
- Node autoscaler is evicting pods to scale down

## How to Fix

### 1. Check eviction events
```bash
kubectl get events --field-selector reason=Evicted --sort-by=.lastTimestamp
```

### 2. Increase pod memory limits
```yaml
resources:
  limits:
    memory: "2Gi"
  requests:
    memory: "1Gi"
```

### 3. Check node conditions
```bash
kubectl describe nodes | grep -A 5 "Conditions:"
```

### 4. Add resource monitoring
```bash
kubectl top pods --sort-by=memory
kubectl top nodes --sort-by=memory
```

### 5. Configure eviction thresholds
```bash
gcloud container node-pools update POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=ZONE \
  --system-config-from-file=sysconfig.yaml
```

## Examples

### Monitor pod memory usage
```bash
kubectl get pods -A -o json | jq -r '.items[] | select(.status.containerStatuses[].lastState.terminated.reason == "OOMKilled") | .metadata.name'
```

### Set pod memory requests
```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    resources:
      requests:
        memory: "512Mi"
      limits:
        memory: "1Gi"
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP GKE Node Pool Resource Exhausted]({{< relref "/cloud/gcp/gcp-gke-node-pool-resource-exhausted" >}})
