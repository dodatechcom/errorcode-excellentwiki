---
title: "YugabyteDB Load Balancer Error Code"
description: "Load balancer error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Load balancer returning specific error code.

## Common Causes
- Load balancer disabled
- Tablet move failing
- Imbalance threshold too high

## How to Fix
```bash
# Check load balancer status
curl http://localhost:9000/metrics | grep load_balancer

# Trigger rebalance
yb-admin leader_rebalancer
```

## Examples
```bash
# Check tablet distribution
yb-admin list_tablets | awk '{print $2}' | sort | uniq -c
# Monitor load
curl http://localhost:9000/metrics | grep load
```

