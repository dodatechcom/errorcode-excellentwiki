---
title: "[Solution] Nginx Limit Conn Zone Missing Error"
description: "The limit_conn directive references a zone not defined with limit_conn_zone."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The limit_conn directive references a zone not defined with limit_conn_zone.

## Common Causes

- **limit_conn without limit_conn_zone**
- **Zone name typo**
- **Wrong context**

## How to Fix

1. Define: `limit_conn_zone $binary_remote_addr zone=conn_limit:10m;`
2. Verify name matches

## Examples

**Config:**
```nginx
http {
    limit_conn_zone $binary_remote_addr zone=per_ip:10m;
    limit_conn_zone $server_name zone=per_host:10m;
    server {
        location /large-files/ {
            limit_conn per_ip 5;
            limit_conn per_host 100;
            proxy_pass http://backend;
        }
    }
}
```