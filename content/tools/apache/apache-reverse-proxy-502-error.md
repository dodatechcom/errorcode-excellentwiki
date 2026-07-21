---
title: "[Solution] Apache Reverse Proxy 502 Bad Gateway"
description: "Fix Apache reverse proxy 502 Bad Gateway errors when the backend is unreachable or times out."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Reverse Proxy 502 Bad Gateway

Apache returns a 502 Bad Gateway because the upstream server is unreachable.

```
AH00898: Error contacting backend server
proxy: HTTP: client denied by server configuration
```

## Common Causes

- Backend server not running
- Backend listening on wrong port
- Connection timeout too short
- Backend rejecting connections
- DNS resolution failing for backend hostname

## How to Fix

### Verify Backend is Running

```bash
# Check backend connectivity
curl -v http://localhost:3000/health
netstat -tlnp | grep 3000
```

### Adjust Proxy Timeout

```apache
# Increase proxy timeouts
<Proxy "http://backend:3000">
    ProxyPass http://backend:3000/connectiontimeout=10 timeout=60
</Proxy>
```

### Configure Proxy Retry

```apache
ProxyPass "/app" "http://backend:3000" retry=5 connectiontimeout=5 timeout=30
ProxyPassReverse "/app" "http://backend:3000"
```

### Use ProxyPassMatch for Flexible Routing

```apache
ProxyPassMatch "^/api/(.*)$" "http://backend:3000/$1" timeout=60
ProxyPassReverse "/api" "http://backend:3000"
```

### Add Custom 502 Error Page

```apache
ErrorDocument 502 /502.html
```

## Examples

```apache
# Load balanced with health checks
<Proxy balancer://app>
    BalancerMember http://server1:3000 route=node1
    BalancerMember http://server2:3000 route=node2
    ProxySet lbmethod=byrequests
</Proxy>

ProxyPass "/app" "balancer://app" timeout=30 retry=10
ProxyPassReverse "/app" "balancer://app"
```
