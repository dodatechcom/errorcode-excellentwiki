---
title: "[Solution] CronJob missed its schedule"
description: "Fix Kubernetes CronJob 'missed schedule' errors. Resolve CronJobs that fail to create Jobs on time."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## CronJob Missed Schedule

This error occurs when the CronJob controller misses a scheduled run.

### Common Causes

- CronJob controller pod is not running or restarting
- Cluster was down during the scheduled time
- Controller is overloaded with too many CronJobs
- ConcurrencyPolicy is set to Forbid and previous job is still running

### How to Fix

Increase startingDeadlineSeconds:
```yaml
spec:
  startingDeadlineSeconds: 300
```

### Examples

```bash
# Check CronJob status
kubectl describe cronjob my-cronjob | grep -i "missed\|last schedule"

# Increase deadline
kubectl patch cronjob my-cronjob -p '{"spec":{"startingDeadlineSeconds":300}}'
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})