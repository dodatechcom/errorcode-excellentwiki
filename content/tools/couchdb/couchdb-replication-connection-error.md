---
title: "[Solution] CouchDB Replication Connection Error — How to Fix"
description: "Fix CouchDB replication connection errors by resolving connection failures during replication, fixing network issues, and handling connection timeout problems"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Replication Connection Error

CouchDB replication connection errors occur when the replicator cannot establish or maintain a connection to source or target database.

## Why It Happens

- Network is unreachable
- DNS resolution fails
- Firewall blocks replication ports
- SSL/TLS handshake fails
- Connection pool is exhausted
- Too many concurrent connections

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Connection refused" }
```

```
{ "error": "timeout", "reason": "Connection timeout" }
```

```
{ "error": "internal_server_error", "reason": "DNS resolution failed" }
```

```
{ "error": "internal_server_error", "reason": "SSL handshake failed" }
```

## How to Fix It

### 1. Test Connection

```bash
# Test basic connectivity
ping source-host

# Test CouchDB port
telnet source-host 5984

# Test with curl
curl -v http://source-host:5984/
```

### 2. Fix DNS Issues

```bash
# Check DNS resolution
nslookup source-host

# Add to /etc/hosts if needed
echo "192.168.1.100 source-host" | sudo tee -a /etc/hosts
```

### 3. Fix Firewall Issues

```bash
# Check if port is open
nc -zv source-host 5984

# Open firewall port (Ubuntu)
sudo ufw allow 5984/tcp

# Open firewall port (CentOS)
sudo firewall-cmd --add-port=5984/tcp --permanent
sudo firewall-cmd --reload
```

### 4. Fix SSL Issues

```bash
# Test SSL connection
curl -v --cacert /path/to/ca.crt https://source-host:6984/

# Skip SSL verification (not recommended for production)
curl -k https://source-host:6984/
```

## Common Scenarios

- **Connection refused**: Check if CouchDB is running and port is correct.
- **Connection timeout**: Check network and firewall settings.
- **SSL handshake failed**: Verify SSL certificate is valid and trusted.

## Prevent It

- Test connectivity before starting replication
- Monitor network health
- Use reliable DNS resolution

## Related Pages

- [CouchDB Replication Error](/tools/couchdb/couchdb-replication-error)
- [CouchDB Connection Error](/tools/couchdb/couchdb-connection-error)
- [CouchDB Network Error](/tools/couchdb/couchdb-network-error)
