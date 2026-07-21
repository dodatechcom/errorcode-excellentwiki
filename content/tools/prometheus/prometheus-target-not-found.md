---
title: "[Solution] Prometheus Target Not Found"
description: "How to fix Prometheus target not found errors when scraping endpoints"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target endpoint is down or unreachable
- Wrong hostname or port in target configuration
- Firewall blocking the connection
- DNS resolution failure for target hostname
- Target application not exposing metrics endpoint

## How to Fix

Check target status in Prometheus UI:

```bash
curl http://localhost:9090/api/v1/targets | python3 -m json.tool
```

Verify target is reachable:

```bash
curl -v http://target-host:9090/metrics
```

Check DNS resolution:

```bash
nslookup target-host.example.com
```

Verify firewall rules:

```bash
sudo iptables -L -n | grep 9090
```

Update target address if needed:

```yaml
scrape_configs:
  - job_name: 'app'
    static_configs:
      - targets: ['correct-host:8080']
```

## Examples

```bash
# List all targets and their status
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, health: .health}'

# Test connectivity to target
nc -zv target-host 8080

# Check target labels
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[].labels'
```
