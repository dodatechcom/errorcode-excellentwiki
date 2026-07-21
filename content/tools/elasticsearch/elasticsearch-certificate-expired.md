---
title: "[Solution] Elasticsearch Certificate Expired Error"
description: "Fix Elasticsearch certificate expired error. Resolve certificate lifecycle issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Certificate Expired Error

The TLS certificate has expired. Nodes cannot establish secure connections.

## Common Causes

- Certificate has expired
- Certificate was not renewed
- Certificate validity period is too short

## How to Fix

### Solution 1

```bash
openssl x509 -in /etc/elasticsearch/certs/http.crt -noout -dates
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
