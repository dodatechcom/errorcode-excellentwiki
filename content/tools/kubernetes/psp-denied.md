---
title: "[Solution] PodSecurityPolicy denied (deprecated in 1.25)"
description: "Fix Kubernetes PodSecurityPolicy denied error (deprecated). Resolve pod creation failures blocked by PSP rules (replaced by Pod Security Admission)."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## PodSecurityPolicy Denied (Deprecated)

`pod "<name>" is forbidden: unable to validate against any pod security policy: <reason>`

This error occurs when no PodSecurityPolicy (PSP, deprecated in 1.25) allows the pod's security context. PSP has been replaced by Pod Security Admission.

### Common Causes

- No PSP is defined in the cluster
- Pod requires privileged access but no PSP allows it
- Pod uses host network, hostPID, or hostIPC
- Pod runs as root without allowPrivilegeEscalation: false

### How to Fix

Create a permissive PSP (if still using PSP):
```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: permissive
spec:
  privileged: true
  seLinux:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  volumes:
  - '*'
```

### Examples

```bash
# List existing PSPs
kubectl get psp
# No resources found

# Create permissive PSP
kubectl apply -f permissive-psp.yaml
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})