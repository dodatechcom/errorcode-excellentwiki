---
title: "[Solution] Elasticsearch Geo Distance Error"
description: "Fix Elasticsearch geo distance error. Resolve geo_distance query issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch Geo Distance Error

The geo_distance query fails due to invalid coordinates or field mapping.

## Common Causes

- Geo point field has invalid coordinates
- Distance unit is not recognized
- Field is not mapped as geo_point

## How to Fix

### Solution 1

```bash
curl -X GET 'localhost:9200/myindex/_search' -H 'Content-Type: application/json' -d '{"query":{"bool":{"must":{"match_all":{}},"filter":{"geo_distance":{"distance":"200km","location":{"lat":40.73,"lon":-74.1}}}}}}'
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
