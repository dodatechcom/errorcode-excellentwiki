---
title: "[Solution] Kubernetes Job failed — Backoff limit exceeded"
description: "Fix Kubernetes Job failed with backoff limit exceeded. Learn why jobs fail and how to configure retry policies."
tools: ["kubernetes"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["job", "batch", "backoff-limit", "failed", "retry"]
weight: 5
---

# Kubernetes Job failed — Backoff limit exceeded

A Job fails when the number of pod failures reaches the configured `backoffLimit`. Kubernetes stops retrying and marks the Job as failed. By default, the backoff limit is 6.

## Common Causes

- Application error causing non-zero exit code
- Insufficient resources preventing pod scheduling
- Missing ConfigMap, Secret, or volume mount
- Job configuration error (wrong command or arguments)

## How to Fix

### Check Job Status and Pod Logs

```bash
kubectl get jobs
kubectl describe job <job-name>
kubectl logs job/<job-name>
```

### View Failed Pod Events

```bash
kubectl get pods --job-name=<job-name> --field-selector=status.phase=Failed
kubectl logs <failed-pod-name> --previous
```

### Increase Backoff Limit for Flaky Jobs

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: my-job
spec:
  backoffLimit: 10
  template:
    spec:
      containers:
        - name: worker
          image: my-worker:latest
      restartPolicy: Never
```

### Set Active Deadline Seconds

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: my-job
spec:
  activeDeadlineSeconds: 600
  backoffLimit: 5
```

## Examples

```bash
# Example 1: Check why job failed
kubectl describe job data-migration
# Events: Job has reached the specified backoff limit
kubectl logs job/data-migration
# Error: connection refused to database at db:5432
# Fix: ensure database is running before job starts

# Example 2: Job with wrong command
kubectl get pods --job-name=batch-job -o yaml | grep -A 5 command
# command: ["python", "run.py"]
# Fix: verify the script name and path

# Example 3: Insufficient resources
kubectl describe pod <job-pod>
# Events: Insufficient cpu
# Fix: increase resource requests or add nodes
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloop-debug" >}}) — pod crashing during execution
- [OOMKilled]({{< relref "/tools/kubernetes/oomkilled" >}}) — container exceeded memory limit
- [Pod Evicted]({{< relref "/tools/kubernetes/pod-evicted" >}}) — pod evicted due to node pressure
