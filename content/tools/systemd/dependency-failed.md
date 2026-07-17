---
title: "[Solution] Systemd Dependency Failed — Dependency failed for X.service"
description: "Fix systemd 'Dependency failed' errors. Resolve service startup ordering and dependency issues."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Systemd Dependency Failed — Dependency failed for X.service

This error means a service could not start because one of its required dependencies failed or was not available. Systemd enforces dependency ordering, so if a dependency in `Requires=` or `Wants=` fails, the dependent service is also stopped.

## Common Causes

- A required service (database, network, etc.) failed to start first
- Incorrect `After=` or `Requires=` directives in the unit file
- Network is not ready when service starts
- Dependency service is not installed on the system

## How to Fix

### Identify the Failed Dependency

```bash
systemctl status <service-name>
journalctl -u <service-name> -n 30
```

### Check Which Services Failed

```bash
systemctl --failed
```

### Fix the Underlying Service

```bash
systemctl status <dependency-service>
sudo systemctl start <dependency-service>
```

### Adjust Service Ordering

```ini
[Unit]
Description=My App
After=network-online.target postgresql.service
Wants=network-online.target
Requires=postgresql.service
```

### Ensure Services Start at Boot

```bash
sudo systemctl enable <dependency-service>
sudo systemctl enable <service-name>
```

### Add a Restart Policy

```ini
[Service]
Restart=on-failure
RestartSec=5s
```

## Examples

```bash
# Example 1: App depends on PostgreSQL
systemctl status my-app
# Dependency failed for My App
systemctl status postgresql
# postgresql.service: inactive (dead)
# Fix: sudo systemctl start postgresql

# Example 2: Fix boot ordering
systemctl --failed
# my-app.service   loaded failed
# Fix: add After= and Wants= to my-app.service unit file
sudo systemctl daemon-reload
sudo systemctl restart my-app
```

## Related Errors

- [Service Failed]({{< relref "/tools/systemd/service-failed" >}}) — service failed to start directly
- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crashloopbackoff" >}}) — Kubernetes pod crash loop
