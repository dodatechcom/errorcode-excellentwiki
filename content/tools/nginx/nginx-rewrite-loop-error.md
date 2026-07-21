---
title: "[Solution] Nginx Rewrite Loop Error"
description: "Nginx rewrite rules create an infinite redirect loop, causing the browser to display an error or the server to return a redirect loop response."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Rewrite Loop Error

Nginx rewrite rules transform request URIs. A rewrite loop occurs when a rule rewrites a URI to a value that triggers the same rule again indefinitely.

## Common Causes

- A rewrite rule matches its own output URI
- The `if` condition matches the rewritten request
- Missing `$uri` vs `$request_uri` distinction causes repeated matching
- Redirect rules lack a condition to stop after the first rewrite

## How to Fix

1. Use `$uri` instead of `$request_uri` to check the current state:

```nginx
location /old-page {
    if ($uri = /old-page) {
        return 301 /new-page;
    }
}
```

2. Use a condition variable to prevent loops:

```nginx
set $redirect_done 0;

location / {
    if ($request_uri ~ "^/old-path" ) {
        set $redirect_done 1;
        return 301 /new-path;
    }
}
```

3. Use the `rewrite` directive with the `last` or `break` flag:

```nginx
location /old {
    rewrite ^/old/(.*)$ /new/$1 last;  # last stops processing
}
```

4. Check redirect chain with curl:

```bash
curl -vL http://localhost/old-page 2>&1 | grep "< location"
```

## Examples

```nginx
# Loop-causing configuration
location / {
    rewrite ^(.*)$ /index.html last;  # always matches
}

# Fixed configuration
location / {
    rewrite ^/$ /index.html last;
}

# Redirect HTTP to HTTPS without loop
server {
    listen 80;
    return 301 https://$host$request_uri;
}
```

```nginx
# Conditional redirect
location /blog {
    if ($request_uri ~* ^/blog/(\d+)$) {
        return 301 /post/$1;
    }
}
```

## Related Errors

- [Rewrite Cycle]({{< relref "/tools/nginx/nginx-rewrite-cycle-error" >}}) -- rewrite cycles
- [Redirect Loop]({{< relref "/tools/nginx/nginx-redirect-loop-error" >}}) -- redirect loops
