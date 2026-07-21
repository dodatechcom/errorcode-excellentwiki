---
title: "[Solution] YugabyteDB Tablet Logging Error"
description: "How to fix YugabyteDB tablet logging errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Log file not writable
- Log level too verbose
- Log rotation not working

## How to Fix

```bash
ls -la /var/log/yugabyte/
```

## Examples

```bash
journalctl -u yb-tserver --since '5 minutes ago' | grep -i error
```
