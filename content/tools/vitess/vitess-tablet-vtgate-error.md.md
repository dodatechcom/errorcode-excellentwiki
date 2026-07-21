---
title: "Vitess Tablet VTGate Error"
description: "Tablet VTGate communication failure"
tools:
  - vitess
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Tablet cannot communicate with VTGate.

## Common Causes
- VTGate process down
- Network connectivity issue
- gRPC connection failed

## How to Fix
```bash
# Check VTGate status
curl http://localhost:15001/debug/health

# Check network connectivity
telnet vtgate-host 15999
```

## Examples
```bash
# Check VTGate logs
tail -100 /var/log/vtgate/vtgate.log
# Monitor VTGate metrics
curl http://localhost:15001/debug/vars
```

