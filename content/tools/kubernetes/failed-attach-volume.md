---
title: "[Solution] FailedAttachVolume"
description: "Fix Kubernetes FailedAttachVolume error. Resolve pod failures when a persistent volume cannot be attached to the node."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## FailedAttachVolume

This error occurs when the volume attachment controller cannot attach a persistent volume to the node where the pod is scheduled.

### Common Causes

- Volume already attached to another node (RWO volume)
- Cloud provider API rate limiting
- Volume does not exist in the cloud provider
- Incorrect availability zone or region
- IAM permissions insufficient for volume attachment

### How to Fix

Check the attach error:
```bash
kubectl describe pod <pod-name> | grep -A5 "FailedAttachVolume"
```

Check volume status in cloud provider:
```bash
# AWS
aws ec2 describe-volumes --volume-ids <vol-id>
# GCP
gcloud compute disks describe <disk-name>
```

### Examples

```bash
# Check for volume multi-attach
kubectl describe pod my-app | grep -i "FailedAttachVolume"
#  Volume is already exclusively attached to another node

# Force detach in AWS
aws ec2 detach-volume --volume-id vol-12345678 --force
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})