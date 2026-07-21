---
title: "[Solution] Elasticsearch Split Brain Error"
description: "Fix Elasticsearch split brain error. Resolve master election split-brain scenarios."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Split Brain Error

A split-brain scenario occurs where two separate master nodes are elected, leading to data inconsistency.

## Common Causes

- Minimum master nodes config is incorrect
- Network partition divides the cluster
- Discovery config allows separate quorums

## How to Fix

### Solution 1

```bash
grep -i 'minimum_master_nodes\|discovery.seed_hosts' /etc/elasticsearch/elasticsearch.yml
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
