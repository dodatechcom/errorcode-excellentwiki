---
title: "[Solution] Systemd Failed with Result 'dependency'"
description: "Fix systemd 'Failed with result dependency' error. Resolve service dependency chain failures."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Systemd Failed with Result 'dependency'

A dependency failure means the service could not start because a required dependency (another service, mount, or socket) failed or was not reached. Systemd stops the dependent service to prevent cascading issues.

## Common Causes

- A required `After=` or `Requires=` dependency service failed to start
- A required mount point is not available
- A socket unit the service depends on is not active
- The dependency service configuration is broken

## How to Fix

### Identify the Failed Dependency

```bash
systemctl status <service-name>
systemctl list-dependencies <service-name>
```

### Check Which Dependency Failed

```bash
systemctl list-units --state=failed
journalctl -u <dependency-service> -n 50
```

### Fix the Root Cause Dependency

```bash
# Check the dependency service status
sudo systemctl status <dependency-service>

# View its logs
journalctl -u <dependency-service> --no-pager -n 100

# Fix configuration and restart
sudo systemctl restart <dependency-service>
```

### Adjust Unit File Dependencies

```ini
[Unit]
Description=My Application
Requires=postgresql.service
After=postgresql.service network.target

[Service]
ExecStart=/usr/bin/my-app
```

### Restart the Full Dependency Chain

```bash
sudo systemctl restart <dependency-service>
sudo systemctl restart <service-name>
```

## Examples

```bash
# PostgreSQL dependency failed, app cannot start
sudo systemctl status my-app
# my-app.service: Failed with result 'dependency'
sudo systemctl status postgresql
# postgresql.service: inactive (dead)
# Fix: sudo systemctl start postgresql && sudo systemctl start my-app

# Broken mount dependency
# my-app.service: Failed with result 'dependency'
mount | grep /data
# /data not mounted
# Fix: mount /dev/sdb1 /data && systemctl start my-app
```

## Related Errors

- [Service Failed]({{< relref "/tools/systemd/service-failed" >}}) — direct service failure (not dependency)
- [Timeout Start]({{< relref "/tools/systemd/timeout-start" >}}) — service startup timed out
