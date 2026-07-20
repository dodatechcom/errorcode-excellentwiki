---
title: "[Solution] Nginx IP Hash Unbalanced Error"
description: "The ip_hash algorithm distributes traffic unevenly due to NAT gateways or proxy IPs."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The ip_hash algorithm distributes traffic unevenly due to NAT gateways or proxy IPs.

## Common Causes

- **Large NAT gateways** funneling many users
- **CDN or proxy IPs** aggregating traffic
- **Few public IPs** in pool

## How to Fix

1. Use hash with $request_id
2. Consider least_conn instead
3. Use weighted servers
4. Monitor: `awk '{print $1}' access.log | sort | uniq -c | sort -rn | head`

## Examples

**Alternative:**
```nginx
upstream backend {
    hash $remote_addr consistent;
    server 10.0.0.1:8080; server 10.0.0.2:8080;
}
```