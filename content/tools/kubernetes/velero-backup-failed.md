---
title: "[Solution] Velero backup failed"
description: "Fix Velero backup failures in Kubernetes. Resolve issues with cluster backup and restore operations."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Velero Backup Failed

`Backup <name> failed: <error>`

This error occurs when Velero cannot complete a backup operation for a Kubernetes cluster.

### Common Causes

- Volume snapshot failed (CSI driver not installed)
- Cloud provider API permissions insufficient
- Backup location (S3, GCS, Azure Blob) is unreachable
- Backup storage bucket does not exist

### How to Fix

Check backup status:
```bash
velero backup describe <name> --details
kubectl logs -n velero deployment/velero
```

### Examples

```bash
# Check Velero backup
velero backup get
velero backup describe my-backup --details

# View failed backup details
velero backup logs my-backup | tail -50
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})