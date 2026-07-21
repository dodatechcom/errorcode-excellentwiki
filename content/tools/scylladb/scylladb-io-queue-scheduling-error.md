---
title: "[Solution] ScyllaDB IO Queue Scheduling Error — How to Fix"
description: "Fix ScyllaDB IO queue scheduling errors when the I/O scheduler cannot distribute disk operations fairly"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB IO Queue Scheduling Error

IO queue scheduling errors occur when ScyllaDB's I/O scheduler fails to distribute disk operations across priority classes, causing latency spikes and throughput drops.

## Why It Happens

- Disk I/O scheduler is misconfigured for the workload
- IOPS limit is set too low for the storage backend
- Multiple I/O priority classes are competing for limited bandwidth
- Storage device does not support the requested I/O scheduler
- System CPU is saturated, delaying I/O scheduling decisions

## Common Error Messages

```
io_queue: request timed out waiting for I/O scheduling
```

```
ERROR: IO scheduler unable to meet latency target for reads
```

```
io_queue: shard 0 I/O queue overloaded, requests queued
```

## How to Fix It

### 1. Check I/O Scheduler Status

```bash
nodetool io-profiler
cat /sys/block/sda/queue/scheduler
```

### 2. Configure I/O Scheduler

```bash
# Set mq-deadline for NVMe drives
echo mq-deadline | sudo tee /sys/block/nvme0n1/queue/scheduler

# Or set noop for fast SSDs
echo noop | sudo tee /sys/block/sda/queue/scheduler
```

### 3. Tune I/O Queue Properties

```yaml
# In scylla.yaml
io_scheduler: mq-deadline
read_iops: 10000
write_iops: 5000
read_throughput: 500
write_throughput: 300
```

### 4. Monitor I/O Queue Metrics

```bash
nodetool tpstats | grep -i io
iostat -x 1 5
```

## Examples

```
$ cat /sys/block/sda/queue/scheduler
[mq-deadline] kyber bfq none
```

## Prevent It

- Use Scylla's built-in io_setup tool for initial configuration
- Monitor I/O latency percentiles with Scylla Monitoring
- Match I/O scheduler to storage type (HDD vs SSD vs NVMe)

## Related Pages

- [ScyllaDB IO Queue Full](/tools/scylladb/scylladb-io-queue-full)
- [ScyllaDB IO Queue Full Error](/tools/scylladb/scylladb-io-queue-full-error)
- [ScyllaDB Disk Latency Error](/tools/scylladb/scylladb-disk-latency-error)
