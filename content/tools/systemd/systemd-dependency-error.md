---
title: "systemd Dependency Failed"
description: "systemd service fails because a required dependency failed to start."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# systemd Dependency Failed

A systemd dependency failure occurs when a service fails because one of its required dependencies failed to start. systemd manages service ordering and dependencies through unit file directives.

## Common Causes

- Required service is not running
- Required mount point is not available
- Network dependency not met
- Required socket not created

## How to Fix

### Check Service Dependencies

```bash
systemctl list-dependencies <service-name>
systemctl list-dependencies --all <service-name>
```

### View Service Tree

```bash
systemctl list-dependencies <service-name> --reverse
```

### Fix Dependency Chain

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target postgresql.service
Requires=postgresql.service
```

### Start Dependencies Manually

```bash
# Start required services first
sudo systemctl start postgresql
sudo systemctl start redis
# Then start the main service
sudo systemctl start myapp
```

### Check Failed Dependencies

```bash
systemctl --failed
# Shows all failed units
```

### Use Wants Instead of Requires

```ini
[Unit]
Wants=postgresql.service  # Won't fail if postgresql is missing
After=postgresql.service
```

### Override Dependency Behavior

```bash
# Create override
sudo systemctl edit myapp.service

# Add override
[Unit]
Wants=postgresql.service
After=postgresql.service
```

## Examples

```bash
systemctl start myapp
myapp.service: Job myapp.service/start failed with result 'dependency'.

# Check what failed
systemctl status postgresql.service
# postgresql.service: Active: failed
```

## Related Errors

- [Unit Start Failed]({{< relref "/tools/systemd/systemd-unit-error" >}}) — service start failure
- [Socket Error]({{< relref "/tools/systemd/systemd-socket-error" >}}) — socket activation error
