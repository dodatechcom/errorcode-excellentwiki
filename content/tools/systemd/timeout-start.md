---
title: "[Solution] Systemd Startup Timeout Exceeded"
description: "Fix systemd startup timeout errors. Resolve services that take too long to initialize."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["timeout", "startup", "systemd", "watchdog", "deadline"]
weight: 5
---

# Systemd Startup Timeout Exceeded

Systemd kills the service process when it fails to signal readiness or complete startup within the configured timeout. The default `TimeoutStartSec` is 90 seconds.

## Common Causes

- The service takes longer than the configured `TimeoutStartSec` to start
- The service does not properly signal readiness via `Type=notify` or `ExecStartPost`
- The service is blocked on a resource (disk, network, database)
- A blocking dependency is stalling the startup sequence

## How to Fix

### Increase the Start Timeout

```ini
[Service]
TimeoutStartSec=300
```

### Set Timeout to Infinity (Use Sparingly)

```ini
[Service]
TimeoutStartSec=infinity
```

### Use Notify Type for Long-Starting Services

```ini
[Service]
Type=notify
ExecStart=/usr/bin/my-app --daemon
WatchdogSec=30
```

### Diagnose What Is Blocking Startup

```bash
journalctl -u <service-name> -n 100 --no-pager
systemd-analyze blame
systemd-analyze critical-chain <service-name>
```

### Add Watchdog Support

```c
// In your application code, send READY=1 when ready
sd_notify(0, "READY=1");
```

## Examples

```bash
# Service exceeded 90s startup timeout
# my-app.service: Startup operation timed out, killing
# Fix: set TimeoutStartSec=300 in unit file

# Service waiting on database that takes long to initialize
# my-app.service: Timed out starting
# Fix: add After=postgresql.service and increase TimeoutStartSec
```

## Related Errors

- [Service Failed]({{< relref "/tools/systemd/service-failed" >}}) — process exited with error code
- [Failed Dependency]({{< relref "/tools/systemd/failed-dependency" >}}) — dependency service failed
