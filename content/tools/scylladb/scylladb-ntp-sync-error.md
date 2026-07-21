---
title: "[Solution] ScyllaDB NTP Sync Error — How to Fix"
description: "Fix ScyllaDB NTP synchronization errors when time drift between nodes causes consistency problems"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB NTP Sync Error

NTP synchronization errors occur when ScyllaDB nodes have significant clock drift, causing consistency issues, hinted handoff problems, and data inconsistency.

## Why It Happens

- NTP service is not running or not installed
- Firewall blocks NTP traffic (UDP port 123)
- NTP server is unreachable or misconfigured
- Virtual machine clock drifts from host
- Hardware clock is significantly wrong

## Common Error Messages

```
WARN: Skew too large between nodes: node1:0ms, node2:5000ms
```

```
ERROR: Clock skew between nodes exceeds threshold
```

```
hinted_handoff: hints may be incorrect due to clock skew
```

## How to Fix It

### 1. Install and Configure NTP

```bash
sudo apt-get install -y ntp
sudo systemctl enable --now ntp
```

### 2. Verify NTP Synchronization

```bash
ntpq -p
timedatectl status
chronyc sources
```

### 3. Fix NTP Configuration

```bash
# /etc/ntp.conf
server pool.ntp.org iburst
restrict default nomodify notrap
```

### 4. Set Maximum Allowed Skew

```yaml
# In scylla.yaml
max_hint_window_in_ms: 10800000
```

## Examples

```
$ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*time.google.com .GPS.            1 u   45   64  377   12.345   -0.123   0.456
```

## Prevent It

- Run NTP on all ScyllaDB nodes
- Use multiple NTP sources for reliability
- Monitor clock drift between nodes

## Related Pages

- [ScyllaDB NTP Error](/tools/scylladb/scylladb-ntp-error)
- [ScyllaDB Consistency Error](/tools/scylladb/scylladb-consistency-error)
- [ScyllaDB Clock Error](/tools/scylladb/scylladb-clock-error)
