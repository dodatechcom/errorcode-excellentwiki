---
title: "[Solution] Systemd Permission Denied"
description: "Fix systemd permission denied errors. Resolve access control and capability issues in service units."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["permission", "denied", "systemd", "user", "capability"]
weight: 5
---

# Systemd Permission Denied

A permission denied error occurs when the service process lacks the necessary file system permissions, user privileges, or Linux capabilities to perform an operation.

## Common Causes

- The service is running as a user that does not own the target files
- Required Linux capabilities are not granted in the unit file
- SELinux or AppArmor is blocking the operation
- The `DynamicUser` or `ProtectSystem` restrictions are too strict

## How to Fix

### Check Which User the Service Runs As

```ini
[Service]
User=www-data
Group=www-data
```

### Grant File Ownership

```bash
sudo chown -R www-data:www-data /var/lib/my-app
sudo chmod -R 750 /var/lib/my-app
```

### Add Required Capabilities

```ini
[Service]
AmbientCapabilities=CAP_NET_BIND_SERVICE CAP_DAC_READ_SEARCH
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
```

### Temporarily Relax Security Sandboxing

```ini
[Service]
ProtectSystem=false
ProtectHome=false
PrivateTmp=false
```

### Check SELinux Context

```bash
ls -Z /var/lib/my-app/
sudo setsebool -P httpd_can_network_connect 1
```

## Examples

```bash
# Service cannot bind to port 80 as non-root
# Permission denied
# Fix: add AmbientCapabilities=CAP_NET_BIND_SERVICE

# Service cannot write to /var/lib
# Permission denied: '/var/lib/my-app/data'
# Fix: chown -R myapp:myapp /var/lib/my-app
```

## Related Errors

- [Service Failed]({{< relref "/tools/systemd/service-failed" >}}) — process exited with error code
- [Core Dump]({{< relref "/tools/systemd/core-dump" >}}) — process crashed
