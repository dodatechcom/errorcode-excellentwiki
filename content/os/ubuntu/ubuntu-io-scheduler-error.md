---
title: "Ubuntu I/O Scheduler Configuration Error"
description: "I/O scheduler misconfiguration causing poor disk performance"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu I/O Scheduler Configuration Error

I/O scheduler misconfiguration causing poor disk performance

## Common Causes

- Wrong scheduler for device type (e.g., CFQ on SSD)
- Scheduler queue depth too high or too low
- Scheduler not optimized for workload pattern
- Multiple devices with different schedulers conflicting

## How to Fix

1. Check scheduler: `cat /sys/block/sda/queue/scheduler`
2. Set scheduler: `echo mq-deadline | sudo tee /sys/block/sda/queue/scheduler`
3. Optimize for SSD: `echo none | sudo tee /sys/block/nvme0n1/queue/scheduler`
4. Check queue depth: `cat /sys/block/sda/queue/nr_requests`

## Examples

```bash
# Check current I/O scheduler
cat /sys/block/sda/queue/scheduler

# Set scheduler for HDD
echo mq-deadline | sudo tee /sys/block/sda/queue/scheduler

# Set scheduler for SSD (no scheduling needed)
echo none | sudo tee /sys/block/nvme0n1/queue/scheduler
```
