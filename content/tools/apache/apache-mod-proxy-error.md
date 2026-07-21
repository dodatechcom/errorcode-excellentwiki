---
title: "[Solution] Apache mod_proxy Error"
description: "Fix Apache mod_proxy errors when reverse proxy fails to connect to backend servers."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache mod_proxy Error

Apache mod_proxy fails to forward requests to the configured backend server.

```
AH00898: proxy: HTTP: failed to enable connection to backend server
```

## Common Causes

- Backend server not running or unreachable
- ProxyPass directive misconfigured
- Missing proxy modules
- Connection refused by backend
- SSL/TLS mismatch between Apache and backend

## How to Fix

### Enable Required Modules

```bash
a2enmod proxy
a2enmod proxy_http
a2enmod proxy_balancer
systemctl restart apache2
```

### Configure ProxyPass

```apache
ProxyPass "/app" "http://localhost:3000"
ProxyPassReverse "/app" "http://localhost:3000"
```

### Fix Connection Refused

```apache
# Set connection timeout and retry
<Proxy "http://backend:3000">
    ProxyPass http://backend:3000/connectiontimeout=5 timeout=30 keepalive=On
</Proxy>
```

### Configure Proxy with Headers

```apache
<Proxy "http://backend:3000/*">
    ProxyPass http://backend:3000/
    ProxyPassReverse http://backend:3000/
    RequestHeader set X-Forwarded-Proto "https"
    RequestHeader set X-Real-IP "%{REMOTE_ADDR}s"
    ProxyPreserveHost On
</Proxy>
```

### Exclude from Proxy

```apache
# Do not proxy certain paths
ProxyPass "/static" "!"
ProxyPass "/api" "http://backend:3000"
```

## Examples

```apache
# Load balanced proxy
<Proxy balancer://backend>
    BalancerMember http://server1:3000
    BalancerMember http://server2:3000
    ProxySet lbmethod=byrequests
</Proxy>
ProxyPass "/app" "balancer://backend"
ProxyPassReverse "/app" "balancer://backend"
```
