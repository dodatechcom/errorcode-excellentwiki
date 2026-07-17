---
title: "[Solution] Kubernetes Service — no endpoints available"
description: "Fix Kubernetes Service no endpoints available. Resolve service routing failures."
tools: ["kubernetes"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Service with no endpoints means the service selector does not match any running pods. Traffic routed to this service will fail because there are no backing pods to handle requests.

## What This Error Means

Kubernetes creates Endpoints objects based on a Service's `selector` field. When no pods match the selector, the Endpoints list is empty. Clients connecting to the service's ClusterIP or DNS name receive connection errors because the kube-proxy rules have no backend addresses to forward to.

## Common Causes

- Service selector labels do not match pod labels
- Pods with matching labels are not in Running state
- Namespace mismatch between service and target pods
- Pods were deleted or scaled to zero
- Label typo in service spec or pod spec
- Pods failed to start due to another error

## How to Fix

### Check Service Endpoints

```bash
kubectl get endpoints <service-name>
```

### Verify Selector Matches Pod Labels

```bash
kubectl get pods --show-labels
kubectl describe service <service-name>
```

### Check Pod Status

```bash
kubectl get pods -l app=my-app
```

### Fix Label Mismatch

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app  # Must match pod labels exactly
  ports:
    - port: 80
      targetPort: 8080
```

### Manually Set Endpoints (Headless Service)

```bash
kubectl get endpoints <service-name> -o yaml
```

### Test Service Connectivity

```bash
kubectl run test --rm -it --image=busybox -- wget -qO- http://<service-name>
```

## Related Errors

- [Kubernetes Ingress Error]({{< relref "/tools/kubernetes/k8s-ingress-error-v2" >}}) — Ingress TLS error
- [Kubernetes NetworkPolicy]({{< relref "/tools/kubernetes/k8s-network-policy-v2" >}}) — ingress blocked
- [Kubernetes DNS Resolution]({{< relref "/tools/kubernetes/k8s-dns-resolution-v2" >}}) — CoreDNS failed
