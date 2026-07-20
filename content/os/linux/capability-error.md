---
title: "[Solution] Linux: capability-error — Linux capability error"
description: "Fix Linux capability-error errors. Linux capability error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---
# Linux: Capability Error

Linux capability errors occur when a process lacks the required capabilities (fine-grained privileges) to perform an operation.

## Common Causes

- Application needs but doesn't have CAP_NET_BIND_SERVICE to bind to ports <1024
- File capabilities removed or not set correctly on the binary
- Container running with restricted capabilities (Docker's --cap-drop)
- Systemd service unit restricts capabilities
- Kernel capability bounding set prevents acquiring specific caps

## How to Fix

### 1. Check Process Capabilities

```bash
# Check capabilities of a running process
cat /proc/<pid>/status | grep Cap
# Decode capabilities
capsh --decode=$(grep CapEff /proc/<pid>/status | awk '{print $2}')
```

### 2. Set File Capabilities

```bash
# Grant capability to bind to privileged ports
sudo setcap cap_net_bind_service=+ep /usr/bin/myapp

# View file capabilities
getcap /usr/bin/myapp
```

### 3. Add Capabilities to Systemd Service

```bash
# Edit service unit
sudo systemctl edit myapp
# Add:
# [Service]
# CapabilityBoundingSet=CAP_NET_BIND_SERVICE
# AmbientCapabilities=CAP_NET_BIND_SERVICE
```

## Examples

```bash
$ getcap /usr/bin/python3
/usr/bin/python3 = cap_net_bind_service+ep

$ sudo setcap cap_net_raw+ep /usr/bin/tcpdump
$ getcap /usr/bin/tcpdump
/usr/bin/tcpdump = cap_net_raw+ep

$ capsh --decode=0000000000000400
0x0000000000000400=cap_net_bind_service
```
