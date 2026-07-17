---
title: "systemd Socket Activation Error"
description: "systemd socket-activated service fails to start due to socket issues."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# systemd Socket Activation Error

A systemd socket activation error occurs when a socket-activated service fails to start because the socket was not properly configured or created by systemd.

## Common Causes

- Socket unit file missing or misconfigured
- Port already in use by another service
- Socket file permissions incorrect
- Service not properly linked to socket

## How to Fix

### Check Socket Unit

```bash
systemctl status <service-name>.socket
systemctl cat <service-name>.socket
```

### Verify Socket Configuration

```ini
# /etc/systemd/system/myapp.socket
[Unit]
Description=My App Socket

[Socket]
ListenStream=8080
Accept=no

[Install]
WantedBy=sockets.target
```

### Check Port Availability

```bash
ss -tlnp | grep 8080
# Ensure the port is not in use
```

### Enable and Start Socket

```bash
sudo systemctl enable myapp.socket
sudo systemctl start myapp.socket
```

### Link Service to Socket

```ini
# Service must accept file descriptors from socket
[Service]
ExecStart=/usr/bin/myapp
# The service reads from stdin (fd 3) provided by systemd
```

### Debug Socket Activation

```bash
systemd-analyze verify myapp.socket
systemd-analyze verify myapp.service
```

## Examples

```bash
systemctl status myapp.socket
myapp.socket: Failed with result 'resources'.

# Fix: ensure port is not in use
ss -tlnp | grep 8080
# If port in use, stop the conflicting service
```

## Related Errors

- [Unit Start Failed]({{< relref "/tools/systemd/systemd-unit-error" >}}) — service start failure
- [Service Not Found]({{< relref "/tools/systemd/service-failed" >}}) — service does not exist
