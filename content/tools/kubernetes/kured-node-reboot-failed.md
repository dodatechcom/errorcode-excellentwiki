---
title: "[Solution] Kured node reboot failed"
description: "Fix Kured (Kubernetes Reboot Daemon) node reboot failures. Resolve issues when automatic node reboot fails."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Kured Node Reboot Failed

This error occurs when Kured (Kubernetes Reboot Daemon) cannot reboot a node that requires a reboot (e.g., pending kernel update).

### Common Causes

- Cordon succeeded but drain failed (PDB blocking)
- Reboot command not found (reboot binary missing)
- Kured not configured for the cloud provider

### How to Fix

Check Kured logs:
```bash
kubectl logs -n kube-system -l app.kubernetes.io/name=kured
```

### Examples

```bash
# Check Kured logs
kubectl logs -n kube-system -l app.kubernetes.io/name=kured --tail=50
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})