---
title: "[Solution] OpenSSL Session Error"
description: "Fix OpenSSL session resumption errors when TLS session tickets fail"
tools: ["openssl"]
error-types: ["tool-error"]
severities: ["error"]
---

# OpenSSL Session Error

Session errors occur when OpenSSL TLS session resumption or session ticket handling fails.

## Common Causes

- Session ID context not configured
- Session ticket key expired
- Session cache too small
- Session callback not registered

## Common Error Messages

```
error:1408F10B:SSL routines:ssl3_get_record:wrong version number
```

## How to Fix

### 1. Check Session Resumption

```bash
openssl s_client -connect example.com:443 -reconnect 2>&1 | grep "Reused"
```

### 2. Test Session Ticket

```bash
openssl s_client -connect example.com:443 -sess_out session.pem
openssl s_client -connect example.com:443 -sess_in session.pem
```

### 3. Disable Session Tickets (Debug)

```bash
openssl s_client -connect example.com:443 -no_ticket
```

## Examples

```bash
openssl s_client -connect example.com:443 -tlsextdebug 2>&1 | grep -i session
```
