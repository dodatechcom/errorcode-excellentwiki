---
title: "[Solution] Linux Elasticsearch Cluster Health RED"
description: "Fix Linux Elasticsearch cluster health RED errors. Resolve unassigned shards, index corruption, and cluster recovery issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["elasticsearch", "cluster", "health-red", "shards", "unassigned", "search"]
weight: 5
---

# Linux: Elasticsearch — cluster health RED

The Elasticsearch `cluster health: RED` status means one or more primary shards are unassigned. A RED cluster cannot serve search requests for the affected indices. This is the most severe health state and requires immediate attention, as it indicates data loss or the inability to access primary shard data.

## What This Error Means

Elasticsearch distributes index data across shards, each with a primary and optional replica. The cluster health is RED when any primary shard is unassigned — the data in that shard is unavailable. This happens when a node hosting primary shards goes down, disk space is exhausted, or the cluster cannot allocate shards due to allocation rules. YELLOW means primaries are OK but replicas are unassigned.

## Common Causes

- Node failure taking primary shards offline
- Disk watermarks exceeded (disk usage above high watermark)
- Too many shards for the available nodes
- Corrupted shard data on disk
- Allocation filtering rules preventing shard placement
- Cluster not recovering after restart (split-brain)
- Index corruption from improper shutdown

## How to Fix

### 1. Check Cluster Health and Identify the Problem

```bash
# Check cluster health
curl -s localhost:9200/_cluster/health?pretty

# Find unassigned shards
curl -s localhost:9200/_cat/shards?v | grep UNASSIGNED

# Check which indices have unassigned shards
curl -s localhost:9200/_cat/indices?v | grep RED
```

### 2. Check Node Status

```bash
# Check all nodes
curl -s localhost:9200/_cat/nodes?v

# Check node disk usage
curl -s localhost:9200/_cat/allocation?v

# Check if nodes are leaving/joining
curl -s localhost:9200/_cat/health?v
```

### 3. Fix Disk Watermark Issues

```bash
# Check current disk usage
df -h

# Check Elasticsearch disk watermarks
curl -s localhost:9200/_cluster/settings | python3 -m json.tool

# Temporarily raise the high watermark
curl -X PUT "localhost:9200/_cluster/settings" -H 'Content-Type: application/json' -d '{
  "transient": {
    "cluster.routing.allocation.disk.watermark.high": "90%",
    "cluster.routing.allocation.disk.watermark.flood_stage": "95%"
  }
}'

# Free disk space
sudo journalctl --vacuum-size=200M
sudo find /var/log -name "*.gz" -delete
```

### 4. Allocate Unassigned Shards

```bash
# Try to allocate all unassigned shards
curl -X POST "localhost:9200/_cluster/reroute" -H 'Content-Type: application/json' -d '{
  "commands": [{
    "allocate_stale_primary": {
      "index": "myindex",
      "shard": 0,
      "node": "node-name",
      "accept_data_loss": true
    }
  }]
}'

# Retry allocation
curl -X POST "localhost:9200/_cluster/reroute?retry_failed=true"

# Or allocate all unassigned shards
curl -s localhost:9200/_cat/shards?v | grep UNASSIGNED | awk '{print $1, $2}' | while read index shard; do
  curl -X POST "localhost:9200/_cluster/reroute" -H 'Content-Type: application/json' -d "{
    \"commands\": [{
      \"allocate_empty_primary\": {
        \"index\": \"$index\",
        \"shard\": $shard,
        \"node\": \"$(curl -s localhost:9200/_cat/nodes?h=name | head -1)\",
        \"accept_data_loss\": true
      }
    }]
  }"
done
```

### 5. Fix Allocation Filtering

```bash
# Check allocation settings
curl -s localhost:9200/_cluster/settings?pretty | grep -A5 allocation

# Remove any exclude rules
curl -X PUT "localhost:9200/_cluster/settings" -H 'Content-Type: application/json' -d '{
  "transient": {
    "cluster.routing.allocation.exclude._name": null,
    "cluster.routing.allocation.include._name": null
  }
}'

# Check index-level allocation
curl -s localhost:9200/myindex/_settings?pretty | grep allocation
```

### 6. Recover from Corrupted Shards

```bash
# If a shard is corrupted, delete and let it rebuild from replicas
curl -X DELETE "localhost:9200/corrupted-index"

# Restore from snapshot
curl -X POST "localhost:9200/_snapshot/my_backup/_restore" -H 'Content-Type: application/json' -d '{
  "indices": "corrupted-index",
  "ignore_unavailable": true
}'

# Force close and reopen the index
curl -X POST "localhost:9200/myindex/_close"
curl -X POST "localhost:9200/myindex/_open"
```

### 7. Monitor Cluster Recovery

```bash
# Watch shard allocation progress
watch -n 5 'curl -s localhost:9200/_cluster/health?pretty | grep -E "status|unassigned_shards|relocating_shards|active_shards"'

# Check recovery status
curl -s localhost:9200/_cat/recovery?v | head -20

# View cluster stats
curl -s localhost:9200/_cluster/stats?pretty | grep -E 'nodes|indices|shards'
```

## Examples

```bash
$ curl -s localhost:9200/_cluster/health?pretty
{
  "cluster_name": "production",
  "status": "red",
  "number_of_nodes": 3,
  "number_of_data_nodes": 3,
  "active_primary_shards": 45,
  "active_shards": 90,
  "relocating_shards": 0,
  "unassigned_shards": 12
}

$ curl -s localhost:9200/_cat/shards?v | grep UNASSIGNED
myindex    0 p UNASSIGNED
myindex    1 p UNASSIGNED

# Fix: allocate the shards
$ curl -X POST "localhost:9200/_cluster/reroute?retry_failed=true"
{"acknowledged":true}

$ curl -s localhost:9200/_cluster/health | grep status
"status":"green"
```

## Related Errors

- [Elasticsearch cluster error]({{< relref "/os/linux/linux-elastic-cluster-error" >}}) — General cluster issues
- [Redis OOM]({{< relref "/os/linux/linux-redis-oom" >}}) — Redis memory errors
- [NFS mount error]({{< relref "/os/linux/linux-nfs-mount-error-v2" >}}) — Storage mount failures
