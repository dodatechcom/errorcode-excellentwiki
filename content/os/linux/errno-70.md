---
title: "[Solution] Linux EISCONN (errno 70) — Already Connected Fix"
description: "Fix Linux EISCONN (errno 70) Already connected error. Solutions for socket connection state issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["eisconn", "socket", "errno-70", "connected", "already"]
weight: 5
---

# Linux EISCONN (errno 70) — Already Connected

EISCONN (errno 70) means the socket is already connected. This error occurs when a program tries to connect a socket that is already in a connected state, or tries to send data to an address when the socket is already connected to a different address. It is distinct from EALREADY (errno 114) because EISCONN indicates the connection is fully established, not just that an operation is in progress.

## Common Causes

- Attempting to `connect()` on an already-connected socket
- Trying to `sendto()` on a connected TCP socket with a different address
- Code logic error calling connect twice without closing
- UDP socket bound to an address then trying to connect again

## How to Fix EISCONN

### 1. Check Socket State

Verify the current socket connection state:

```bash
ss -t state established
netstat -tnp
```

### 2. Close and Reconnect

If you need to connect to a different address, close first:

```bash
# Close the socket before reconnecting
close(sock);
sock = socket(AF_INET, SOCK_STREAM, 0);
connect(sock, &addr, sizeof(addr));
```

### 3. Use sendto() Properly

For UDP sockets, use `sendto()` without connecting first:

```bash
# Don't connect UDP sockets, use sendto directly
sendto(sock, data, len, 0, &dest_addr, sizeof(dest_addr));
```

### 4. Check Application Logic

Review code for multiple connect calls:

```bash
strace -e trace=connect ./program
```

## Verification

After fixing the connection logic, confirm operations succeed:

```bash
strace -e trace=connect,sendto ./program
ss -t state established
```

## Related Error Codes

- [EALREADY (errno 78)](/os/linux/errno-78/) — Operation already in progress
- [EINPROGRESS (errno 79)](/os/linux/errno-79/) — Operation now in progress
- [ECONNREFUSED (errno 75)](/os/linux/errno-75/) — Connection refused
