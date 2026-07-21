---
title: "[Solution] YugabyteDB Proxy Error — How to Fix"
description: "Fix YugabyteDB proxy errors by resolving connection proxy failures, fixing load balancer issues, and handling smart client routing problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Proxy Error

YugabyteDB proxy errors occur when connection proxies, load balancers, or smart client drivers fail to route requests correctly to tablet leaders.

## Why It Happens

- Proxy cannot determine tablet leader location
- Load balancer health check fails for a tablet server
- Smart client cache is stale after tablet leader change
- Proxy connection pool is exhausted
- Network latency between proxy and tablet servers is high
- Proxy configuration does not match cluster topology

## Common Error Messages

```
ERROR: tablet not found on this server
```

```
ERROR: proxy connection timeout
```

```
ERROR: leader not found for tablet
```

```
WARNING: stale tablet leader cache
```

## How to Fix It

### 1. Check Proxy Configuration

```yaml
# HAProxy configuration example
global
  maxconn 4096

defaults
  mode tcp
  timeout connect 5000ms
  timeout client 60000ms
  timeout server 60000ms

frontend yugabyte_front
  bind *:5433
  default_backend yugabyte_back

backend yugabyte_back
  option httpchk GET /healthz
  server yb1 yugabyte:5433 check
  server yb2 yugabyte2:5433 check
```

### 2. Fix Smart Client Routing

```python
# Use YugabyteDB smart driver
from yugabyte import smart_driver

conn = smart_driver.connect(
    host='yugabyte-cluster.example.com',
    port=5433,
    dbname='mydb',
    load_balance=True,
    topology_keys='cloud:region:zone'
)
```

### 3. Fix Health Check Issues

```bash
# Test health check endpoint
curl http://yugabyte:9000/healthz

# Check tablet server status
yb-admin -master_addresses yugabyte:7100 list_tablet_servers
```

### 4. Configure Connection Pooling

```yaml
# PgBouncer with load balancing
[databases]
mydb = host=yugabyte port=5433 dbname=mydb

[pgbouncer]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 50
```

## Common Scenarios

- **Proxy routes to wrong node**: Enable health checks and verify tablet leader information.
- **Smart client stale cache**: Increase cache refresh frequency or handle retry logic.
- **Connection pool exhaustion**: Increase pool size or reduce connection hold time.

## Prevent It

- Use YugabyteDB smart driver for automatic load balancing
- Configure proper health checks on load balancers
- Monitor proxy connection metrics

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Load Balancer Error](/tools/yugabyte/yugabyte-load-balancer-error)
- [YugabyteDB Connection Pool Error](/tools/yugabyte/yugabyte-connection-pool-error)
