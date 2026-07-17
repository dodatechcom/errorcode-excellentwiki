---
title: "[Solution] Nginx worker process — exited on signal"
description: "Fix Nginx worker process exited on signal. Resolve worker process crashes and signal issues."
tools: ["nginx"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A worker process exited on signal means an Nginx worker process was terminated unexpectedly by the operating system or a signal, causing request processing to fail. This indicates a critical issue with the Nginx process or system resources.

## What This Error Means

Nginx runs a master process that spawns worker processes to handle requests. When a worker receives a fatal signal (SIGSEGV, SIGBUS, SIGKILL, OOM killer), it exits abnormally. The master process typically respawns a new worker, but during the transition, some requests may fail. Frequent worker exits indicate a serious problem — memory corruption, resource exhaustion, or a bug in an Nginx module.

## Common Causes

- Out of memory: OS OOM killer terminated the worker
- Segmentation fault in a third-party Nginx module
- Shared memory zone (rate limiting, caching) corruption
- File descriptor limit reached (too many open connections)
- Disk full causing write failures that crash workers
- Worker process hit resource limits (RLIMIT_NOFILE)

## How to Fix

### Check Nginx Error Logs

```bash
sudo tail -f /var/log/nginx/error.log | grep -i "signal\|crash\|segfault\|worker"
```

### Check System Logs for OOM

```bash
dmesg | grep -i "oom\|killed"
sudo journalctl -k | grep -i "oom"
```

### Increase Worker Connection Limits

```nginx
events {
    worker_connections 4096;
    multi_accept on;
}
```

### Check File Descriptor Limits

```bash
# Check current limits
ulimit -n

# Increase in /etc/security/limits.conf
www-data soft nofile 65535
www-data hard nofile 65535
```

### Check System-Wide Limits

```bash
# /etc/sysctl.conf
fs.file-max = 2097152
net.core.somaxconn = 65535
```

### Increase Shared Memory Zones

```nginx
# Ensure adequate shared memory
limit_req_zone $binary_remote_addr zone=api:20m rate=10r/s;
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:100m;
```

### Monitor Memory Usage

```bash
# Watch Nginx memory
ps aux | grep nginx
top -p $(pgrep -d, nginx)
```

### Check for Module Issues

```bash
# Verify Nginx modules
nginx -V 2>&1 | grep -o "add-module=.*"
# Remove problematic third-party modules
```

### Check Disk Space

```bash
df -h /var/log/nginx
df -h /var/cache/nginx
```

## Related Errors

- [Nginx 502 Bad Gateway]({{< relref "/tools/nginx/nginx-502-error-v2" >}}) — upstream connection closed
- [Nginx 504 Timeout]({{< relref "/tools/nginx/nginx-504-error-v2" >}}) — upstream timed out
- [Nginx Limit Request]({{< relref "/tools/nginx/nginx-limit-req-v2" >}}) — rate limiting 503
