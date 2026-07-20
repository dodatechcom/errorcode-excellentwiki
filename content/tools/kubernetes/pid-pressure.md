---
title: "[Solution] PIDPressure"
description: "Fix Kubernetes PIDPressure node condition. Resolve nodes under PID usage pressure affecting pod scheduling."
tools: ["kubernetes"]
error-types: ["scheduling-error", "pod-error"]
severities: ["error"]
---

## PIDPressure

A node enters PIDPressure when the number of processes (PIDs) on the node exceeds the configured threshold (default 90% of kernel.pid_max, typically 32768).

### Common Causes

- Fork bomb or runaway process creation
- Pods running many parallel processes
- System processes consuming PIDs
- pid_max kernel parameter set too low

### How to Fix

SSH to the node and check PID usage:
```bash
cat /proc/sys/kernel/pid_max
ps aux | wc -l
```

Increase pid_max:
```bash
sudo sysctl -w kernel.pid_max=65536
```

### Examples

```bash
# Increase max PIDs
ssh <node> sudo sysctl -w kernel.pid_max=65536
# Make permanent:
echo 'kernel.pid_max=65536' | sudo tee -a /etc/sysctl.d/99-pid.conf
```

## Related Errors

- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})
- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})
- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})