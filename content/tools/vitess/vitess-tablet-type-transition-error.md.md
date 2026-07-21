---
title: "Vitess Tablet Type Transition Error"
description: "Tablet type transition failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet type transition is failing.

## Common Causes
- Invalid type transition
- Type not supported
- Promotion rules violated

## How to Fix
```bash
# Check tablet type
vtctlclient ListTablets

# Set tablet type
vtctlclient SetTabletType <tablet-alias> REPLICA
```

## Examples
```bash
# Check tablet stats
curl http://localhost:15100/debug/vars | jq '.TabletType'
# Monitor type changes
curl http://localhost:15001/debug/vars | jq '.TabletTypes'
```

