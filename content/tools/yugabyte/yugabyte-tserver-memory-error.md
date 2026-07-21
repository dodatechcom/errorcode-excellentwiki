---
title: "[Solution] YugabyteDB TServer Memory Error"
description: "How to fix YugabyteDB TServer memory errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- TServer OOM
- Too many concurrent queries
- Memory limit too low

## How to Fix

```bash
yb-admin list_tablet_servers
```

## Examples

```bash
free -h
```
