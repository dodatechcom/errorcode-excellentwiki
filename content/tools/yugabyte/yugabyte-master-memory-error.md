---
title: "[Solution] YugabyteDB Master Memory Error"
description: "How to fix YugabyteDB master memory errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Master OOM
- Too many tablets to track
- Memory limit too low

## How to Fix

```bash
yb-admin list_masters
```

## Examples

```bash
free -h
```
