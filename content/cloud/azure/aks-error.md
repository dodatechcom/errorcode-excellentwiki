---
title: "Azure AKS: Container Health Checks Failed"
description: "AKS: Container health checks failed — Fix Azure Kubernetes Service health probe failures."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The AKS container health check failure occurs when Kubernetes liveness or readiness probes fail, causing pods to be restarted or removed from service endpoints. This is the most common cause of application unavailability on AKS.

## Common Causes

- Liveness probe fails because the application is deadlocked or crashed
- Readiness probe fails because the application is not ready to serve traffic
- Probe endpoint returns non-200 status code
- Application takes longer to start than the probe's `initialDelaySeconds`
- Resource limits cause the container to be OOMKilled

## How to Fix

Check pod status and events:

```bash
az aks get-credentials --resource-group my-rg --name my-aks

kubectl get pods -o wide
kubectl describe pod <pod-name>
kubectl logs <pod-name> --previous
```

Check health probe configuration:

```bash
kubectl get deployment my-app -o yaml | grep -A 20 "livenessProbe\|readinessProbe"
```

Update the deployment with better probe settings:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: my-app
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
        resources:
          limits:
            memory: "512Mi"
            cpu: "500m"
```

Apply the updated deployment:

```bash
kubectl apply -f deployment.yaml
kubectl rollout status deployment/my-app
```

## Examples

- Pod is in `CrashLoopBackOff` because the liveness probe keeps failing and Kubernetes restarts it
- Service has no endpoints because all pods fail readiness probes after a database connection timeout
- New pods fail to start because the initial probe delay is too short for the application to initialize

## Related Errors

- [Azure Disk Error]({{< relref "/cloud/azure/disk-error" >}}) — persistent volume I/O issues.
- [Azure Storage Error]({{< relref "/cloud/azure/storage-error" >}}) — storage account issues.
- [GCP GKE Error]({{< relref "/cloud/gcp/gke-error" >}}) — GKE equivalent.
