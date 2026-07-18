---
title: "[Solution] Systemd Job Timeout Exceeded Error — How to Fix"
description: "Fix systemd job timeout errors by increasing timeout values, optimizing service startup, resolving dependency bottlenecks, and debugging slow units"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Job Timeout Exceeded Error

This error means a systemd job (service start, stop, or restart) took longer than the configured timeout and was forcefully killed by systemd. The default timeout for most operations is 90 seconds.

## Why It Happens

- The service takes a long time to initialize (loading large datasets, warming caches)
- The service is stuck waiting for a network resource that is slow or unreachable
- A dependency is hanging and the service waits indefinitely for it
- The service is performing heavy I/O at startup
- `TimeoutStartSec` is set too low for the workload
- The service is deadlocked or blocked on a system call
- A mounted filesystem is slow or unresponsive

## Common Error Messages

```
A start job is running for myapp.service (30s / 90s)
systemd[1]: myapp.service: Start operation timed out. Terminating.
systemd[1]: myapp.service: Failed with result 'timeout'.
```

```
Job for myapp.service failed because a timeout was exceeded.
```

```
systemd[1]: myapp.service: Service entered dead state with result 'timeout'.
```

## How to Fix It

### 1. Check Which Job Is Timing Out

```bash
# See active jobs
systemctl list-jobs

# Check the specific service
systemctl status myapp.service

# View logs around the timeout
journalctl -u myapp.service --since "5 minutes ago" --no-pager
```

### 2. Increase the Timeout

```bash
# In /etc/systemd/system/myapp.service
[Service]
ExecStart=/usr/bin/myapp
TimeoutStartSec=300  # 5 minutes instead of default 90s

# For stop timeout (service takes time to drain connections)
TimeoutStopSec=120

# Reload the unit file
sudo systemctl daemon-reload
sudo systemctl restart myapp
```

### 3. Optimize Service Startup

```bash
# Profile startup time
systemd-analyze time myapp.service

# Show which services are slowest
systemd-analyze blame | head -20

# Show critical chain (longest path through dependencies)
systemd-analyze critical-chain myapp.service
```

### 4. Use Type=notify for Long-Starting Services

```ini
# If your application supports sd_notify
[Service]
Type=notify
ExecStart=/usr/bin/myapp
NotifyAccess=main

# The application must call sd_notify(0, "READY=1") when ready
```

### 5. Add Watchdog Support

```ini
[Service]
Type=notify
WatchdogSec=30
Restart=on-failure
RestartSec=10

# The application must periodically call sd_notify(0, "WATCHDOG=1")
```

### 6. Debug Slow Dependencies

```bash
# Check what the service depends on
systemctl list-dependencies myapp.service

# Check if a dependency is slow
systemd-analyze blame | grep -E "network|postgresql|redis"

# Start dependencies manually first
sudo systemctl start postgresql redis
sudo systemctl start myapp
```

## Common Scenarios

- **Application loading large model**: A machine learning service takes 5 minutes to load a model into memory. Increase `TimeoutStartSec` to 600 and use `Type=notify` so systemd knows when the service is ready.
- **Database migration on startup**: A web app runs migrations before accepting traffic. Move migrations to a separate systemd unit that runs before the app.
- **Slow NFS mount**: The service depends on an NFS mount that takes 30 seconds to connect. Add `After=remote-fs.target` and increase timeout.

## Prevent It

- Use `systemd-analyze blame` regularly to identify slow-starting services
- Configure `Type=notify` instead of `Type=simple` so systemd only marks the service ready when it actually is
- Set explicit `TimeoutStartSec` values per service based on measured startup times

## Related Pages

- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Dependency Cycle](/tools/systemd/systemd-dependency-cycle)
- [Systemd Mount Error](/tools/systemd/systemd-mount-error)
