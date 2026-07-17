---
title: "[Solution] CockroachDB Connection Refused - Fix Cluster Connectivity"
description: "Fix CockroachDB connection refused errors by verifying the node process is running, checking firewall rules, opening port 26257, and configuring driver settings"
tools: ["cockroachdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A CockroachDB connection refused error occurs when the SQL client cannot establish a TCP connection to a CockroachDB node. The error appears as `connection refused` or `dial tcp: connect: connection refused` depending on the client library.

## What This Error Means

When a client attempts to connect to CockroachDB, the operating system rejects the TCP handshake because either no process is listening on the target port, or a firewall is blocking the connection. CockroachDB uses port 26257 for SQL connections and port 8080 for the HTTP admin UI by default.

The error is a network-level failure and occurs before any SQL authentication takes place. It is distinct from authentication errors or query-level errors.

## Why It Happens

- CockroachDB node is not running or has crashed
- Incorrect host or port in the connection string
- CockroachDB is bound to `localhost` and the client connects from a remote host
- Firewall or security group blocking port 26257
- Kubernetes service not routing traffic to the correct pod
- DNS resolution failure for the configured hostname
- Node is in a decommissioning state and no longer accepting connections

## How to Fix It

### 1. Verify CockroachDB is Running

```bash
# Check the process
ps aux | grep cockroach

# Or check as a systemd service
systemctl status cockroachdb
```

### 2. Check if the Port is Listening

```bash
ss -tlnp | grep 26257
# Expected: LISTEN 0 128 0.0.0.0:26257
```

### 3. Start CockroachDB

```bash
cockroach start-single-node \
  --insecure \
  --listen-addr=0.0.0.0:26257 \
  --http-addr=0.0.0.0:8080 \
  --store=path=/var/lib/cockroach/data
```

### 4. Test the Connection

```bash
cockroach sql --insecure --host=localhost:26257
```

### 5. Check Firewall Rules

```bash
sudo ufw allow from 10.0.0.0/8 to any port 26257
```

### 6. Verify the Connection String

```go
// Go driver
import "github.com/lib/pq"

connStr := "postgresql://user:pass@10.0.1.5:26257/mydb?sslmode=require"
db, err := sql.Open("postgres", connStr)
```

```python
# Python with psycopg2
import psycopg2
conn = psycopg2.connect(
    host="10.0.1.5",
    port=26257,
    dbname="mydb",
    user="root",
    sslmode="require"
)
```

### 7. Check Node Status in a Multi-Node Cluster

```bash
cockroach node status --host=localhost:26257 --insecure
```

## Common Mistakes

- Using port 5432 (PostgreSQL default) instead of 26257 (CockroachDB default)
- Forgetting to set `--listen-addr` to `0.0.0.0` when running in Docker
- Not exposing port 26257 in the Docker container or Kubernetes pod spec
- Connecting without SSL when the cluster is configured to require TLS

## Related Pages

- [CockroachDB Node Unavailable](/tools/cockroachdb/cockroach-node-unavailable)
- [CockroachDB Certificate Error](/tools/cockroachdb/cockroach-certificate-error)
- [CockroachDB Timeout](/tools/cockroachdb/cockroach-timeout)
