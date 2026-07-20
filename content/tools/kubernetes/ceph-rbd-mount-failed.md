---
title: "[Solution] Ceph RBD volume mount failed"
description: "Fix Kubernetes Ceph RBD volume mount failures. Resolve persistent volume mount errors with Ceph RBD storage."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Ceph RBD Mount Failed

`MountVolume.SetUp failed for volume "<name>" : rbd: map failed: exit status 1`

This error occurs when Kubernetes cannot mount a Ceph RBD (RADOS Block Device) volume.

### Common Causes

- Ceph cluster is unreachable
- Ceph secret key incorrect or missing
- RBD image does not exist
- Kernel RBD module not loaded
- Ceph monitor addresses incorrect
- Cephx authentication failure
- Pool or image name incorrect

### How to Fix

Check Ceph cluster connectivity:
```bash
ceph -s
```

Verify the Ceph secret in Kubernetes:
```bash
kubectl get secret <ceph-secret> -o yaml
```

Install ceph-common on all nodes:
```bash
sudo apt-get install -y ceph-common
```

### Examples

```bash
# Check Ceph status
ceph -s
# cluster: id: xxxx, health: HEALTH_OK

# Verify the RBD image exists
rbd info <pool>/<image>
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})