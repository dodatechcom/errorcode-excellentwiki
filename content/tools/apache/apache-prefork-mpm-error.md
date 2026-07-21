---
title: "[Solution] Apache Prefork MPM Error"
description: "Fix Apache prefork MPM errors when process spawning fails under high concurrency."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Prefork MPM Error

Apache prefork MPM spawns too many processes or fails to spawn new workers.

```
AH00485: scoreboard is full, but not MaxRequestWorkers
```

## Common Causes

- MaxRequestWorkers set too high for available RAM
- ProcessLimit reached
- KeepAliveTimeout too long keeping idle processes
- mod_php or mod_perl causing memory leaks
- Spawn rate too slow for traffic spikes

## How to Fix

### Tune Prefork MPM

```apache
<IfModule mpm_prefork_module>
    StartServers 5
    MinSpareServers 5
    MaxSpareServers 10
    ServerLimit 256
    MaxRequestWorkers 256
    MaxConnectionsPerChild 10000
</IfModule>
```

### Calculate RAM per Process

```bash
# Check current process memory usage
ps aux | grep apache2 | awk '{print $6}' | sort -n | tail

# Calculate max workers: Total RAM / Average process size
# Example: 4GB / 20MB = ~200 workers
```

### Reduce KeepAlive Overhead

```apache
KeepAlive On
KeepAliveTimeout 3
MaxKeepAliveRequests 50
```

### Switch to Event MPM

```bash
a2dismod mpm_prefork
a2enmod mpm_event
systemctl restart apache2
```

### Monitor Process Count

```bash
# Watch process count
watch -n 1 'ps aux | grep apache2 | wc -l'

# Check scoreboard
curl -s http://localhost/server-status?auto | grep BusyWorkers
```

## Examples

```apache
# Conservative prefork for small servers
<IfModule mpm_prefork_module>
    StartServers 2
    MinSpareServers 2
    MaxSpareServers 5
    ServerLimit 64
    MaxRequestWorkers 64
    MaxConnectionsPerChild 5000
</IfModule>
```
