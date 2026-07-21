---
title: "[Solution] Nginx Upstream Not Found Error"
description: "Nginx cannot find the upstream server block referenced in a proxy_pass or other directive, causing a configuration error."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Upstream Not Found Error

Nginx upstream blocks define groups of backend servers. This error occurs when a `proxy_pass`, `fastcgi_pass`, or similar directive references an upstream name that is not defined.

## Common Causes

- The `upstream` block name is misspelled in the `proxy_pass` directive
- The upstream block is defined in a different server or http context
- The upstream name includes characters that are not valid
- The upstream block is commented out or removed

## How to Fix

1. Verify the upstream block is defined:

```nginx
upstream backend {
    server 127.0.0.1:8080;
    server 127.0.0.1:8081;
}
```

2. Ensure the proxy_pass references the correct upstream name:

```nginx
server {
    listen 80;
    location / {
        proxy_pass http://backend;  # must match upstream name
    }
}
```

3. Place the upstream block in the correct context:

```nginx
# upstream blocks must be in http context, not inside server
http {
    upstream backend {
        server 127.0.0.1:8080;
    }

    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }
}
```

4. Test the configuration before reload:

```bash
nginx -t
```

## Examples

```nginx
# Error configuration
upstream app-servers {
    server 127.0.0.1:8080;
}

server {
    location / {
        proxy_pass http://app-server;  # typo: missing 's'
    }
}
```

```nginx
# Fixed configuration
upstream app-servers {
    server 127.0.0.1:8080;
}

server {
    location / {
        proxy_pass http://app-servers;  # correct name
    }
}
```

## Related Errors

- [Upstream Error]({{< relref "/tools/nginx/nginx-upstream-error" >}}) -- upstream connection failures
- [Proxy Pass Error]({{< relref "/tools/nginx/nginx-proxy-pass-error" >}}) -- proxy configuration issues
