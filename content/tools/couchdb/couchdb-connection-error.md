---
title: "[Solution] CouchDB Connection Error — How to Fix"
description: "Fix CouchDB connection errors by verifying port bindings, adjusting bind_address settings, and resolving network timeout issues"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Connection Error

CouchDB connection errors occur when clients cannot establish or maintain a connection to the CouchDB instance. These errors are common during initial setup, network changes, or high-load scenarios.

## Why It Happens

- CouchDB is bound to `127.0.0.1` and the client connects remotely
- The `bind_address` in `local.ini` is set to localhost only
- The CouchDB service is not running or has crashed
- Firewall rules block port 5984 (HTTP) or 6984 (HTTPS)
- Reverse proxy misconfiguration drops the connection
- Too many open connections exceed the limit

## Common Error Messages

```
{ "error": "econnrefused", "reason": "Connection refused - connect(2) for \"127.0.0.1\" port 5984" }
```

```
{ "error": "econnreset", "reason": "Connection reset by peer" }
```

```
{ "error": "etimeout", "reason": " connect ETIMEDOUT 10.0.0.5:5984" }
```

```
{ "error": "eaddrinuse", "reason": "Address already in use - bind(2) for 0.0.0.0:5984" }
```

## How to Fix It

### 1. Configure bind_address for Remote Access

```ini
; In /opt/couchdb/etc/local.ini or /etc/couchdb/local.ini
[chttpd]
bind_address = 0.0.0.0
port = 5984

[httpd]
bind_address = 0.0.0.0
port = 5984
```

```bash
sudo systemctl restart couchdb
```

### 2. Verify CouchDB is Running

```bash
# Check service status
sudo systemctl status couchdb

# Check if port is in use
ss -tlnp | grep 5984

# Test local connection
curl http://127.0.0.1:5984/
```

### 3. Adjust Timeout Settings

```ini
; In local.ini
[chttpd]
; Increase socket timeout in milliseconds
socket_options = [{nodelay, true}, {keepalive, true}, {delay_send, false}]

; Increase request timeout
; request_timeout = 60000
```

```bash
# Also increase OS-level TCP settings
sudo sysctl -w net.core.somaxconn=1024
sudo sysctl -w net.ipv4.tcp_keepalive_time=60
```

### 4. Fix Firewall Rules

```bash
# Ubuntu/Debian
sudo ufw allow 5984/tcp
sudo ufw allow 6984/tcp

# CentOS/RHEL
sudo firewall-cmd --permanent --add-port=5984/tcp
sudo firewall-cmd --reload

# Test remote connectivity
curl http://your-server:5984/
```

## Common Scenarios

- **Docker CouchDB not reachable**: Map port 5984 explicitly with `-p 5984:5984` and set `bind_address = 0.0.0.0`.
- **Reverse proxy drops connections**: Ensure nginx or HAProxy forwards `X-Forwarded-For` headers and does not set aggressive timeouts.
- **Cluster nodes cannot connect**: Verify all nodes use the same `bind_address` and inter-node communication ports.

## Prevent It

- Use a reverse proxy (nginx/HAProxy) instead of exposing CouchDB directly
- Monitor CouchDB with `_up` endpoint and set up alerts on connection failures
- Configure connection pooling in your application client

## Related Pages

- [CouchDB HTTP Error](/tools/couchdb/couchdb-http-error)
- [CouchDB SSL Error](/tools/couchdb/couchdb-ssl-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
