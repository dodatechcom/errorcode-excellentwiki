---
title: "[Solution] Docker Network Bridge Error — Failed to Create Bridge"
description: "Fix Docker network bridge errors on Linux. Resolve bridge creation failures, subnet conflicts, and network driver issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["docker", "network", "bridge", "docker0", "iptables", "subnet"]
weight: 5
---

# Docker Network Bridge Error — Failed to Create Bridge

A Docker network bridge error occurs when the Docker daemon cannot create or configure the network bridge (`docker0`). The error reads:

> "could not find bridge docker0: No such device"

Or:

> "failed to set up sandbox after jumpstart: path wait cancelled"

## What This Error Means

Docker uses a Linux bridge (`docker0` by default) to provide container networking. Each container gets a virtual ethernet pair connected to this bridge. If the bridge interface is missing, misconfigured, or has conflicting IP settings, containers cannot start and Docker reports a network error.

## Common Causes

- `docker0` bridge was manually deleted or removed by a script
- IP subnet conflict with host network
- `net.bridge.bridge-nf-call-iptables` kernel parameter not set
- iptables rules corrupted or conflicting
- Docker daemon configuration has incorrect bridge settings
- NetworkManager interfering with Docker bridge

## How to Fix

### Restart Docker and Recreate Bridge

```bash
# Stop Docker
sudo systemctl stop docker

# Delete broken bridge
sudo ip link set docker0 down
sudo ip link delete docker0

# Start Docker (will recreate docker0)
sudo systemctl start docker
```

### Verify Bridge Exists

```bash
ip link show docker0
brctl show docker0
```

### Configure Bridge Parameters

```bash
# Enable bridge-nf-call-iptables
echo "net.bridge.bridge-nf-call-iptables = 1" | sudo tee -a /etc/sysctl.conf
echo "net.bridge.bridge-nf-call-ip6tables = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### Disable NetworkManager Interference

```bash
# Check if NetworkManager is managing docker0
nmcli device status | grep docker0

# Remove docker0 from NetworkManager management
sudo nmcli device set docker0 managed no

# Or add to /etc/NetworkManager/NetworkManager.conf
# [keyfile]
# unmanaged-devices=interface-name:docker0
```

### Configure Custom Bridge in Docker Daemon

```json
// /etc/docker/daemon.json
{
  "bip": "192.168.100.1/24",
  "fixed-cidr": "192.168.100.0/25",
  "mtu": 1500,
  "default-gateway": "192.168.100.1",
  "dns": ["8.8.8.8", "8.8.4.4"]
}
```

Then restart Docker:

```bash
sudo systemctl restart docker
```

### Flush and Rebuild iptables

```bash
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo systemctl restart docker
```

## Related Errors

- [Docker Compose Network Error]({{< relref "/os/linux/linux-docker-compose-error" >}}) — docker-compose network creation failures
- [Docker Socket Permission Denied]({{< relref "/os/linux/linux-docker-socket-permission" >}}) — Docker daemon access issues
- [iptables Error]({{< relref "/os/linux/linux-iptables-error" >}}) — iptables firewall errors
