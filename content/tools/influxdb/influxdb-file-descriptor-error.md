---
title: "[Solution] InfluxDB File Descriptor Error — How to Fix"
description: "Fix InfluxDB file descriptor limit errors when the process exceeds the OS limit for open file handles"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB File Descriptor Error

File descriptor errors occur when InfluxDB tries to open more files than the operating system allows per process.

## Why It Happens

- Too many concurrent connections open file handles
- TSM compaction opens multiple files simultaneously
- Default ulimit is too low for production workload
- WAL files accumulate without being flushed
- Each shard requires multiple open file handles

## Common Error Messages

```
error: too many open files
```

```
tsm1: error opening TSM file: too many open files
```

```
runtime: cannot allocate memory for file descriptor table
```

```
panic: runtime: out of memory -- cannot allocate file descriptors
```

## How to Fix It

### 1. Increase File Descriptor Limit

```bash
# Check current limit
ulimit -n

# Set higher limit for influxdb user
sudo bash -c 'echo "influxdb soft nofile 65536" >> /etc/security/limits.conf'
sudo bash -c 'echo "influxdb hard nofile 65536" >> /etc/security/limits.conf'
```

### 2. Update Systemd Service Limits

```bash
# In /etc/systemd/system/influxdb.service.d/limits.conf
[Service]
LimitNOFILE=65536
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart influxdb
```

### 3. Verify Current Usage

```bash
# Check open files for influxd process
ls -la /proc/$(pgrep influxd)/fd | wc -l

# Monitor file descriptor usage
cat /proc/$(pgrep influxd)/limits | grep "Max open files"
```

### 4. Reduce Shard Count

```bash
# Longer shard group duration means fewer shards
influx -execute 'CREATE RETENTION POLICY "long" ON "mydb" DURATION 365d REPLICATION 1 SHARD DURATION 30d'
```

## Examples

```
$ cat /proc/$(pgrep influxd)/limits | grep "Max open files"
Max open files            1024                 1048576              files
```

After increasing:

```
Max open files            65536                65536                files
```

## Prevent It

- Set file descriptor limits before production deployment
- Monitor open file count with system metrics
- Reduce shard count to minimize open files

## Related Pages

- [InfluxDB Memory Error](/tools/influxdb/influxdb-memory-error)
- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB Compaction Error](/tools/influxdb/influxdb-compaction-error)
