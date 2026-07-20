---
title: "[Solution] Bootstrap token expired"
description: "Fix Kubernetes bootstrap token expiration errors. Resolve node join failures when the cluster bootstrap token has expired."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Bootstrap Token Expired

`[discovery] Failed to request cluster-info, will try again: Get "https://<ip>:6443/api/v1/namespaces/kube-public/configmaps/cluster-info": x509: certificate has expired or is not yet valid`

This error occurs when the bootstrap token used to join a node to the cluster has expired.

### Common Causes

- Default token expiration (24 hours) has passed
- Token was deleted after use
- Cluster was created and node joined too late
- Token creation date is not tracked properly
- Manual token deletion

### How to Fix

Create a new bootstrap token on the control plane:
```bash
kubeadm token create
```

List existing tokens:
```bash
kubeadm token list
```

Create a token with longer expiration:
```bash
kubeadm token create --ttl 48h0m0s
```

### Examples

```bash
# Create new token
TOKEN=$(kubeadm token create)
echo $TOKEN

# Get the full join command
kubeadm token create --print-join-command
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})