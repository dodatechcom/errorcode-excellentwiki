---
title: "[Solution] GCP GKE Network Policy Error"
description: "Fix GKE network policy errors. Resolve Kubernetes NetworkPolicy, Calico, and network segmentation issues in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Network Policy Error

The GKE Network Policy error occurs when NetworkPolicy enforcement fails, causing pods to have incorrect network access or connectivity issues.

## Common Causes

- Network policy enforcement is not enabled on the cluster
- Calico or Dataplane V2 is not installed
- NetworkPolicy YAML has incorrect pod selectors
- Default deny policy blocks required traffic
- Namespace labels are missing for policy targeting

## How to Fix

### 1. Enable network policy
```bash
gcloud container clusters update CLUSTER_NAME \
  --enable-network-policy \
  --region=REGION
```

### 2. Check network policy status
```bash
kubectl get networkpolicies -A
```

### 3. Create a basic allow policy
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-web
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: web
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
    ports:
    - port: 80
```

### 4. Check cluster addons
```bash
gcloud container clusters describe CLUSTER_NAME --zone=ZONE \
  --format="yaml(addonsConfig)"
```

## Examples

### Default deny all ingress
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

### Allow DNS resolution
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to: []
    ports:
    - port: 53
      protocol: UDP
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP VPC Error]({{< relref "/cloud/gcp/gcp-vpc-error" >}})
