---
title: "[Solution] InfluxDB Connection Error — How to Fix"
description: "Fix InfluxDB connection errors including refused connections, timeout issues, HTTP API failures, and authentication problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Connection Error

InfluxDB connection errors occur when clients cannot connect via the HTTP API, UDP, or Unix socket interfaces.

## Why It Happens

- InfluxDB is not running or crashed
- The HTTP bind address is set to localhost only
- The port is already in use by another service
- Authentication is required but not provided
- Firewall blocks the InfluxDB port (8086)
- The client and server have network connectivity issues

## Common Error Messages

```
Failed to connect to http://localhost:8086
```

```
{"error":"unauthorized access"}
```

```
connection refused: dial tcp 127.0.0.1:8086: connect: connection refused
```

```
http: server gave HTTP response to HTTPS client
```

## How to Fix It

### 1. Check InfluxDB Service Status

```bash
sudo systemctl status influxd
influx version
```

### 2. Fix Bind Address

```bash
# In /etc/influxdb/influxdb.conf
[http]
  bind-address = ":8086"
  # Or for specific interface
  # bind-address = "192.168.1.100:8086"
```

```bash
sudo systemctl restart influxd
```

### 3. Fix Authentication

```bash
# Create an admin user first
influx -execute 'CREATE USER admin WITH PASSWORD "password" WITH ALL PRIVILEGES'

# Then connect with credentials
influx -username admin -password password
```

### 4. Fix Firewall

```bash
sudo ufw allow 8086/tcp
sudo iptables -A INPUT -p tcp --dport 8086 -j ACCEPT
```

### 5. Test Connection

```bash
curl -s 'http://localhost:8086/ping'
curl -s 'http://localhost:8086/query?q=SHOW+DATABASES'
```

## Common Scenarios

- **Fresh install cannot connect**: Ensure InfluxDB is started and listening on the correct port.
- **Remote client cannot connect**: Change bind-address to `0.0.0.0` and open firewall.
- **Authentication fails**: Create admin user before enabling auth.

## Prevent It

- Configure bind-address to accept remote connections during initial setup
- Use environment variables for credentials instead of hardcoding
- Monitor InfluxDB health with regular ping checks

## Related Pages

- [InfluxDB Auth Error](/tools/influxdb/influxdb-auth-error)
- [InfluxDB HTTP Error](/tools/influxdb/influxdb-http-error)
- [InfluxDB Token Error](/tools/influxdb/influxdb-token-error)
