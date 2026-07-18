---
title: "[Solution] CockroachDB Connection Error — How to Fix"
description: "Fix CockroachDB connection refused errors by verifying node status, checking port configuration, resolving DNS issues, and tuning driver connection pools."
tools: ["cockroachdb"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB connection error occurs when a SQL client cannot establish a TCP connection to a CockroachDB node. The error appears as `connection refused`, `dial tcp: connect: connection refused`, or `timeout` depending on the client library and network configuration.

## Why It Happens

Connection errors in CockroachDB can occur at any layer of the connection stack — from DNS resolution to TCP handshake to TLS negotiation. The root cause depends on where in the stack the failure occurs.

- The CockroachDB node process is not running or has crashed
- The SQL port (default 26257) is not listening or is blocked by a firewall
- The node is bound to localhost but the client connects from a remote host
- DNS resolution fails for the configured hostname in containerized environments
- Kubernetes service is not routing traffic to the correct pod
- TLS is required but the client does not provide a valid certificate
- The node is in a decommissioning state and refuses new connections
- Connection pool exhaustion on the client side prevents new connections

## Common Error Messages

```text
dial tcp: connect: connection refused
```

The TCP handshake was rejected. No process is listening on the target port, or a firewall is blocking the connection.

```text
dial tcp: i/o timeout
```

The TCP handshake timed out. This usually indicates a network routing issue or the port is firewalled without a reject response.

```text
FATAL: password authentication failed for user "root"
```

The connection succeeded but authentication failed. This is distinct from a connection error but often confused with it.

```text
connection reset by peer
```

The server accepted the connection but immediately closed it. This can indicate node crash during connection setup or TLS mismatch.

## How to Fix It

### 1. Verify the Node is Running

```bash
# Check if cockroach process is running
ps aux | grep cockroach

# Check as a systemd service
systemctl status cockroachdb

# Check the process logs
tail -100 /var/log/cockroachdb/cockroach.log
```

```bash
# Check if the port is listening
ss -tlnp | grep 26257
# Expected: LISTEN 0 128 0.0.0.0:26257
```

### 2. Start or Restart the Node

```bash
# Start a single-node cluster
cockroach start-single-node \
  --insecure \
  --listen-addr=0.0.0.0:26257 \
  --http-addr=0.0.0.0:8080 \
  --store=path=/var/lib/cockroach/data

# Start a multi-node cluster
cockroach start \
  --insecure \
  --listen-addr=0.0.0.0:26257 \
  --http-addr=0.0.0.0:8080 \
  --join=10.0.1.1:26257,10.0.1.2:26257,10.0.1.3:26257 \
  --store=path=/var/lib/cockroach/data
```

### 3. Configure the Connection String Correctly

```go
// Go with pgx driver
import "github.com/jackc/pgx/v5"

connStr := "postgresql://root@10.0.1.5:26257/mydb?sslmode=require"
conn, err := pgx.Connect(context.Background(), connStr)
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

```java
// Java with JDBC
String url = "jdbc:postgresql://10.0.1.5:26257/mydb?sslmode=require";
Connection conn = DriverManager.getConnection(url, "root", "");
```

### 4. Fix Firewall Rules

```bash
# Allow CockroachDB SQL port
sudo ufw allow from 10.0.0.0/8 to any port 26257

# Allow HTTP admin UI port
sudo ufw allow from 10.0.0.0/8 to any port 8080

# For Kubernetes, ensure the service exposes the correct ports
kubectl get svc cockroachdb -o yaml
```

### 5. Check Node Status in Multi-Node Cluster

```bash
# Check all nodes are healthy
cockroach node status --host=localhost:26257 --insecure

# Decommissioned nodes will show status "DECOMMISSIONED"
# and will not accept new connections
```

### 6. Fix DNS Resolution in Kubernetes

```yaml
# Ensure the headless service resolves correctly
apiVersion: v1
kind: Service
metadata:
  name: cockroachdb
spec:
  clusterIP: None
  selector:
    app: cockroachdb
  ports:
    - name: grpc
      port: 26257
    - name: http
      port: 8080
```

```bash
# Test DNS resolution from a client pod
nslookup cockroachdb-0.cockroachdb.default.svc.cluster.local
```

## Common Scenarios

**Docker containers cannot connect to CockroachDB.** The default configuration binds to localhost. Use `--listen-addr=0.0.0.0:26257` and ensure the container exposes port 26257 in the Docker Compose or Kubernetes pod spec.

**Connection drops intermittently under load.** The node may be hitting resource limits. Check CPU and memory usage, and increase the SQL memory pool with `--sql-memory=4GiB`. Also verify the client connection pool is not too large.

**New nodes cannot join the cluster.** Ensure the `--join` flag points to existing healthy nodes and that inter-node ports (26257, 8080) are open between all nodes. Check the join list with `cockroach init --host`.

## Prevent It

- Always provide multiple contact points in the connection string so the driver can failover if one node is unreachable
- Use load balancers or HAProxy to distribute client connections across healthy nodes
- Monitor node health with CockroachDB's built-in Prometheus metrics and alert when nodes go down
