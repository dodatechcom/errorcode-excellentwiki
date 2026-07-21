---
title: "Systemd Socket Activation Port Error"
description: "Service fails to start because socket port is already in use"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd Socket Activation Port Error

Service fails to start because socket port is already in use

## Common Causes

- Another instance of the service already running
- Previous service instance did not shut down cleanly
- Different service bound to same port
- SO_REUSEPORT not enabled for socket

## How to Fix

1. Check what's using the port: `sudo ss -tlnp | grep :<port>`
2. Stop the conflicting service
3. Kill lingering processes: `sudo fuser -k <port>/tcp`
4. Configure socket with ReusePort=yes if needed

## Examples

```bash
# Find process using port 8080
sudo ss -tlnp | grep :8080

# Kill process on port
sudo fuser -k 8080/tcp

# Check for zombie service instances
systemctl list-units --state=failed
```
