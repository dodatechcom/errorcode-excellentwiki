---
title: "[Solution] Linux ENOPROTOOPT (errno 61) — Protocol Not Available Fix"
description: "Fix Linux ENOPROTOOPT (errno 61) Protocol not available error. Solutions for socket protocol option issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enoprotoopt", "socket", "errno-61", "protocol", "option"]
weight: 5
---

# Linux ENOPROTOOPT (errno 61) — Protocol Not Available

ENOPROTOOPT (errno 61) means the requested socket protocol option is not available. This error occurs when a program tries to set or get a socket option (using `setsockopt()` or `getsockopt()`) that is not supported by the underlying protocol. It is distinct from EOPNOTSUPP (errno 95) because ENOPROTOOPT specifically refers to protocol-level option unavailability.

## Common Causes

- Trying to use a socket option on a protocol that doesn't support it
- TCP-specific option used on a UDP socket
- Option not supported by the kernel version
- Attempting to use IPv6 options on an IPv4 socket

## How to Fix ENOPROTOOPT

### 1. Check Socket Type and Protocol

Verify which protocol the socket is using:

```bash
ss -tlnp
netstat -tlnp
```

### 2. Use Protocol-Appropriate Options

Ensure the option matches the socket protocol:

```bash
# TCP options (SOCK_STREAM)
setsockopt(sock, IPPROTO_TCP, TCP_NODELAY, ...)

# UDP options (SOCK_DGRAM)
setsockopt(sock, IPPROTO_UDP, UDP_CORK, ...)
```

### 3. Check Kernel Support for the Option

Verify the kernel supports the option:

```bash
man socket | grep -A5 "setsockopt"
```

### 4. Upgrade the Kernel

If the option is new, upgrade to a kernel that supports it:

```bash
sudo apt update
sudo apt install linux-generic-hwe-22.04
```

## Verification

After fixing the option, confirm it works:

```bash
strace -e trace=setsockopt ./program
```

## Related Error Codes

- [EOPNOTSUPP (errno 95)](/os/linux/errno-95/) — Operation not supported
- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [ENOPROTOOPT (errno 61)](/os/linux/errno-61/) — Protocol not available
