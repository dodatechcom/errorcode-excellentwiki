---
title: "[Solution] GCP GKE Horizontal Pod Autoscaler Error"
description: "Fix GKE Horizontal Pod Autoscaler errors. Resolve HPA scaling, metrics, and configuration issues in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Horizontal Pod Autoscaler Error

The GKE Horizontal Pod Autoscaler error occurs when HPA fails to scale pods based on metrics due to misconfiguration or missing metrics.

## Common Causes

- Metrics Server is not installed in the cluster
- HPA target CPU/Memory utilization is set incorrectly
- Custom metrics are not available from the application
- Min/max replicas are not properly configured
- Resource requests are not defined on pods

## How to Fix

### 1. Check HPA status
```bash
kubectl get hpa -A
```

### 2. Verify metrics server
```bash
kubectl get deployment metrics-server -n kube-system
kubectl top pods -n kube-system
```

### 3. Create HPA
```bash
kubectl autoscale deployment my-app \
  --cpu-percent=70 \
  --min=2 \
  --max=10
```

### 4. Check HPA events
```bash
kubectl describe hpa my-app-hpa
```

### 5. Install metrics server (if missing)
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

## Examples

### HPA with custom metrics
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### Check scaling history
```bash
kubectl get events --field-selector reason=ScalingReplicaSet --sort-by=.lastTimestamp
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP GKE Node Pool Resource Exhausted]({{< relref "/cloud/gcp/gcp-gke-node-pool-resource-exhausted" >}})
