---
title: "[Solution] kubectl unknown command"
description: "Fix 'kubectl unknown command' error. Resolve kubectl command syntax and spelling errors."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## Unknown Command

`Error: unknown command "<command>" for "kubectl"`

This error occurs when kubectl does not recognize the command you typed. The command may be misspelled or does not exist.

### Common Causes

- Typo in the command name
- Wrong command syntax (e.g., `kubectl pod` instead of `kubectl get pod`)
- Using a kubectl version that does not support the command

### How to Fix

Check available commands:
```bash
kubectl --help
kubectl <verb> --help
```

Use the correct syntax:
```bash
kubectl get pods         # correct
kubectl describe pod     # correct
kubectl pod get          # wrong
```

### Examples

```bash
# Common mistake: wrong order
kubectl pod get my-pod     # error: unknown command
kubectl get pod my-pod     # correct
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})