---
title: "[Solution] Helm upgrade failed"
description: "Fix Helm upgrade failures in Kubernetes. Resolve errors when upgrading Helm releases."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Helm Upgrade Failed

`Error: UPGRADE FAILED: <release> has no deployed releases`

This error occurs when a Helm upgrade cannot find a deployed release to upgrade.

### Common Causes

- Release was deleted with `helm delete` but not `helm uninstall`
- Release history was purged
- Release name is misspelled
- Release is in a failed state
- Wrong Helm version compatibility

### How to Fix

Check release history:
```bash
helm history <release>
```

List all releases:
```bash
helm list -a
```

Reinstall instead of upgrade:
```bash
helm upgrade --install <release> <chart>
```

Force rollback to a working revision:
```bash
helm rollback <release> <revision>
```

### Examples

```bash
# Install or upgrade
helm upgrade --install my-app ./chart --namespace default --create-namespace

# Check release history
helm history my-app
# REVISION  STATUS     CHART
# 1         failed     my-app-1.0.0
# 2         deployed   my-app-1.0.1
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})