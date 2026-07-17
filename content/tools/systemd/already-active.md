---
title: "[Solution] Systemd Unit is Already Active"
description: "Fix systemd 'unit is already active' error. Resolve duplicate service activation conflicts."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Systemd Unit is Already Active

This error occurs when you try to start a systemd unit that is already in an active state. Systemd prevents duplicate activation unless the unit is configured for it.

## Common Causes

- The service is already running and start was called again
- A timer or socket triggered the service while it was active
- The unit file lacks `RemainAfterExit=yes` for services that exit cleanly
- Multiple automation scripts are trying to start the same service

## How to Fix

### Check Current Unit Status

```bash
systemctl status <service-name>
```

### Use Restart Instead of Start

```bash
sudo systemctl restart <service-name>
```

### Check for Duplicate Triggers

```bash
systemctl list-timers --all
systemctl list-sockets --all
```

### Allow Repeated Activation with RemainAfterExit

```ini
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/my-setup-script
```

### Mask the Service If It Should Not Run

```bash
sudo systemctl mask <service-name>
```

## Examples

```bash
# Attempting to start an already running service
sudo systemctl start nginx
# Failed to start nginx: Unit nginx.service is already active.
# Fix: use systemctl restart nginx

# Timer triggered while service was active
# Fix: check timers with systemctl list-timers
```

## Related Errors

- [Not Found]({{< relref "/tools/systemd/not-found8" >}}) — unit does not exist
- [Reload Error]({{< relref "/tools/systemd/reload-error" >}}) — service failed to reload configuration
