---
title: "[Solution] Nginx Resolver Error"
description: "Nginx DNS resolver fails to resolve upstream server hostnames, causing proxy_pass and other directives to fail at runtime."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Resolver Error

Nginx uses a DNS resolver to look up upstream server hostnames at runtime. A resolver error occurs when Nginx cannot reach the DNS server or the hostname cannot be resolved.

## Common Causes

- The `resolver` directive is missing or points to an unreachable DNS server
- The upstream uses a hostname that does not have a DNS record
- The resolver `valid` timeout is too short for DNS propagation
- The system resolv.conf is misconfigured

## How to Fix

1. Configure the DNS resolver in the http or server block:

```nginx
http {
    resolver 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 5s;
}
```

2. Use a variable for dynamic upstream resolution:

```nginx
server {
    listen 80;

    location / {
        set $backend http://backend.example.com:8080;
        proxy_pass $backend;
    }
}
```

3. Verify DNS resolution works:

```bash
nslookup backend.example.com
dig backend.example.com
```

4. Set the resolver with IPv6 support:

```nginx
resolver 8.8.8.8 [2001:4860:4860::8888] valid=300s ipv6=off;
```

## Examples

```bash
# Error output
nginx: [emerg] no resolver defined to resolve backend.example.com
```

```nginx
# Dynamic upstream resolution with resolver
http {
    resolver 127.0.0.1 valid=10s;

    server {
        listen 80;

        location / {
            set $upstream http://backend:8080;
            proxy_pass $upstream;
        }
    }
}
```

## Related Errors

- [DNS Error]({{< relref "/tools/nginx/nginx-dns-error" >}}) -- DNS resolution failures
- [Upstream Name Not Resolved]({{< relref "/tools/nginx/nginx-upstream-name-not-resolved-error" >}}) -- hostname resolution
