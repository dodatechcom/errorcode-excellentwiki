---
title: "[Solution] Resource already exists"
description: "Fix Kubernetes 'already exists' error. Resolve resource creation failures when a resource with the same name already exists."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Resource Already Exists

`Error from server (AlreadyExists): <resource> "<name>" already exists`

This error occurs when you try to create a Kubernetes resource with a name that already exists. Resource names must be unique within a namespace.

### Common Causes

- Running `kubectl create` instead of `kubectl apply` on an existing resource
- CI/CD pipeline creating resources without checking for existing ones
- Manual creation followed by automated creation

### How to Fix

Use `kubectl apply` which creates or updates:
```bash
kubectl apply -f resource.yaml
```

Delete and recreate:
```bash
kubectl delete <resource> <name>
kubectl create -f resource.yaml
```

### Examples

```bash
# Use apply instead of create
kubectl apply -f deployment.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})