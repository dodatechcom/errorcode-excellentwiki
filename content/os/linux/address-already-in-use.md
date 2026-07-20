---
title: "[Solution] Linux: address-already-in-use — address already in use error"
description: "Fix Linux address-already-in-use errors. address already in use error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 6
---

# Linux: Address Already In Use Error

The address already in use error occurs when a program tries to bind to a port or address that is already occupied.

## Common Causes

- Another process is already listening on the port
- Previous process did not release the port (TIME_WAIT state)
- Socket option SO_REUSEADDR not set
- Port reserved for privileged use only
- Binding to wrong IP address

## How to Fix

### 1. Identify the Process Using the Port

```bash
sudo ss -tlnp | grep <port>
sudo lsof -i :<port>
```

### 2. Check Process Details

```bash
ps aux | grep <pid>
```

### 3. Kill the Conflicting Process

```bash
sudo kill <pid>
# Or force kill
sudo kill -9 <pid>
```

### 4. Use SO_REUSEADDR

```bash
# For socket programming
setsockopt(socket, SOL_SOCKET, SO_REUSEADDR, 1)
# For systemd services, add to service file:
# Restart=always
```

## Examples

```bash
$ sudo ss -tlnp | grep :8080
LISTEN 0 128 0.0.0.0:8080 0.0.0.0:* users:(("java",pid=12345,fd=12))
$ ps aux | grep 12345
user  12345  0.5  2.0  ... java -jar myapp.jar
$ sudo kill 12345
$ sudo ss -tlnp | grep :8080
# Port now free
```
