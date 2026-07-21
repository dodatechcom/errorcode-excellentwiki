---
title: "[Solution] Elasticsearch Cluster Block Error"
description: "Fix Elasticsearch cluster block errors. Resolve write blocks preventing index operations on the cluster."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Cluster Block Error

Elasticsearch cluster block errors occur when write or read operations are rejected due to cluster-level or index-level blocks being active.

## Common Causes

- Disk watermark exceeded triggering automatic write block
- Manual block applied with cluster update settings
- Read-only block set during maintenance or migration
- Block applied due to exceeding shard allocation limits

## Common Error Messages

- `cluster_block_exception`
- `blocked_by: [FORBIDDEN/index_block]`
- `write_block_exception`

## How to Fix It

### Solution 1: Check active blocks

View current cluster blocks:

```bash
curl -X GET "localhost:9200/_cluster/settings?pretty" | grep -A 5 "blocks"
```

### Solution 2: Remove the read-only block

If set during maintenance, remove it:

```bash
curl -X PUT "localhost:9200/_all/_settings" -H 'Content-Type: application/json' -d '{
  "index.blocks.write": null
}'
```

### Solution 3: Clear cluster-level blocks

Remove all cluster blocks:

```bash
curl -X PUT "localhost:9200/_cluster/settings" -H 'Content-Type: application/json' -d '{
  "persistent": {
    "cluster.blocks.configuration": null
  }
}'
```

## Prevent It

- Monitor disk usage and configure appropriate watermarks
- Remove maintenance blocks after completing operations
- Use index-level blocks instead of cluster-level when possible
