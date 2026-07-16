---
title: "[Solution] Linux ENOSR (errno 48) — No STREAMS Buffers Available Fix"
description: "Fix Linux ENOSR (errno 48) No STREAMS buffers available error. Solutions for STREAMS buffer exhaustion."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enOSR", "streams", "errno-48", "buffers"]
weight: 5
---

# Linux ENOSR (errno 48) — No STREAMS Buffers Available

ENOSR (errno 48) means the system cannot allocate STREAMS message buffers. This error occurs when `getmsg()` or `getpmsg()` is called but the kernel has exhausted its pool of STREAMS message buffers. It is distinct from ENOMEM (errno 12) because ENOSR specifically refers to STREAMS buffer allocation.

## Common Causes

- The STREAMS buffer pool is exhausted due to high message volume
- Memory pressure prevents allocation of new STREAMS buffers
- A process is consuming STREAMS buffers without releasing them
- The STREAMS buffer configuration is too low for the workload

## How to Fix ENOSR

### 1. Check STREAMS Buffer Usage

Monitor STREAMS buffer allocation:

```bash
cat /proc/streams/buffer_stats
strconf < /dev/streams/null
```

### 2. Increase STREAMS Buffer Limits

Adjust kernel parameters for STREAMS buffers:

```bash
sudo sysctl -w streams buffers_max=8192
```

### 3. Free Consumed Buffers

Ensure processes are properly releasing STREAMS buffers:

```bash
# Identify processes with many open STREAMS
ls -la /proc/*/fd
```

### 4. Reduce Message Volume

If the application generates excessive STREAMS traffic, batch or reduce messages:

```c
// Instead of many small messages, use fewer larger ones
```

## Verification

After adjusting buffer limits, confirm buffers are available:

```bash
cat /proc/streams/buffer_stats
```

## Related Error Codes

- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
- [ERMSR (errno 44)](/os/linux/errno-44/) — No STREAMS resources
- [EAGAIN (errno 7)](/os/linux/errno-7/) — Resource temporarily unavailable
