---
title: "Vitess Tablet Replication Health Error"
description: "Tablet replication health failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet replication health check is failing.

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

