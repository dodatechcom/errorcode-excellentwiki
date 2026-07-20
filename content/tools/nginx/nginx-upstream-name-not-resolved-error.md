---
title: "[Solution] Nginx Upstream Name Not Resolved Error"
description: "The hostname in the upstream block could not be resolved to an IP address."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The hostname in the upstream block could not be resolved to an IP address.

## Common Causes

- **Domain does not exist** or misspelled
- **DNS not available** during startup
- **Temporary DNS outage**

## How to Fix

1. Verify: `dig backend.example.com +short`
2. Use IPs for static upstreams
3. Use resolver with variable for dynamic
4. Add to /etc/hosts as temporary fix

## Examples

**Static (IP-based):**
```nginx
upstream backend { server 10.0.0.1:8080; server 10.0.0.2:8080; }
```
**Dynamic with resolver:**
```nginx
resolver 8.8.8.8 valid=300s;
location / { proxy_pass http://backend.example.com:8080; }
```