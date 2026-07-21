---
title: "[Solution] GCP GKE Canary Deployment Error"
description: "Fix GKE canary deployment errors. Resolve canary release, traffic splitting, and progressive delivery issues in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Canary Deployment Error

The GKE Canary Deployment error occurs when canary deployments fail to route traffic correctly or cannot be promoted due to misconfiguration.

## Common Causes

- Istio or Anthos service mesh is not configured for traffic splitting
- Canary deployment YAML has incorrect virtual service rules
- Canary replica count is too low to receive traffic
- Prometheus/Grafana monitoring is not set up for canary metrics
- Rollout controller is not installed in the cluster

## How to Fix

### 1. Install Argo Rollouts
```bash
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/install.yaml
```

### 2. Define canary rollout
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  replicas: 10
  strategy:
    canary:
      steps:
      - setWeight: 20
      - pause: {duration: 5m}
      - setWeight: 40
      - pause: {duration: 5m}
      - setWeight: 60
      - setWeight: 100
```

### 3. Check rollout status
```bash
kubectl argo rollouts status my-app
```

### 4. Promote canary to stable
```bash
kubectl argo rollouts promote my-app
```

## Examples

### Canary with analysis
```yaml
strategy:
  canary:
    analysis:
      templates:
      - templateName: success-rate
      args:
      - name: service-name
        value: my-app
    steps:
    - setWeight: 25
    - pause: {duration: 10m}
```

### View canary replicas
```bash
kubectl get pods -l app=my-app --show-labels
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP GKE Autopilot]({{< relref "/cloud/gcp/gcp-gke-autopilot" >}})
