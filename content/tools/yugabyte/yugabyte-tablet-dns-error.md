---
title: "[Solution] YugabyteDB Tablet DNS Error"
description: "How to fix YugabyteDB tablet DNS errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- DNS resolution failing
- DNS timeout
- DNS cache stale

## How to Fix

```bash
nslookup tikv-host
```

## Examples

```bash
dig tikv-host
```
