---
title: "[Solution] Linux ETIME (errno 47) — Stream ioctl Timeout Fix"
description: "Fix Linux ETIME (errno 47) Stream ioctl timeout error. Solutions for STREAMS ioctl timeout issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enTIME", "streams", "errno-47", "timeout"]
weight: 5
---

# Linux ETIME (errno 47) — Stream ioctl Timeout

ETIME (errno 47) means an `ioctl()` operation on a STREAMS device timed out. This error occurs when a STREAMS ioctl command does not complete within the expected time, often due to the underlying driver or module not responding. It is distinct from ETIMEDOUT (errno 110) because ETIME specifically refers to STREAMS ioctl timeouts.

## Common Causes

- The STREAMS driver or module is not responding to ioctl requests
- The device is in a busy or locked state
- Network STREAMS connections have timed out
- The ioctl command requires a response from a remote or slow device

## How to Fix ETIME

### 1. Check Device Status

Verify the STREAMS device is responsive:

```bash
ls -la /dev/streams/*
strconf < /dev/streams/<device>
```

### 2. Increase Timeout Values

Adjust STREAMS timeout settings if configurable:

```bash
sudo sysctl -w streams.timeout=30
```

### 3. Reset the Stream

Reset the stream to clear any stuck state:

```bash
close(fd);
fd = open("/dev/streams/<device>", O_RDWR);
```

### 4. Check Driver Load

Ensure the driver module is loaded and functioning:

```bash
lsmod | grep <driver_name>
dmesg | tail -20
```

## Verification

After addressing the timeout, confirm ioctl operations succeed:

```bash
strace -e trace=ioctl ./program 2>&1 | grep ETIME
```

## Related Error Codes

- [EBADMSG (errno 45)](/os/linux/errno-45/) — Not a STREAMS message
- [ETIMEDOUT (errno 110)](/os/linux/errno-110/) — Connection timed out
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
