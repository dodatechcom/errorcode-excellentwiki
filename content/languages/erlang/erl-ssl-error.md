---
title: "[Solution] Erlang SSL Error"
description: "SSL/TLS connection errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang SSL Error

SSL/TLS connection errors.

### Common Causes
Wrong cert; version mismatch; handshake

### How to Fix
```erlang
ssl:start(),
{ok, Socket} = ssl:connect("example.com", 443, [{verify, verify_none}]).
```

### Examples
```erlang
{ok, CACert} = file:read_file("ca.pem"),
{ok, Socket} = ssl:connect("example.com", 443, [{cacerts, [CACert]}, {verify, verify_peer}]).
```
