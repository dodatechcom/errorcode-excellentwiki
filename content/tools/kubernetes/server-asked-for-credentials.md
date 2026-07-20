---
title: "[Solution] Server has asked for the credentials"
description: "Fix kubectl 'server has asked for the credentials' error. Resolve authentication failures when the API server requires valid credentials."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Server Asked for Credentials

`error: You must be logged in to the server (the server has asked for the credentials)`

This error occurs when kubectl cannot authenticate with the Kubernetes API server. The server is reachable but no valid credentials are provided.

### Common Causes

- Kubeconfig is missing or incomplete
- Token has expired
- Client certificate has expired
- Wrong user context selected

### How to Fix

Check current user context:
```bash
kubectl config view --minify -o jsonpath='{.users[0].name}'
```

Re-authenticate with your cloud provider:
```bash
gcloud container clusters get-credentials <cluster> --region <region>
aws eks update-kubeconfig --name <cluster>
az aks get-credentials --name <cluster> --resource-group <rg>
```

### Examples

```bash
# EKS cluster
aws eks update-kubeconfig --region us-east-1 --name my-cluster

# GKE cluster
gcloud container clusters get-credentials my-cluster --zone us-central1-a
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})