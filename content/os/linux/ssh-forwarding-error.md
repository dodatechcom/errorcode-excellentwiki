---
title: "[Solution] Linux: ssh-forwarding-error -- SSH forwarding failure"
description: "Fix Linux SSH forwarding errors. SSH port forwarding or tunnel creation failure."
os: ["linux"]
error-types: ["ssh-error"]
severities: ["error"]
---

# Linux: SSH Forwarding Error

SSH forwarding errors occur when port forwarding tunnels fail to establish.

## Common Causes

- GatewayPorts not enabled for remote forwarding
- Target port already in use locally
- PermitOpen restricting destination hosts
- Firewall blocking forwarded port
- Agent forwarding not enabled on server

## How to Fix

### 1. Check Forwarding Config

```bash
sshd -T | grep -E "gateway|permitopen|allowtcp"
ss -tlnp | grep <port>
```

### 2. Fix SSH Server Config

```bash
# /etc/ssh/sshd_config
GatewayPorts yes
AllowTcpForwarding yes
PermitOpen any
sudo systemctl restart sshd
```

### 3. Test Forwarding

```bash
ssh -L 8080:localhost:80 user@remote
ssh -R 9090:localhost:3000 user@remote
ssh -D 1080 user@remote
```

## Examples

```bash
$ ssh -L 8080:localhost:80 user@remote
Warning: remote port forwarding failed for listen address 127.0.0.1
$ ssh -vv user@remote 2>&1 | grep forwarding
debug1: Remote: Forwarding listen address "127.0.0.1" port 8080
```
