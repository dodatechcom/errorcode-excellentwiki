---
title: "[Solution] CSI driver not installed"
description: "Fix Kubernetes CSI driver not installed errors. Resolve volume provisioning failures when the Container Storage Interface driver is missing."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CSI Driver Not Installed

`failed to get CSI driver: rpc error: code = Unimplemented`

This error occurs when a CSI driver is not installed or not registered on the node where the volume needs to be mounted.

### Common Causes

- CSI driver (EBS CSI, GCE PD CSI, etc.) not installed
- CSI driver pods are not running
- CSI node driver is not registered on the specific node
- Old Kubernetes version without CSI support
- Invalid CSIDriver object

### How to Fix

List installed CSI drivers:
```bash
kubectl get csidrivers
```

Check CSI driver pods:
```bash
kubectl get pods -n kube-system | grep csi
```

Install the CSI driver:
```bash
# EBS CSI driver
kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/"

# GCE PD CSI driver
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/master/deploy/kubernetes/overlays/stable/gcp-pd-csi-driver.yaml
```

### Examples

```bash
# Check CSI drivers
kubectl get csidrivers
# ebs.csi.aws.com

# Check CSI node status
kubectl get csinodes
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})