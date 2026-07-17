---
title: "[Solution] Linux elasticsearch Cluster Error — Fix"
description: "Fix Linux 'elasticsearch: cluster error' and Elasticsearch failures. Resolve cluster health issues, node failures, and shard allocation problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["elasticsearch", "cluster-error", "shard", "node", "search", "logstash"]
weight: 5
---

# Linux: elasticsearch: cluster error

The `elasticsearch: cluster error` message means the Elasticsearch cluster is in a degraded state. This can appear as `cluster_health: RED` or `YELLOW`, shard allocation failures, or node disconnection errors. Cluster errors prevent indexing and search operations from completing successfully.

## What This Error Means

Elasticsearch clusters consist of one or more nodes that hold data shards. The cluster health status indicates: `GREEN` (all shards allocated), `YELLOW` (replica shards unallocated), or `RED` (primary shards unallocated — data loss risk). Cluster errors occur when nodes can't communicate, disk space is exhausted, or shard allocation fails.

## Common Causes

- Node crashed or disconnected from cluster
- Disk space below flood watermark (85%/90%)
- Too many shards per node
- JVM heap memory exhausted (OOM)
- Network partition between nodes
- Corrupted shard data
- Cluster formed but nodes have different versions
- `cluster.max_shards_per_node` limit exceeded

## How to Fix

### 1. Check Cluster Health

```bash
# Check cluster health
curl -s http://localhost:9200/_cluster/health?pretty

# Check node status
curl -s http://localhost:9200/_cat/nodes?v

# Check shard allocation
curl -s http://localhost:9200/_cat/shards?v

# Check for unassigned shards
curl -s http://localhost:9200/_cat/shards?v | grep UNASSIGNED
```

### 2. Fix Disk Watermark Issues

```bash
# Check disk usage
df -h

# Check Elasticsearch disk watermarks
curl -s http://localhost:9200/_cluster/settings?pretty | grep watermark

# Temporarily increase watermarks
curl -X PUT http://localhost:9200/_cluster/settings \
  -H "Content-Type: application/json" \
  -d '{
    "persistent": {
      "cluster.routing.allocation.disk.watermark.low": "90%",
      "cluster.routing.allocation.disk.watermark.high": "95%",
      "cluster.routing.allocation.disk.watermark.flood_stage": "97%"
    }
  }'

# Free up disk space
sudo journalctl --vacuum-size=200M
sudo apt clean
```

### 3. Allocate Unassigned Shards

```bash
# Check unassigned shards
curl -s http://localhost:9200/_cat/shards?v | grep UNASSIGNED

# Force allocate a specific shard
curl -X POST http://localhost:9200/_cluster/reroute \
  -H "Content-Type: application/json" \
  -d '{
    "commands": [{
      "allocate_stale_primary": {
        "index": "my-index",
        "shard": 0,
        "node": "node-name",
        "accept_data_loss": true
      }
    }]
  }'

# Allocate all unassigned shards
curl -X POST http://localhost:9200/_cluster/reroute \
  -H "Content-Type: application/json" \
  -d '{
    "commands": [{
      "allocate_stale_primary": {
        "index": "my-index",
        "shard": 0,
        "node": "node-name",
        "accept_data_loss": true
      }
    }]
  }'
```

### 4. Fix JVM Heap Memory

```bash
# Check heap usage
curl -s http://localhost:9200/_cat/nodes?v&h=name,heap.percent,heap.max

# Increase heap size
sudo nano /etc/elasticsearch/jvm.options
# Change: -Xms4g -Xmx4g (set to 50% of available RAM, max 32GB)

# Restart Elasticsearch
sudo systemctl restart elasticsearch
```

### 5. Restart Elasticsearch Nodes

```bash
# Restart the node
sudo systemctl restart elasticsearch

# For rolling restart of cluster
# 1. Stop shard allocation
curl -X PUT http://localhost:9200/_cluster/settings \
  -H "Content-Type: application/json" \
  -d '{"persistent": {"cluster.routing.allocation.enable": "primaries"}}'

# 2. Stop indexing and flush
curl -X POST http://localhost:9200/_flush/synced

# 3. Stop the node
sudo systemctl stop elasticsearch

# 4. Start the node
sudo systemctl start elasticsearch

# 5. Re-enable shard allocation
curl -X PUT http://localhost:9200/_cluster/settings \
  -H "Content-Type: application/json" \
  -d '{"persistent": {"cluster.routing.allocation.enable": "all"}}'
```

### 6. Delete Problematic Indices

```bash
# List all indices
curl -s http://localhost:9200/_cat/indices?v&s=health

# Delete corrupted or problematic index
curl -X DELETE http://localhost:9200/problematic-index

# Delete old indices to free space
curl -X DELETE http://localhost:9200/logs-2024.01.*
```

### 7. Check Elasticsearch Logs

```bash
# Check Elasticsearch logs
sudo tail -f /var/log/elasticsearch/elasticsearch.log

# Check for specific errors
sudo grep -i "cluster\|shard\|error" /var/log/elasticsearch/elasticsearch.log | tail -20
```

## Examples

```bash
$ curl -s http://localhost:9200/_cluster/health?pretty
{
  "cluster_name": "my-cluster",
  "status": "red",
  "number_of_nodes": 3,
  "number_of_data_nodes": 2,
  "unassigned_shards": 5
}

# Fix: allocate unassigned shards
$ curl -X POST http://localhost:9200/_cluster/reroute \
  -H "Content-Type: application/json" \
  -d '{"commands": [{"allocate_stale_primary": {"index": "logs", "shard": 0, "node": "node-1", "accept_data_loss": true}}]}'

$ curl -s http://localhost:9200/_cluster/health?pretty
{
  "status": "green",
  "unassigned_shards": 0
}
```

## Related Errors

- [Logstash pipeline error]({{< relref "/os/linux/linux-logstash-error" >}}) — Log pipeline failures
- [Grafana dashboard error]({{< relref "/os/linux/linux-grafana-error" >}}) — Dashboard display issues
- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk exhaustion causing cluster issues
