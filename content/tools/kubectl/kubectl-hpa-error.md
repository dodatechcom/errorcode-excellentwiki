---
title: "[Solution] Kubectl HPA Error - Fix HorizontalPodAutoscaler Error"
description: "Fix Kubernetes HPA errors when autoscaling fails. Resolve metrics server issues, resource limits, and scaling configuration problems."
tools: ["kubectl"]
error-types: ["hpa-error"]
severities: ["warning"]
weight: 5
---

This error means the HorizontalPodAutoscaler (HPA) is not scaling pods as expected. The HPA cannot read metrics, the target does not exist, or scaling limits are reached.

## What This Error Means

When an HPA fails to function, you see:

```
kubectl get hpa
NAME        REFERENCE         TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
my-hpa      Deployment/myapp  <unknown>/50%   1         10        1          5m
```

The `unknown` target means the HPA cannot fetch metrics. Or the HPA may be stuck at min/max replicas despite load changes.

## Why It Happens

- The metrics server is not installed or not running
- The HPA target does not have CPU or memory requests set
- The HPA references a resource that does not exist
- Custom metrics are configured but the metrics adapter is not installed
- The target value is set to 0% which prevents scaling
- Min and max replicas are set to the same value
- The HPA cannot access the Kubernetes metrics API

## How to Fix It

### Install the metrics server

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

The metrics server provides CPU and memory metrics that HPAs need.

### Verify metrics are available

```bash
kubectl top pods
kubectl top nodes
```

If `kubectl top` does not work, the metrics server is not functioning.

### Check HPA status

```bash
kubectl describe hpa my-hpa
```

The Events section shows why scaling is not working.

### Set resource requests on the target

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
```

HPAs require resource requests to calculate utilization percentages.

### Verify the HPA target reference

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
```

### Set appropriate min and max replicas

```yaml
minReplicas: 2
maxReplicas: 10
```

Min and max must be different, and min must be at least 1.

### Check custom metrics configuration

```bash
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1" | jq .
```

If this returns an error, the custom metrics adapter is not installed.

## Common Mistakes

- Installing HPA without the metrics server
- Not setting CPU or memory requests on the target Deployment
- Setting minReplicas equal to maxReplicas, preventing scaling
- Using an older HPA API version that lacks required features
- Assuming HPA works immediately after deployment without waiting for metrics

## Related Pages

- [Kubectl Pod Pending]({{< relref "/tools/kubectl/kubectl-pod-pending" >}}) -- pod scheduling
- [Kubectl OOMKilled]({{< relref "/tools/kubectl/kubectl-oomkilled" >}}) -- memory limit kills
- [Kubectl Node Not Ready]({{< relref "/tools/kubectl/kubectl-node-not-ready" >}}) -- node health
