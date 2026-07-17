---
title: "[Solution] Linux EINVAL (errno 22) — Invalid Argument Fix"
description: "Fix Linux EINVAL (errno 22) Invalid Argument error. Resolve malformed parameters, invalid system calls, and argument validation issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
weight: 60
---

# Linux EINVAL (errno 22) — Invalid Argument

EINVAL (errno 22) means a system call or library function received an argument that is not valid. This is one of the most generic Linux errors — it can appear in virtually any context, from filesystem operations and socket configuration to ioctl calls and memory mapping. EINVAL usually indicates a coding error or misconfiguration rather than a transient issue.

## Common Causes

- Malformed command-line arguments or options
- Invalid file descriptor passed to a system call
- Misconfigured kernel or filesystem parameters
- ioctl call with unsupported command or argument
- Memory mapping with invalid address or length
- Invalid flags passed to open(), mmap(), or socket()
- Sysctl parameter out of the allowed range

## How to Fix EINVAL

### 1. Check Function Arguments

Review each argument passed to the failing function:

```bash
# Verify command syntax
command --help

# Read the man page for the specific syscall
man 2 open
man 2 mmap
man 2 ioctl
man 2 socket

# Check if the argument is within the valid range
python3 -c "
import os
# Example: checking valid uid/gid
print('UID:', os.getuid())
print('GID:', os.getgid())
"
```

### 2. Validate Input Parameters

Validate parameters before passing them to system calls:

```bash
# Check that a file descriptor is valid
ls -la /proc/self/fd/

# Verify a memory address for mmap (must be page-aligned)
python3 -c "
import os
page_size = os.sysconf('SC_PAGE_SIZE')
print('Page size:', page_size)
print('Must be multiple of', page_size)
"

# Check socket options
ss -tlnp
```

### 3. Check ioctl Compatibility

ioctl EINVAL is common with device drivers:

```bash
# Find the correct ioctl command for your device
man ioctl

# List available ioctl commands for a device
strace -e ioctl your_command 2>&1 | grep -i "ioctl"

# Check device driver information
cat /proc/devices
lsmod | grep driver_name
```

### 4. Fix mmap Arguments

Common mmap EINVAL causes:

```bash
# Check page size (address must be page-aligned)
getconf PAGESIZE

# Verify the offset is a multiple of page size
python3 -c "
import os
page = os.sysconf('SC_PAGE_SIZE')
offset = 4096
if offset % page != 0:
    print(f'Offset {offset} not aligned to page size {page}')
else:
    print('Offset is valid')
"

# Check memory limits
cat /proc/self/limits | grep "Address space"
ulimit -a
```

### 5. Fix sysctl and Kernel Parameters

Invalid sysctl values cause EINVAL:

```bash
# Check current sysctl value
sysctl net.core.somaxconn

# Find valid range for a parameter
sysctl -a | grep parameter_name

# Set a valid value
sudo sysctl -w net.core.somaxconn=1024

# Make persistent
echo "net.core.somaxconn = 1024" | sudo tee -a /etc/sysctl.conf
```

### 6. Check Socket Arguments

Socket-related EINVAL:

```bash
# Verify address family
python3 -c "
import socket
print('AF_INET:', socket.AF_INET)
print('AF_INET6:', socket.AF_INET6)
print('AF_UNIX:', socket.AF_UNIX)
"

# Check that the port is in valid range (0-65535)
python3 -c "
port = 8080
if not (0 <= port <= 65535):
    print(f'Invalid port: {port}')
else:
    print(f'Port {port} is valid')
"

# Check TCP keepalive settings
cat /proc/sys/net/ipv4/tcp_keepalive_time
```

### 7. Fix open() Flags

Invalid flags passed to `open()`:

```bash
# Verify flags are compatible
python3 -c "
import os
# O_RDONLY, O_WRONLY, O_RDWR are mutually exclusive
# O_CREAT without O_EXCL is fine
# O_TRUNC requires write access
fd = os.open('/tmp/test', os.O_CREAT | os.O_RDWR | os.O_TRUNC, 0o644)
print('Opened successfully')
os.close(fd)
"
```

### 8. Use strace to Identify the Failing Call

Trace system calls to pinpoint the exact failure:

```bash
# Trace all system calls and filter for EINVAL
strace -e trace=network your_command 2>&1 | grep EINVAL

# Trace file operations
strace -e trace=file your_command 2>&1

# Full trace for debugging
strace -f -o /tmp/trace.log your_command
grep -i "EINVAL" /tmp/trace.log
```

### 9. Check Argument Alignment and Types

Some syscalls require specific alignment:

```bash
# Check struct alignment requirements
python3 -c "
import ctypes
print('sizeof(int):', ctypes.sizeof(ctypes.c_int))
print('sizeof(long):', ctypes.sizeof(ctypes.c_long))
print('Alignment:', ctypes.alignment(ctypes.c_long))
"

# For sendmsg/recvmsg, verify iovec structures
python3 -c "
import socket, struct
# Verify message header is correctly formed
print('MSG_TRUNC:', socket.MSG_TRUNC)
print('MSG_PEEK:', socket.MSG_PEEK)
"
```

### 10. Consult Documentation for Specific Syscall

Each syscall has unique EINVAL conditions:

```bash
# Common EINVAL man pages
man 2 open       # flags validation
man 2 mmap       # addr, length, offset, flags
man 2 ioctl      # request code and argument
man 2 socket     # domain, type, protocol
man 2 sendto     # address length, flags
man 2 prctl      # option and argument
man 2 ptrace     # request and pid
```

## Related Error Codes

- [EBADF (errno 9)](/os/linux/errno-9/) — Bad file descriptor
- [EFAULT (errno 14)](/os/linux/errno-14/) — Bad address
- [ENOTTY (errno 25)](/os/linux/errno-25/) — Inappropriate ioctl for device
