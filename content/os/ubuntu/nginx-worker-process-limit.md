---
title: "Nginx Worker Process Limit Error"
description: "Nginx worker processes exceed system limit or cause resource exhaustion"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Nginx Worker Process Limit Error

Nginx worker processes exceed system limit or cause resource exhaustion

## Common Causes

- worker_processes set higher than CPU cores
- Each worker consuming excessive memory
- Too many worker connections configured
- No file descriptor limit set for workers

## How to Fix

1. Check worker count: `ps aux | grep nginx | grep worker | wc -l`
2. Set worker_processes auto (matches CPU cores)
3. Limit worker_connections: `worker_connections 1024;`
4. Check file limits: `ulimit -n`

## Examples

```nginx
# Optimize worker configuration
worker_processes auto;
worker_rlimit_nofile 65535;
events {
    worker_connections 1024;
}
```
