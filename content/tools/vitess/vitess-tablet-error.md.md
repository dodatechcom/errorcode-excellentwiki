---
title: "Vitess Tablet Error"
description: "Tablet operation failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet operation is failing.

## Common Causes
- Tablet process crashed
- Disk space exhausted
- Memory pressure

## How to Fix
```bash
# Check tablet status
vtctlclient ListTablets

# Restart tablet
vtctlclient RestartTablet <tablet-alias>
```

## Examples
```bash
# Check tablet logs
tail -100 /var/log/vttablet/vttablet.log
# Monitor tablet metrics
curl http://localhost:15100/debug/vars
```

