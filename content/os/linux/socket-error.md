---
title: "[Solution] Linux: socket-error — socket error"
description: "Fix Linux socket-error errors. socket error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: Socket Error

Socket errors occur when applications fail to create, bind, connect, or communicate through network sockets.

## Common Causes

- Socket file descriptor limit reached (EMFILE)
- Socket address family not supported (EAFNOSUPPORT)
- Protocol not supported (EPROTONOSUPPORT)
- Socket buffer size too small for the operation
- UNIX socket file path too long or permissions wrong

## How to Fix

### 1. Check Socket Limits

```bash
# Check file descriptor limits
ulimit -n
cat /proc/sys/fs/file-max
```

### 2. Check Socket Statistics

```bash
ss -s
```

### 3. Check UNIX Socket Permissions

```bash
ls -la /var/run/*.sock
ls -la /tmp/*.sock
```

### 4. Increase File Descriptor Limit

```bash
ulimit -n 65535
# Or system-wide
echo "fs.file-max = 2097152" | sudo tee -a /etc/sysctl.conf
```

## Examples

```bash
$ ss -s
Total: 345 (kernel 456)
TCP:   98 (estab 45, closed 35, orphaned 0, synrecv 0, timewait 35/0), ports 0

Transport Total     IP        IPv6
*	  456       -         -
RAW	  0         0         0
UDP	  12        8         4
TCP	  63        45        18
INET	  75        53        22
FRAG	  0         0         0
```
