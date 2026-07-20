---
title: "[Solution] Nginx Upstream Has No Suitable Server Error"
description: "All servers in the upstream were skipped due to constraints like down, backup, or max_fails."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

All servers in the upstream were skipped due to constraints like down, backup, or max_fails.

## Common Causes

- **All primary servers down** and no backup
- **Backup servers** cannot serve regular traffic
- **max_fails exceeded** on all servers
- **slow_start** preventing immediate use

## How to Fix

1. Remove `down` markers
2. Add non-backup servers
3. Reduce max_fails sensitivity
4. Validate: `sudo nginx -t`

## Examples

**Balanced:**
```nginx
upstream backend {
    server 10.0.0.1:8080 max_fails=3 fail_timeout=60s;
    server 10.0.0.2:8080 max_fails=3 fail_timeout=60s;
    server 10.0.0.3:8080 backup;
}
```