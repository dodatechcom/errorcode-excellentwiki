---
title: "[Solution] Nginx DNS Resolution Error"
description: "Fix Nginx dns resolution errors. Learn why this happens and how to resolve it quickly."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Nginx DNS Resolution Error

Nginx DNS resolution errors occur when Nginx cannot resolve upstream server hostnames.

## Why This Happens

- DNS not configured
- Resolver unavailable
- Resolution failed
- Cache stale

## Common Error Messages

- `dns_not_configured_error`
- `dns_resolver_error`
- `dns_resolution_error`
- `dns_cache_error`

## How to Fix It

### Solution 1: Configure resolver

Set up DNS resolver:

```nginx
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
```

### Solution 2: Fix DNS issues

Verify DNS resolution:

```bash
nslookup upstream-server
```

### Solution 3: Use IP addresses

Use IPs instead of hostnames if DNS is unreliable.


## Common Scenarios

- **DNS not configured:** Add resolver directive.
- **Resolution failed:** Check DNS server configuration.

## Prevent It

- Configure DNS properly
- Use reliable resolvers
- Monitor DNS health
