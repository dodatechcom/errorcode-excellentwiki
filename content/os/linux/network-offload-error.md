---
title: "[Solution] Linux: network-offload-error -- TSO GRO offload failure"
description: "Fix Linux network offload errors. TCP segmentation or generic receive offload failure."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network Offload Error

Network offload failures occur when NIC or driver cannot handle TSO, LRO, or GRO.

## Common Causes

- NIC driver does not support requested offload feature
- Virtual switch not forwarding offloaded packets
- Firmware bug in NIC preventing segmentation
- Conflicting offload settings between host and VM
- Kernel module loading incorrect NIC driver

## How to Fix

### 1. Check Offload Status

```bash
ethtool -k eth0 | grep -E "offload|segmentation|large-receive|generic-receive"
```

### 2. Disable Problematic Offloads

```bash
sudo ethtool -K eth0 tso off
sudo ethtool -K eth0 gro off
sudo ethtool -K eth0 lro off
```

### 3. Make Persistent

```bash
sudo tee /etc/networkd-dispatcher/routable.d/50-tune.sh << EOF
#!/bin/bash
ethtool -K eth0 tso off gro off lro off
EOF
sudo chmod +x /etc/networkd-dispatcher/routable.d/50-tune.sh
```

## Examples

```bash
$ ethtool -k eth0 | grep tso
tcp-segmentation-offload: on
$ sudo ethtool -K eth0 tso off
$ ethtool -k eth0 | grep tso
tcp-segmentation-offload: off
```
