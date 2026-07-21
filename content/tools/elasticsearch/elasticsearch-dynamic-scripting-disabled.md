---
title: "[Solution] Elasticsearch Dynamic Scripting Disabled Error"
description: "Fix Elasticsearch dynamic scripting disabled error. Resolve script execution permission issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Dynamic Scripting Disabled Error

Dynamic scripting is disabled. Inline scripts and script queries cannot execute.

## Common Causes

- Scripting is disabled for security
- script.inline is false in elasticsearch.yml
- Security plugin blocks scripts

## How to Fix

### Solution 1

```bash
grep 'script.inline\|script.stored' /etc/elasticsearch/elasticsearch.yml
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
