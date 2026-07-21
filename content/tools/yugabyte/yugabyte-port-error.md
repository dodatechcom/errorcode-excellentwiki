---
title: "[Solution] YugabyteDB Port Error — How to Fix"
description: "Fix YugabyteDB port errors by resolving port conflicts, fixing network binding issues, and handling multi-port configuration problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Port Error

YugabyteDB port errors occur when master or tablet server ports are already in use, blocked by firewalls, or misconfigured for inter-node communication.

## Why It Happens

- Another process is using the configured port
- Port is blocked by firewall or security group
- Multiple YugabyteDB instances use the same port
- Port binding address conflicts with the host IP
- RPC port and admin port are configured to the same value
- Client connects to wrong port number

## Common Error Messages

```
ERROR: address already in use
```

```
FATAL: could not bind to port
```

```
ERROR: connection refused on port
```

```
WARNING: port already in use, retrying
```

## How to Fix It

### 1. Check Port Usage

```bash
# Check which process uses a port
sudo netstat -tlnp | grep 7100
sudo netstat -tlnp | grep 9100
sudo netstat -tlnp | grep 5433

# Check all YugabyteDB ports
sudo netstat -tlnp | grep yugabyte
```

### 2. Configure Ports Correctly

```bash
# Master ports
--rpc_bind_addresses=yugabyte:7100
--webserver_port=7000

# TServer ports
--rpc_bind_addresses=yugabyte:9100
--webserver_port=9000
--ysql_proxy_bind_address=yugabyte:5433
--ycql_bind_address=yugabyte:9042
```

### 3. Fix Port Conflicts

```bash
# Kill process using the port
sudo fuser -k 7100/tcp

# Or change the port in configuration
# In master.conf:
--rpc_bind_addresses=yugabyte:7101
```

### 4. Configure Firewall Rules

```bash
# Allow YugabyteDB ports
sudo firewall-cmd --permanent --add-port=7100/tcp
sudo firewall-cmd --permanent --add-port=9100/tcp
sudo firewall-cmd --permanent --add-port=5433/tcp
sudo firewall-cmd --reload

# Or with iptables
sudo iptables -A INPUT -p tcp --dport 7100 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 9100 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5433 -j ACCEPT
```

## Common Scenarios

- **Port already in use**: Kill the conflicting process or change the YugabyteDB port.
- **Client cannot connect**: Ensure the port is open in the firewall.
- **Multiple instances on same port**: Each instance must use unique ports.

## Prevent It

- Document all port assignments for each node
- Verify ports are available before starting services
- Configure firewall rules before deploying

## Related Pages

- [YugabyteDB Connection Error](/tools/yugabyte/yugabyte-connection-error)
- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-config-error)
- [YugabyteDB DNS Error](/tools/yugabyte/yugabyte-tablet-dns-error)
