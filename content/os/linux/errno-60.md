---
title: "[Solution] Linux ENOTSOCK (errno 60) — Socket Operation on Non-Socket Fix"
description: "Fix Linux ENOTSOCK (errno 60) Socket operation on non-socket error. Solutions for socket and file descriptor issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOTSOCK (errno 60) — Socket Operation on Non-Socket

ENOTSOCK (errno 60) means a socket operation was attempted on a file descriptor that is not a socket. This error occurs when a program passes a regular file descriptor (such as from `open()`) to a socket function like `send()`, `recv()`, or `bind()`. It is distinct from EBADF (errno 9) because ENOTSOCK specifically identifies that the descriptor is not a socket type.

## Common Causes

- Passing a file descriptor from `open()` to a socket function
- Wrong file descriptor number used in a socket call
- File descriptor was closed and reused for a non-socket file
- Confusion between stdin (fd 0) and a socket descriptor

## How to Fix ENOTSOCK

### 1. Verify the File Descriptor Type

Check what type of file descriptor you have:

```bash
lsof -p <pid> | grep <fd_number>
```

### 2. Check for Descriptor Duplication

Ensure socket and file descriptors are not accidentally swapped:

```bash
ls -la /proc/<pid>/fd/
```

### 3. Validate the File Descriptor Before Use

In C code, check the descriptor type:

```bash
# Check if fd is a socket using fstat
struct stat st;
fstat(fd, &st);
if (!S_ISSOCK(st.st_mode)) {
    // Not a socket
}
```

### 4. Ensure Proper Socket Creation

Create the socket before using socket functions:

```bash
# In C: create socket first
int sock = socket(AF_INET, SOCK_STREAM, 0);
```

## Verification

After correcting the file descriptor, confirm the socket operation succeeds:

```bash
strace -e trace=socket,send,recv ./program
```

## Related Error Codes

- [EBADF (errno 9)](/os/linux/errno-9/) — Bad file descriptor
- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [ENOTCONN (errno 71)](/os/linux/errno-71/) — Not connected
