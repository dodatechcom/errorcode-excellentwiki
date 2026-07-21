---
title: "[Solution] Prometheus Target Fallback Scraped Error"
description: "Fix Prometheus target fallback errors. Resolve targets being scraped from fallback endpoints unexpectedly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Target Fallback Scraped Error

Prometheus target fallback scraped errors occur when a target falls back to an alternate endpoint due to the primary endpoint failing, resulting in unexpected metric labels or data.

## Common Causes

- Primary target endpoint returning HTTP errors
- DNS resolution failing and falling back to cached IPs
- Service mesh routing to a degraded replica
- Health check endpoint returning partial data

## How to Fix It

### Solution 1: Check target health status

View current target health in the Prometheus UI or API:

```bash
curl -s http://localhost:9090/api/v1/targets | python3 -m json.tool | grep -A 5 '"health"'
```

### Solution 2: Verify the primary endpoint

Test the target directly:

```bash
curl -v http://primary-endpoint:8080/metrics
curl -v http://fallback-endpoint:8080/metrics
```

### Solution 3: Remove or disable fallback scraping

If fallback data is incorrect, remove the fallback configuration:

```yaml
scrape_configs:
  - job_name: "my-app"
    static_configs:
      - targets: ["primary-app:8080"]
    # Remove or fix fallback targets
```

## Prevent It

- Monitor target health and alert on degraded states
- Use HTTPS endpoints with certificate validation
- Ensure fallback endpoints produce valid metrics
