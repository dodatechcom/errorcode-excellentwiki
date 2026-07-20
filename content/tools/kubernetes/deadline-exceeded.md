---
title: "[Solution] DeadlineExceeded (Job)"
description: "Fix Kubernetes Job DeadlineExceeded error. Resolve jobs that exceed their activeDeadlineSeconds limit and are terminated."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## DeadlineExceeded (Job)

This error occurs when a Kubernetes Job runs longer than the configured `activeDeadlineSeconds` limit. Kubernetes terminates the job and marks it as failed.

### Common Causes

- Job takes longer to complete than expected
- activeDeadlineSeconds is set too low
- Worker pods are stuck or hanging
- BackoffLimit exceeded for retries
- Dependent services are slow or unavailable

### How to Fix

Check job status:
```bash
kubectl describe job <job-name>
```

View logs of the failed pod:
```bash
kubectl logs job/<job-name>
```

Increase the deadline:
```yaml
spec:
  activeDeadlineSeconds: 3600
```

### Examples

```bash
# Delete and recreate job with longer deadline
kubectl delete job <job-name>
kubectl create job <job-name> --image=myapp
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})