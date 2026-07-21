---
title: "[Solution] Prometheus Rule Group Error"
description: "Fix Prometheus rule group errors. Resolve invalid rule group definitions causing evaluation failures."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Rule Group Error

Prometheus rule group errors occur when a rule group is malformed, contains invalid PromQL, or has conflicting rule names, preventing the group from being evaluated.

## Common Causes

- Duplicate record names within the same rule group
- Invalid PromQL expression in a rule
- Rule group interval set to zero or negative
- Rules referencing metrics that do not exist yet

## How to Fix It

### Solution 1: Check rule group syntax

Validate the rule file:

```bash
promtool check rules /etc/prometheus/rules/my_rules.yml
```

### Solution 2: Test rule expressions

Test PromQL expressions individually:

```bash
promtool test rules /etc/prometheus/rules/test_file.yml
```

### Solution 3: Fix duplicate record names

Ensure unique record names within a group:

```yaml
groups:
  - name: http_metrics
    rules:
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
      - record: job:http_errors:rate5m
        expr: sum(rate(http_requests_total{code=~"5.."}[5m])) by (job)
```

## Prevent It

- Run promtool check rules as part of CI/CD
- Use unique record names with a consistent naming scheme
- Test new rules against a dev Prometheus before production
