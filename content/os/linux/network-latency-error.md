---
title: "[Solution] Linux: network-latency-error — network latency error"
description: "Fix Linux network-latency-error errors. network latency error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: Network Latency Error

High network latency errors occur when network round-trip times exceed acceptable thresholds, causing timeouts and poor performance.

## Common Causes

- Network congestion on the local link or WAN
- High CPU load on routers or firewalls causing queuing delays
- Bufferbloat in network equipment
- Wireless interference causing retransmissions
- Oversubscribed upstream bandwidth

## How to Fix

### 1. Measure Latency

```bash
# Continuous ping to measure
ping -c 100 google.com | tail -5

# MTR shows latency per hop
mtr -n google.com
```

### 2. Check for Packet Loss

```bash
ping -c 100 -i 0.1 google.com | grep -E "loss|time"
```

### 3. Check Local Network

```bash
# Check link speed and duplex
sudo ethtool eth0

# Check for errors on interface
ip -s link show eth0
```

### 4. Apply Traffic Shaping (if bufferbloat)

```bash
# Use tc (traffic control) to limit bandwidth
sudo tc qdisc replace dev eth0 root fq_codel
```

## Examples

```bash
$ ping -c 10 google.com
PING google.com (142.250.80.46) 56(84) bytes of data.
64 bytes from 142.250.80.46: icmp_seq=1 ttl=117 time=345 ms
64 bytes from 142.250.80.46: icmp_seq=2 ttl=117 time=456 ms
64 bytes from 142.250.80.46: icmp_seq=3 ttl=117 time=234 ms
--- google.com ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9000ms
rtt min/avg/max/mdev = 234/345/456/78.9 ms

$ sudo ethtool eth0 | grep -E "Speed|Duplex"
        Speed: 100Mb/s
        Duplex: Half
```
