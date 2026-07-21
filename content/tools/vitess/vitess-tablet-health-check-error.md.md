---
title: "Vitess Tablet Health Check Error"
description: "Tablet health check failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet health checks are failing.

## Common Causes
- MySQL replication lag
- Tablet process crashed
- Health check timeout

## How to Fix
```bash
# Check tablet health
vtctlclient ListTablets

# Restart tablet
vtctlclient RestartTablet <tablet-alias>
```

## Examples
```bash
# Check health endpoint
curl http://localhost:15100/debug/health
# Tablet should return 200 OK
```

