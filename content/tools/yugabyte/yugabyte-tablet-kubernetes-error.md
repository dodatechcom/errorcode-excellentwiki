---
title: "[Solution] YugabyteDB Tablet Kubernetes Error"
description: "How to fix YugabyteDB tablet Kubernetes errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Pod not scheduled
- Pod in CrashLoopBackOff
- PersistentVolumeClaim not bound

## How to Fix

```bash
kubectl get pods -l app=yb-tserver
```

## Examples

```bash
kubectl describe pod yb-tserver-0
```
