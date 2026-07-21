---
title: "[Solution] Prometheus PuppetDB Service Discovery Error"
description: "How to fix Prometheus PuppetDB-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- PuppetDB API unreachable
- Wrong query language (PQL vs AST)
- SSL certificate not configured
- PuppetDB returned empty results

## How to Fix

Configure PuppetDB SD:

```yaml
scrape_configs:
  - job_name: 'puppetdb'
    puppetdb_sd_configs:
      - url: 'https://puppetdb.example.com:8081/pdb/query'
        query: 'inventory { facts.networking.ip != "0.0.0.0"}'
        port: 9100
```

## Examples

```bash
# Test PuppetDB API
curl -k https://puppetdb:8081/pdb/query/v4/status

# Query nodes
curl -k -X POST https://puppetdb:8081/pdb/query/v4/nodes -d '{"query":"nodes {}"}'

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_puppetdb != null)'
```
