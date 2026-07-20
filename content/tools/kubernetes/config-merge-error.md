---
title: "[Solution] kubectl config merge error"
description: "Fix kubectl config merge errors. Resolve issues when merging multiple kubeconfig files."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Config Merge Error

`error: unable to merge multiple kubeconfig files`

This error occurs when kubectl cannot merge configuration from multiple kubeconfig files specified in KUBECONFIG.

### Common Causes

- Conflicting cluster, user, or context names
- Corrupted kubeconfig files
- Duplicate entries with different configurations
- Invalid YAML formatting in one of the files
- Incompatible kubeconfig versions

### How to Fix

Merge configs manually:
```bash
export KUBECONFIG=~/.kube/config:~/.kube/other-config
kubectl config view --merge --flatten > ~/.kube/merged
mv ~/.kube/merged ~/.kube/config
```

Validate the kubeconfig:
```bash
kubectl config view
```

### Examples

```bash
# Merge two configs
export KUBECONFIG=~/.kube/config:~/.kube/eks-config
kubectl config view --merge --flatten > ~/.kube/all-config
cp ~/.kube/all-config ~/.kube/config
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})