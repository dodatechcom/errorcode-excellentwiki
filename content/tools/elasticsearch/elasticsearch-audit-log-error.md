---
title: "[Solution] Elasticsearch Audit Log Error"
description: "Fix Elasticsearch audit log error. Resolve audit logging issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Audit Log Error

Audit logging is not working. Audit events are not being recorded.

## Common Causes

- Audit logging is not enabled
- Audit log destination is not writable
- Audit event filters are wrong

## How to Fix

### Solution 1

```bash
grep 'xpack.security.audit' /etc/elasticsearch/elasticsearch.yml
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
