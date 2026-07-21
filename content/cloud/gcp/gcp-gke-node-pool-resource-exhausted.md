---
title: "[Solution] GCP GKE Node Pool Resource Exhausted"
description: "Fix GKE node pool resource exhaustion. Resolve insufficient capacity, resource pressure, and scaling failures in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Node Pool Resource Exhausted

The GKE Node Pool Resource Exhausted error occurs when a node pool runs out of CPU, memory, or GPU resources and cannot schedule new pods.

## Common Causes

- Node pool max node count reached
- Pods request more resources than available on nodes
- GPU nodes have no spare capacity for new pods
- Local SSD storage is full
- Ephemeral storage pressure causes evictions

## How to Fix

### 1. Check node resource usage
```bash
kubectl describe nodes | grep -A 5 "Allocated resources"
```

### 2. Enable cluster autoscaling
```bash
gcloud container clusters update CLUSTER_NAME \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=10 \
  --zone=ZONE
```

### 3. Add node pool
```bash
gcloud container node-pools create extra-pool \
  --cluster=CLUSTER_NAME \
  --zone=ZONE \
  --num-nodes=3 \
  --machine-type=e2-standard-8
```

### 4. Reduce pod resource requests
```yaml
resources:
  requests:
    cpu: "200m"
    memory: "256Mi"
```

## Examples

### Check autoscaler status
```bash
gcloud container node-pools describe default-pool \
  --cluster=CLUSTER_NAME --zone=ZONE \
  --format="yaml(autoscaling)"
```

### Monitor node pressure
```bash
kubectl get nodes -o custom-columns=\
"NAME:.metadata.name,CPU_ALLOC:.status.capacity.cpu,\
MEM_ALLOC:.status.capacity.memory"
```

## Related Errors

- [GCP GKE Node Pool]({{< relref "/cloud/gcp/gcp-node-pool-(gke)" >}})
- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
