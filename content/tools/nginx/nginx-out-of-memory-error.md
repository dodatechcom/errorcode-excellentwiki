---
title: "[Solution] Nginx Out of Memory Error"
description: "Nginx worker process was killed by the OOM killer due to excessive memory usage."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx worker process was killed by the OOM killer due to excessive memory usage.

## Common Causes

- **Large client body buffering**
- **Too many workers**
- **Memory leak** in module
- **Large proxy buffers/cache**
- **High concurrency**

## How to Fix

1. Reduce buffers: `client_body_buffer_size 8k; proxy_buffer_size 4k;`
2. Limit workers: `worker_processes 4;`
3. Monitor: `ps aux | grep nginx | awk '{sum+=$6} END {print sum/1024 " MB"}'`
4. Check: `free -h`

## Examples

**Memory-conscious:**
```nginx
worker_processes 4;
worker_rlimit_nofile 16384;
events { worker_connections 4096; }
http {
    client_body_buffer_size 8k;
    proxy_buffer_size 4k;
    proxy_buffers 4 4k;
}
```