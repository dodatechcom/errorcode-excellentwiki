---
title: "[Solution] Elasticsearch Security Not Enabled Error"
description: "Fix Elasticsearch security not enabled error. Resolve security plugin configuration issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Security Not Enabled Error

Security features are not enabled. The cluster is running without authentication or authorization.

## Common Causes

- Security plugin is not enabled
- xpack.security.enabled is false
- Security features are disabled in config

## How to Fix

### Solution 1

```bash
grep 'xpack.security.enabled' /etc/elasticsearch/elasticsearch.yml
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
