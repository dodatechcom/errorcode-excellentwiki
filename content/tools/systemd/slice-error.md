---
title: "[Solution] Systemd Slice Error"
description: "Fix systemd slice errors. Resolve resource control and cgroup slice configuration issues."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["slice", "systemd", "cgroup", "resource-control", "memory"]
weight: 5
---

# Systemd Slice Error

A slice error occurs when a systemd unit cannot be placed in its specified cgroup slice, or the slice itself has invalid configuration. Slices control resource limits (CPU, memory, I/O) for groups of services.

## Common Causes

- The slice unit file is missing or has syntax errors
- The referenced slice does not exist
- Memory or CPU limits in the slice exceed system capabilities
- The slice hierarchy is too deep (exceeds cgroup depth limits)

## How to Fix

### Verify the Slice Exists

```bash
systemctl status my-app.slice
systemctl list-units --type=slice
```

### Create a Custom Slice

```ini
# /etc/systemd/system/my-app.slice
[Unit]
Description=Slice for My Application

[Slice]
MemoryMax=2G
CPUQuota=150%
TasksMax=512
```

### Assign a Service to the Slice

```ini
# /etc/systemd/system/my-app.service
[Unit]
Description=My Application

[Service]
Slice=my-app.slice
ExecStart=/usr/bin/my-app
```

### Reload and Restart

```bash
sudo systemctl daemon-reload
sudo systemctl restart my-app
```

### Check Slice Resource Usage

```bash
systemctl status my-app.slice
systemd-cgtop
```

## Examples

```bash
# Missing slice referenced by service
# my-app.service: Failed with result 'dependency'
# Fix: create my-app.slice or remove Slice= directive

# Memory limit too high for available resources
# my-app.slice: Failed to set memory limit
# Fix: reduce MemoryMax to a feasible value
```

## Related Errors

- [Failed Dependency]({{< relref "/tools/systemd/failed-dependency" >}}) — dependency chain failure
- [Permission Error]({{< relref "/tools/systemd/permission-error7" >}}) — insufficient capabilities
