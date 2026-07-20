---
title: "[Solution] CPU Manager policy error"
description: "Fix Kubernetes CPU Manager policy errors. Resolve issues when the CPU Manager configuration causes pod scheduling failures."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CPU Manager Policy Error

`Failed to start container: failed to set cpu_manager policy: error updating CPU manager`

This error occurs when the kubelet's CPU Manager policy configuration causes errors during pod startup.

### Common Causes

- CPU Manager policy set to `static` but node does not have exclusive CPUs
- CPU Manager state file is corrupted
- CPU Manager cannot allocate the requested CPUs
- kubelet restart with stale CPU manager state
- Insufficient CPU capacity for static policy
- SMT (Hyper-Threading) alignment issues

### How to Fix

Reset the CPU Manager state:
```bash
sudo systemctl stop kubelet
sudo rm -f /var/lib/kubelet/cpu_manager_state
sudo systemctl start kubelet
```

Change CPU Manager policy:
```bash
# In kubelet config
cpuManagerPolicy: none
```

### Examples

```bash
# Reset CPU manager state
sudo systemctl stop kubelet
sudo rm -f /var/lib/kubelet/cpu_manager_state
sudo systemctl start kubelet

# Check current policy
sudo cat /var/lib/kubelet/cpu_manager_state | jq .
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})