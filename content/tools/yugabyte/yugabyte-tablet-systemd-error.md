---
title: "[Solution] YugabyteDB Tablet Systemd Error"
description: "How to fix YugabyteDB tablet systemd errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Service not starting
- Service crash looping
- Service not enabled

## How to Fix

```bash
systemctl status yb-tserver
```

## Examples

```bash
journalctl -u yb-tserver --since '5 minutes ago'
```
