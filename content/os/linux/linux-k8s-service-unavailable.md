---
title: "[Solution] k8s: Service Unavailable — No Endpoints for Service"
description: "Fix Kubernetes service unavailable errors. Resolve 'no endpoints available for service' and ClusterIP/NodePort connectivity issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kubernetes", "k8s", "service", "endpoints", "clusterip", "connectivity"]
weight: 5
---

# k8s: Service Unavailable — No Endpoints for Service

A service unavailable error occurs when a Kubernetes Service has no backing pods (endpoints). The error reads:

> "no endpoints available for service \"my-service\""

Or in a pod:

> "Connection refused" when accessing the service ClusterIP.

## What This Error Means

Kubernetes Services use label selectors to route traffic to pods. When no pods match the Service's selector — because pods are crashing, have wrong labels, or haven't started — the Service has zero endpoints and returns connection errors. ClusterIP services have no external IP, so the connection is refused at the IP level.

## Common Causes

- No pods match the Service selector labels
- All pods are in CrashLoopBackOff or Pending state
- Service selector labels don't match pod labels (typo, case sensitivity)
- Pod readiness probe failing (pod is running but not Ready)
- Network policy blocking traffic to the Service
- kube-proxy not running on the node

## How to Fix

### Check Service Endpoints

```bash
kubectl get endpoints <service-name>
kubectl describe service <service-name>
```

If endpoints are empty, no pods match the selector.

### Verify Pod Labels Match Service Selector

```bash
# Check service selector
kubectl get svc <service-name> -o yaml | grep -A 5 selector

# Check pod labels
kubectl get pods --show-labels

# Find pods matching the selector
kubectl get pods -l app=myapp,version=v1
```

### Check Pod Readiness

```bash
kubectl get pods -o wide
kubectl describe pod <pod-name> | grep -A 10 "Conditions:"
```

Pod must have `Ready=True` to be an endpoint.

### Check Network Policy

```bash
kubectl get networkpolicy
kubectl describe networkpolicy <policy-name>
```

### Test Connectivity from Inside the Cluster

```bash
kubectl run debug --rm -it --image=busybox -- wget -qO- http://<service-name>:<port>
```

### Check kube-proxy

```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
kubectl logs -n kube-system -l k8s-app=kube-proxy
```

## Related Errors

- [k8s CrashLoopBackOff]({{< relref "/os/linux/linux-k8s-crashloop" >}}) — Pods crashing before becoming endpoints
- [k8s NetworkPolicy Error]({{< relref "/os/linux/linux-k8s-network-policy" >}}) — Network policy blocking traffic
- [k8s DNS Resolution Failed]({{< relref "/os/linux/linux-k8s-dns-resolution" >}}) — DNS lookup failures for services
