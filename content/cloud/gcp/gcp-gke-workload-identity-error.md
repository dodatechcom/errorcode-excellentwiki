---
title: "[Solution] GCP GKE Workload Identity Error"
description: "Fix GKE Workload Identity errors. Resolve Workload Identity Pool, binding, and GCP API access issues in Google Kubernetes Engine."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP GKE Workload Identity Error

The GKE Workload Identity error occurs when Kubernetes pods cannot access GCP APIs using Workload Identity due to misconfigured bindings.

## Common Causes

- Workload Identity is not enabled on the cluster
- Kubernetes SA is not bound to a GCP service account
- Namespace annotation is missing or incorrect
- GCP service account lacks required IAM roles
- Workload Identity Pool is not in the project

## How to Fix

### 1. Enable Workload Identity
```bash
gcloud container clusters update CLUSTER_NAME \
  --workload-pool=PROJECT_ID.svc.id.goog
```

### 2. Create Workload Identity binding
```bash
gcloud iam service-accounts add-iam-policy-binding SA@PROJECT_ID.iam.gserviceaccount.com \
  --role=roles/iam.workloadIdentityUser \
  --member="serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/KSA]"
```

### 3. Annotate Kubernetes service account
```bash
kubectl annotate serviceaccount KSA \
  iam.gke.io/gcp-service-account=SA@PROJECT_ID.iam.gserviceaccount.com \
  -n NAMESPACE
```

### 4. Verify Workload Identity
```bash
gcloud iam service-accounts describe SA@PROJECT_ID.iam.gserviceaccount.com \
  --format="yaml(bindings)"
```

## Examples

### Deploy pod with Workload Identity
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      serviceAccountName: my-ksa
      containers:
      - name: app
        image: my-image
```

### Check pod access
```bash
kubectl exec -it POD_NAME -- curl -H "Metadata-Flavor: Google" \
  http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token
```

## Related Errors

- [GCP Workload Identity Error]({{< relref "/cloud/gcp/gcp-workload-identity-error" >}})
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}})
