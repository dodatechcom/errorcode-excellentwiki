---
title: "[Solution] Prometheus DNS Service Discovery Error"
description: "How to fix Prometheus DNS-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- DNS SRV record lookup failure
- DNS server unreachable
- Wrong DNS name specified
- TTL expired on DNS records

## How to Fix

Configure DNS SD:

```yaml
scrape_configs:
  - job_name: 'dns-sd'
    dns_sd_configs:
      - names:
          - '_prometheus._tcp.example.com'
        type: SRV
        refresh_interval: 30s
```

## Examples

```bash
# Test DNS SRV lookup
dig _prometheus._tcp.example.com SRV

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_dns_name != null)'

# Test DNS resolution
nslookup example.com
```
