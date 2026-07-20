---
title: "[Solution] Linux: wireguard-error — WireGuard VPN error"
description: "Fix Linux wireguard-error errors. WireGuard VPN error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: WireGuard Error

WireGuard errors occur when the secure VPN tunnel fails to establish or maintain connectivity.

## Common Causes

- WireGuard kernel module not loaded or not installed
- Interface configuration has incorrect keys or endpoints
- Firewall blocking UDP port on both sides
- Keepalive not configured for NAT traversal
- Peer endpoint IP changed (dynamic DNS not updated)

## How to Fix

### 1. Check WireGuard Status

```bash
sudo wg show
sudo wg show wg0
```

### 2. Check Interface State

```bash
ip link show wg0
ip addr show wg0
```

### 3. Check Kernel Module

```bash
lsmod | grep wireguard
sudo modprobe wireguard
sudo apt install wireguard
```

### 4. Restart WireGuard

```bash
sudo systemctl restart wg-quick@wg0
```

### 5. Check Firewall

```bash
# Ensure UDP port is open
sudo ufw allow 51820/udp
# Or firewalld
sudo firewall-cmd --add-port=51820/udp --permanent
```

## Examples

```bash
$ sudo wg show wg0
interface: wg0
  public key: abc123...
  private key: (hidden)
  listening port: 51820

peer: def456...
  endpoint: 203.0.113.1:51820
  allowed ips: 10.0.0.0/24
  latest handshake: 1 minute ago
  transfer: 123.45 MiB received, 67.89 MiB sent

$ sudo wg show wg0 | grep handshake
  latest handshake: 5 minutes ago
# If no handshake, peers cannot communicate
```
