---
title: "[Solution] Container restart policy error"
description: "Fix Kubernetes container restart policy issues. Resolve pods that restart unexpectedly or not at all."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Container Restart Policy

Kubernetes uses the pod's `restartPolicy` to determine when to restart containers. Misconfiguration can cause unexpected behavior.

### Restart Policies

- `Always` (default for Deployments): always restart
- `OnFailure`: restart only on non-zero exit codes
- `Never`: never restart (used for Jobs)

### Common Causes

- restartPolicy set to Never for a deployment (stuck in Terminating)
- restartPolicy set to Always for a Job (never completes)
- Exit code 0 with Always policy causes unnecessary restart
- Sidecar containers with Always policy restarting the pod
- Pod marked as Failed even though container completed

### How to Fix

Check restart policy:
```bash
kubectl get pod <name> -o jsonpath='{.spec.restartPolicy}'
```

Update the restart policy:
```bash
kubectl patch deployment <name> -p '{"spec":{"template":{"spec":{"restartPolicy":"Always"}}}}'
```

### Examples

```bash
# Check pod restart policy
kubectl get pod my-job-xxx -o jsonpath='{.spec.restartPolicy}'

# For Jobs, use OnFailure or Never
# For Deployments, Always must be used
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})