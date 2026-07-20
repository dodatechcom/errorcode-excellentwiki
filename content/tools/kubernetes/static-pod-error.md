---
title: "[Solution] Static pod error in Kubernetes"
description: "Fix Kubernetes static pod errors. Resolve issues with static pods managed directly by the kubelet on a node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Static Pod Error

Static pods are pods managed directly by the kubelet on a specific node. They are defined in the kubelet's manifest directory.

### Common Causes

- Manifest file has YAML syntax errors
- Static pod conflict with API server-created pod
- Kubelet cannot read the manifest directory
- Invalid pod specification
- Duplicate pod names across nodes
- Mirror pod not created on the API server

### How to Fix

Check the static pod manifest directory:
```bash
sudo ls /etc/kubernetes/manifests/
```

Validate the manifest:
```bash
sudo kubelet --validate-config --config /var/lib/kubelet/config.yaml
```

Check kubelet logs for static pod errors:
```bash
sudo journalctl -u kubelet | grep -i "static\|mirror"
```

### Examples

```bash
# List static pods
sudo ls /etc/kubernetes/manifests/
# kube-apiserver.yaml
# kube-controller-manager.yaml
# kube-scheduler.yaml

# Validate a static pod manifest
kubectl apply -f /etc/kubernetes/manifests/kube-apiserver.yaml --dry-run=server
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})