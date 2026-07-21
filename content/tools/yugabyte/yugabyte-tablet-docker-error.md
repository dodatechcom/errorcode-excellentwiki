---
title: "[Solution] YugabyteDB Tablet Docker Error"
description: "How to fix YugabyteDB tablet Docker errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Container not starting
- Container OOMKilled
- Container networking issue

## How to Fix

```bash
docker ps | grep yugabyte
```

## Examples

```bash
docker logs yb-tserver-1
```
