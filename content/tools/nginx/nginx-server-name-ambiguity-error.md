---
title: "[Solution] Nginx Server Name Ambiguity Error"
description: "Nginx cannot determine which server block to use for a request because multiple server blocks share the same server_name and listen directives."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

# Nginx Server Name Ambiguity Error

Nginx selects a server block based on the `server_name` and `listen` directives. An ambiguity error occurs when multiple server blocks match a request equally, causing unpredictable routing.

## Common Causes

- Two server blocks listen on the same port with the same `server_name`
- A catch-all `server_name _` conflicts with specific server names
- The `default_server` flag is applied to multiple listen directives
- Server name matching priority is not understood (exact > wildcard > regex)

## How to Fix

1. Ensure each server block has a unique `server_name`:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
}

server {
    listen 80;
    server_name api.example.com;
}
```

2. Set a single default server:

```nginx
server {
    listen 80 default_server;
    server_name _;
    return 444;  # close connection
}

server {
    listen 80;
    server_name example.com;
    # your application
}
```

3. Check the Nginx configuration for duplicate server names:

```bash
nginx -T | grep "server_name"
```

4. Use `listen` directives to differentiate server blocks:

```nginx
server {
    listen 80;
    listen 443 ssl;
    server_name example.com;
}
```

## Examples

```bash
# Error output
nginx: [warn] conflicting server name "example.com" on 0.0.0.0:80, ignored
```

```nginx
# Correct -- unique server names
server {
    listen 80;
    server_name example.com;
    root /var/www/example;
}

server {
    listen 80;
    server_name admin.example.com;
    root /var/www/admin;
}
```

## Related Errors

- [Conflicting Server Name]({{< relref "/tools/nginx/nginx-conflicting-server-name-error" >}}) -- duplicate server names
- [Duplicate Server Name]({{< relref "/tools/nginx/nginx-duplicate-server-name-error" >}}) -- repeated server names
