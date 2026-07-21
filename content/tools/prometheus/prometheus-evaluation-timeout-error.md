---
title: "[Solution] Prometheus Evaluation Timeout Error"
description: "Fix Prometheus evaluation timeout errors. Resolve rule evaluation failures from slow or complex queries."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Evaluation Timeout Error

Prometheus evaluation timeout errors occur when a recording rule or alerting rule takes longer than the configured evaluation interval or timeout to complete.

## Common Causes

- Recording rule query is too complex for the evaluation interval
- Slow queries scanning large numbers of time series
- Insufficient CPU or memory on the Prometheus server
- Evaluation interval set too short for the query complexity

## How to Fix It

### Solution 1: Increase the evaluation timeout

Set a longer rule evaluation timeout:

```yaml
rule_files:
  - /etc/prometheus/rules/*.yml

global:
  evaluation_interval: 1m

# In the rule file
groups:
  - name: slow-rules
    interval: 5m
    rules:
      - record: my:slow:metric
        expr: sum(rate(http_requests_total[5m])) by (job)
```

### Solution 2: Simplify the rule expression

Use less expensive PromQL expressions:

```yaml
# Avoid large group-by label sets
- record: simplified:metric
  expr: sum(http_requests_total) by (job)
```

### Solution 3: Check Prometheus resource usage

Monitor server performance:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | python3 -m json.tool
```

## Prevent It

- Set evaluation interval at least 2x the query duration
- Use recording rules for expensive queries
- Monitor Prometheus CPU and memory usage
