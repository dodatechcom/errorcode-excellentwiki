---
title: "[Solution] Elasticsearch Cross-Cluster Search Error"
description: "Fix Elasticsearch cross-cluster search errors. Resolve issues connecting to remote clusters for CCS."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Cross-Cluster Search Error

Elasticsearch cross-cluster search errors occur when a local cluster cannot connect to or query a configured remote cluster.

## Common Causes

- Remote cluster seed nodes are unreachable
- TLS certificates not configured for remote connections
- Remote cluster proxy settings misconfigured
- Network firewall blocking inter-cluster ports

## Common Error Messages

- `no_such_remote_cluster`
- `remote_cluster_connection_failed`
- `cross_cluster_search_exception`

## How to Fix It

### Solution 1: Check remote cluster configuration

Verify the configured remote clusters:

```bash
curl -X GET "localhost:9200/_remote/info?pretty"
```

### Solution 2: Add remote cluster seed nodes

Configure a remote cluster:

```bash
curl -X PUT "localhost:9200/_cluster/settings" -H 'Content-Type: application/json' -d '{
  "persistent": {
    "cluster.remote.remote_prod.seeds": ["node1.remote_prod:9300", "node2.remote_prod:9300"]
  }
}'
```

### Solution 3: Test cross-cluster search

Run a search targeting the remote cluster:

```bash
curl -X GET "localhost:9200/remote_prod:myindex/_search?pretty" -H 'Content-Type: application/json' -d '{
  "query": { "match_all": {} }
}'
```

## Prevent It

- Ensure network connectivity on transport ports (9300)
- Verify TLS certificates match across clusters
- Monitor remote cluster connection status
