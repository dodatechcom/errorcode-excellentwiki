---
title: "[Solution] Prometheus Query Error"
description: "Fix Prometheus query errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Query Error

Prometheus query errors occur when PromQL expressions are invalid or return unexpected results.

## Why This Happens

- Invalid PromQL syntax
- Series not found
- Query timeout
- Label mismatch

## Common Error Messages

- `query_syntax_error`
- `series_not_found`
- `query_timeout`
- `label_error`

## How to Fix It

### Solution 1: Validate PromQL

Test your query in the Prometheus UI:

http://localhost:9090/graph

Use the Expression Browser to validate syntax.

### Solution 2: Check label names

Ensure label names are valid:

```promql
http_requests_total{method="GET"}
```

### Solution 3: Optimize long-running queries

Use recording rules for expensive queries:

```yaml
group:
  name: my_rules
  rules:
    - record: job:http_requests:rate5m
      expr: rate(http_requests_total[5m])
```


## Common Scenarios

- **Series not found:** Check if the metric is being scraped.
- **Query timeout:** Optimize the query or increase timeout.

## Prevent It

- Use recording rules
- Validate queries in UI
- Monitor query performance
