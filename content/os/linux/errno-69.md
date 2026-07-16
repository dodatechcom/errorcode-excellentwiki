---
title: "[Solution] Linux ENOBUFS (errno 69) — No Buffer Space Available Fix"
description: "Fix Linux ENOBUFS (errno 69) No buffer space available error. Solutions for socket and network buffer issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enobufs", "buffer", "errno-69", "socket", "memory"]
weight: 5
---

# Linux ENOBUFS (errno 69) — No Buffer Space Available

ENOBUFS (errno 69) means there is no buffer space available for the requested operation. This error occurs when the kernel cannot allocate memory for network or socket buffers, typically during high network traffic or when the system is under memory pressure. It is distinct from ENOMEM (errno 12) because ENOBUFS specifically refers to I/O buffer allocation failure.

## Common Causes

- System is under heavy memory pressure
- Network interface receive or transmit queues are full
- Socket buffer size limits are too low
- High network traffic overwhelming the system

## How to Fix ENOBUFS

### 1. Check Current Buffer Usage

Monitor network buffer usage:

```bash
cat /proc/net/softnet_stat
netstat -s | grep -i buffer
```

### 2. Increase Network Buffer Sizes

Raise the kernel network buffer limits:

```bash
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216
sudo sysctl -w net.core.netdev_max_backlog=5000
```

### 3. Increase Socket Backlog

Allow more pending connections:

```bash
sudo sysctl -w net.core.somaxconn=65535
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=65535
```

### 4. Free Memory

Reduce memory pressure:

```bash
free -h
sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches
```

### 5. Check for Memory Leaks

Find processes using excessive memory:

```bash
ps aux --sort=-%mem | head -20
```

## Verification

After increasing buffer limits, confirm operations succeed:

```bash
cat /proc/net/softnet_stat
ss -t state established | wc -l
```

## Related Error Codes

- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
- [EAGAIN (errno 11)](/os/linux/errno-11/) — Resource temporarily unavailable
- [ECONNRESET (errno 68)](/os/linux/errno-68/) — Connection reset by peer
