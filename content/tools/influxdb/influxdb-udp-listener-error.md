---
title: "[Solution] InfluxDB UDP Listener Error — How to Fix"
description: "Fix InfluxDB UDP listener errors when data sent via UDP protocol is rejected or not received"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB UDP Listener Error

UDP listener errors occur when InfluxDB fails to receive or process data sent over the UDP protocol, which is commonly used by Graphite and StatsD integrations.

## Why It Happens

- UDP listener is not enabled in the configuration
- UDP buffer size is too small for the incoming data rate
- Firewall blocks incoming UDP traffic on the configured port
- Line protocol data exceeds the UDP packet size limit (64KB)
- UDP listener port conflicts with another service

## Common Error Messages

```
error: UDP listener not configured
```

```
udp: packet too large, dropping data
```

```
udp: buffer overflow, incoming data dropped
```

```
error: UDP connection refused on port 8089
```

## How to Fix It

### 1. Enable UDP Listener

```bash
[[udp]]
  enabled = true
  bind-address = ":8089"
  database = "udp_metrics"
  retention-policy = "autogen"
  precision = "ns"
  batch-size = 1000
  batch-timeout = "1s"
```

### 2. Increase UDP Buffer Size

```bash
[[udp]]
  enabled = true
  bind-address = ":8089"
  buffer-size = 1048576
  read-buffer = 2097152
```

### 3. Open Firewall for UDP

```bash
sudo ufw allow 8089/udp
sudo firewall-cmd --add-port=8089/udp --permanent
sudo firewall-cmd --reload
```

### 4. Split Large UDP Packets

```python
import socket

MAX_UDP_SIZE = 65507

def send_udp_chunked(data, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(0, len(data), MAX_UDP_SIZE):
        chunk = data[i:i + MAX_UDP_SIZE]
        sock.sendto(chunk.encode(), (host, port))
```

## Examples

```
$ nc -u -z localhost 8089
$ echo 'cpu,host=s01 value=42' | nc -u -w 1 localhost 8089
```

## Prevent It

- Monitor UDP packet loss with system metrics
- Set appropriate buffer sizes for expected throughput
- Use TCP for critical data that cannot tolerate loss

## Related Pages

- [InfluxDB UDP Error](/tools/influxdb/influxdb-udp-error)
- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB Graphite Error](/tools/influxdb/influxdb-graphite-error)
