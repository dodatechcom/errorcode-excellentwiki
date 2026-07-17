---
title: "[Solution] Linux ENOTCONN (errno 71) — Not Connected Fix"
description: "Fix Linux ENOTCONN (errno 71) Not connected error. Solutions for socket connection and state issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOTCONN (errno 71) — Not Connected

ENOTCONN (errno 71) means the socket is not connected. This error occurs when a program tries to send or receive data on a stream socket that has not been connected (or has been disconnected). It is distinct from EPIPE (errno 32) because ENOTCONN indicates the connection was never established, not that it was broken.

## Common Causes

- Attempting to `send()` or `recv()` on an unconnected TCP socket
- Socket was closed by the remote peer and not detected
- Forgetting to call `connect()` before sending data
- Using `send()` instead of `sendto()` on an unconnected UDP socket

## How to Fix ENOTCONN

### 1. Verify Socket State

Check the current state of the socket:

```bash
ss -tnp
netstat -tnp | grep <pid>
```

### 2. Ensure Connection is Established

Call `connect()` before sending data:

```bash
# In C: establish connection first
int sock = socket(AF_INET, SOCK_STREAM, 0);
connect(sock, (struct sockaddr *)&addr, sizeof(addr));
send(sock, data, len, 0);
```

### 3. Check for Broken Connections

Detect stale connections:

```bash
ss -tnp state established | grep <port>
```

### 4. Use sendto() for Unconnected Sockets

For UDP, use `sendto()` with destination address:

```bash
sendto(sock, data, len, 0, &dest_addr, sizeof(dest_addr));
```

### 5. Handle EPIPE and SIGPIPE

Detect connection loss before writing:

```bash
signal(SIGPIPE, SIG_IGN);
send(sock, data, len, MSG_NOSIGNAL);
```

## Verification

After ensuring proper connection, confirm data flows:

```bash
ss -tnp state established
curl -v http://server/api
```

## Related Error Codes

- [EPIPE (errno 32)](/os/linux/errno-32/) — Broken pipe
- [ECONNREFUSED (errno 75)](/os/linux/errno-75/) — Connection refused
- [EISCONN (errno 70)](/os/linux/errno-70/) — Already connected
