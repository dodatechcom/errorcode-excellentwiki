---
title: "[Solution] InfluxDB Clock Skew Error — How to Fix"
description: "Fix InfluxDB clock skew errors when server and client time differences cause write rejections"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Clock Skew Error

Clock skew errors occur when there is a significant time difference between the InfluxDB server and the client, causing data points to be written outside the acceptable time window.

## Why It Happens

- NTP synchronization is not configured or is failing
- Virtual machine clocks drift from the host system
- Container time is not synchronized with the host
- Manual time configuration was incorrect
- Timezone mismatches between client and server

## Common Error Messages

```
partial write: points out of time window, check clock skew
```

```
error: timestamp too far in the future
```

```
partial write: unable to write points older than retention policy
```

## How to Fix It

### 1. Synchronize Clocks with NTP

```bash
ntpdate -q pool.ntp.org
sudo apt install ntp
sudo systemctl enable --now ntp
```

### 2. Configure NTP on Containers

```bash
docker run -v /etc/localtime:/etc/localtime:ro \
  -v /etc/timezone:/etc/timezone:ro \
  influxdb:latest
```

### 3. Check Time on Kubernetes Pods

```bash
kubectl exec -it influxdb-pod -- date
kubectl exec -it influxdb-pod -- ntpdate -q pool.ntp.org
```

### 4. Set Correct Timezone

```bash
sudo timedatectl set-timezone UTC
timedatectl
```

## Examples

```
$ ntpdate -q pool.ntp.org
server 203.0.113.1, stratum 2, offset -5.2345, delay 0.05678
```

## Prevent It

- Run NTP on all InfluxDB servers and clients
- Monitor clock drift in infrastructure monitoring
- Use UTC for all timestamp operations

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Line Protocol Error](/tools/influxdb/influxdb-line-protocol-error)
- [InfluxDB Point Time Error](/tools/influxdb/influxdb-point-time-error)
