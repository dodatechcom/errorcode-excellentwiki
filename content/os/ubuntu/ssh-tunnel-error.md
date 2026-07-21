---
title: "SSH Tunnel Forwarding Error"
description: "SSH local or remote port forwarding fails to establish"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Tunnel Forwarding Error

SSH local or remote port forwarding fails to establish

## Common Causes

- Forwarding ports already in use on local or remote side
- AllowTcpForwarding disabled in sshd_config
- SSH session disconnected before tunnel established
- GatewayPorts directive preventing remote binding

## How to Fix

1. Test forwarding: `ssh -L 8080:localhost:80 user@host`
2. Check sshd config: `sshd -T | grep forwarding`
3. Enable AllowTcpForwarding: `AllowTcpForwarding yes` in sshd_config
4. Use `-N` flag to prevent shell: `ssh -N -L 8080:localhost:80 user@host`

## Examples

```bash
# Create local port forward
ssh -N -L 8080:localhost:80 user@remote-host

# Create remote port forward
ssh -N -R 9090:localhost:3000 user@remote-host

# Check forwarding is enabled
sudo sshd -T | grep -i forwarding
```
