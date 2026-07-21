---
title: "[Solution] GCP GKE Multi-Cluster Error"
description: "Fix GKE multi-cluster errors. Resolve multi-cluster services, fleet, and Anthos multi-cluster management issues in GCP GKE."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Multi-Cluster Error

The GKE Multi-Cluster error occurs when managing applications across multiple GKE clusters using multi-cluster services or fleet management.

## Common Causes

- Clusters are not registered with the same fleet
- Multi-cluster services controller is not enabled
- VPC peering is not configured between clusters
- Cluster names or regions conflict in fleet config
- Anthos service mesh is not installed across clusters

## How to Fix

### 1. Register cluster with fleet
```bash
gcloud container fleet memberships register MEMBER_NAME \
  --gke-cluster=ZONE/CLUSTER_NAME \
  --enable-workload-identity
```

### 2. Enable multi-cluster services
```bash
gcloud container fleet multi-cluster-services enable \
  --project=PROJECT_ID
```

### 3. Configure multi-cluster service
```yaml
apiVersion: networking.gke.io/v1
kind: MultiClusterService
metadata:
  name: my-service
spec:
  template:
    spec:
      selector:
        app: my-app
      ports:
      - port: 80
        targetPort: 8080
```

### 4. Check fleet status
```bash
gcloud container fleet memberships list --format="table(name,cluster)"
```

## Examples

### Deploy multi-cluster service
```bash
kubectl apply -f - << EOF
apiVersion: networking.gke.io/v1
kind: MultiClusterService
metadata:
  name: frontend
spec:
  template:
    spec:
      selector:
        app: frontend
      ports:
      - port: 80
EOF
```

### List fleet clusters
```bash
gcloud container fleet memberships list
```

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gcp-gke-error" >}})
- [GCP GKE Autopilot]({{< relref "/cloud/gcp/gcp-gke-autopilot" >}})
