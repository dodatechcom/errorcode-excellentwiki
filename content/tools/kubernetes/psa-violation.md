---
title: "[Solution] Pod Security Admission violation"
description: "Fix Kubernetes Pod Security Admission (PSA) violations. Resolve pod creation failures due to pod security standards."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Pod Security Admission Violation

`Error: pod <name> violates PodSecurity "<profile>:<version>" - <violation>`

This error occurs when a pod does not meet the Pod Security Standards enforced by Pod Security Admission in the namespace.

### Common Causes

- Container runs as root (requires `restricted` profile)
- Privileged containers not allowed
- Host network or host PID access not allowed
- HostPath volumes not allowed
- Capabilities not allowed (NET_ADMIN, SYS_ADMIN)

### How to Fix

Check the namespace's PSA labels:
```bash
kubectl get ns <namespace> -o yaml | grep pod-security
```

Apply the correct security context to the pod:
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 3000
  seccompProfile:
    type: RuntimeDefault
  capabilities:
    drop: ["ALL"]
```

Relax the namespace policy:
```bash
kubectl label ns <namespace> pod-security.kubernetes.io/enforce=baseline
```

### Examples

```bash
# Check namespace PSA level
kubectl get ns my-ns -o yaml | grep -i "pod-security"
# pod-security.kubernetes.io/enforce: restricted

# Fix: add security context to pod
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"securityContext":{"runAsNonRoot":true,"seccompProfile":{"type":"RuntimeDefault"}}}}}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})