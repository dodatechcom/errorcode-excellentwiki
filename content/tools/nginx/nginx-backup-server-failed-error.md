---
title: "[Solution] Nginx Backup Server Failed Error"
description: "A backup server in the upstream block is unreachable or misconfigured."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

A backup server in the upstream block is unreachable or misconfigured.

## Common Causes

- **Backup server also down**
- **Port mismatch**
- **Not listening** on expected address
- **Firewall blocking**

## How to Fix

1. Verify: `curl -I http://backup:8080/health`
2. Ensure same config as primaries
3. Add multiple backups for redundancy

## Examples

**Test:**
```bash
for s in 10.0.0.1 10.0.0.2 10.0.0.3; do
    echo -n "$s:8080 -> "
    curl -s -o /dev/null -w "%{http_code}" http://$s:8080/health
done
```