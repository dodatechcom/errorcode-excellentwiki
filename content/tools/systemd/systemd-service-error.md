---
title: "systemd Service Not Found"
description: "systemd cannot find the specified service unit."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# systemd Service Not Found

A systemd service not found error occurs when systemctl cannot locate the specified service unit file. This means the service is not installed or the unit name is incorrect.

## Common Causes

- Service unit file not installed
- Typo in the service name
- Unit file is in a non-standard location
- systemd unit cache not refreshed

## How to Fix

### Check Available Services

```bash
systemctl list-units --type=service | grep <service-name>
```

### Search for Unit Files

```bash
find /etc/systemd /usr/lib/systemd /lib/systemd -name "*.service" 2>/dev/null
```

### Install the Service

```bash
# Copy unit file to correct location
sudo cp myapp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

### Fix Service Name

```bash
# Common mistakes
systemctl start nginx        # correct
systemctl start Nginx        # wrong (case-sensitive)
systemctl start nginx.service # also correct
```

### Check Service Loading

```bash
systemctl list-unit-files | grep <service-name>
```

### Reload Unit Cache

```bash
sudo systemctl daemon-reload
systemctl list-units --type=service --all
```

## Examples

```bash
systemctl start myapp
Failed to start myapp.service: Unit myapp.service not found.

# Fix:
find / -name "myapp.service" 2>/dev/null
# Install if not found
sudo cp myapp.service /etc/systemd/system/
sudo systemctl daemon-reload
```

## Related Errors

- [Unit Start Failed]({{< relref "/tools/systemd/systemd-unit-error" >}}) — service start failure
- [Dependency Failed]({{< relref "/tools/systemd/dependency-failed" >}}) — dependency issue
