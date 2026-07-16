---
title: "[Solution] Linux EBADMSG (errno 45) — Not a STREAMS Message Fix"
description: "Fix Linux EBADMSG (errno 45) Not a STREAMS message error. Solutions for STREAMS message format issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enBADMSG", "streams", "errno-45", "message"]
weight: 5
---

# Linux EBADMSG (errno 45) — Not a STREAMS Message

EBADMSG (errno 45) means the received message is not a valid STREAMS message. This error occurs when `getmsg()` or `getpmsg()` receives a message that does not conform to the expected STREAMS message format, or when the message priority band is invalid.

## Common Causes

- The message buffer is corrupted or not properly allocated
- A non-STREAMS file descriptor was used with `getmsg()` or `getpmsg()`
- The message was truncated or overwritten by another operation
- The message type or priority band is outside valid ranges

## How to Fix EBADMSG

### 1. Verify STREAMS File Descriptor

Ensure the file descriptor refers to a STREAMS device:

```bash
file /proc/self/fd/<fd_number>
strconf < /dev/streams/<device>
```

### 2. Properly Allocate Message Buffers

Use correct allocation for STREAMS messages:

```c
struct strbuf ctl, data;
ctl.maxlen = 256;
ctl.buf = malloc(256);
data.maxlen = 1024;
data.buf = malloc(1024);
```

### 3. Check Message Flags

Ensure proper flags are used with `getpmsg()`:

```c
int band;
int flags;
int ret = getpmsg(fd, &ctl, &data, &band, &flags);
if (ret < 0 && errno == EBADMSG) {
    fprintf(stderr, "Invalid STREAMS message\n");
}
```

### 4. Reset the Stream

Reset the stream to clear any corrupted state:

```bash
# Close and reopen the device
close(fd);
fd = open("/dev/streams/null", O_RDWR);
```

## Verification

After fixing message handling, confirm valid messages are received:

```bash
strace -e trace=recvmsg ./program 2>&1 | grep EBADMSG
```

## Related Error Codes

- [ENOSTR (errno 46)](/os/linux/errno-46/) — No stream head associated
- [ETIME (errno 47)](/os/linux/errno-47/) — Stream ioctl timeout
- [EAGAIN (errno 7)](/os/linux/errno-7/) — Resource temporarily unavailable
