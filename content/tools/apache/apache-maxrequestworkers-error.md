---
title: "[Solution] Apache MaxRequestWorkers Reached Error"
description: "Fix Apache MaxRequestWorkers limit reached when all worker threads or processes are occupied."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache MaxRequestWorkers Reached Error

Apache reaches the MaxRequestWorkers limit and cannot accept new connections.

```
AH00484: server reached MaxRequestWorkers setting, consider raising MaxRequestWorkers
```

## Common Causes

- MaxRequestWorkers set too low for traffic
- Slow requests keeping workers occupied
- KeepAlive timeout too high
- Backend responses taking too long
- Insufficient system memory for more workers

## How to Fix

### Check Current Settings

```bash
# View current MPM settings
apachectl -V | grep -i mpm
# Check active connections
apachectl -t status
```

### Adjust MaxRequestWorkers

```apache
# For event MPM (recommended)
<IfModule mpm_event_module>
    StartServers 2
    MinSpareThreads 25
    MaxSpareThreads 250
    ThreadLimit 64
    ThreadsPerChild 25
    MaxRequestWorkers 400
    MaxConnectionsPerChild 1000
</IfModule>
```

### Reduce KeepAlive Timeout

```apache
KeepAlive On
KeepAliveTimeout 3
MaxKeepAliveRequests 100
```

### Use Timeout for Slow Requests

```apache
# Reduce timeout to free workers faster
Timeout 60
```

### Monitor Worker Usage

```bash
# Enable mod_status for monitoring
a2enmod status

# Check status page
curl http://localhost/server-status
```

## Examples

```bash
# Calculate appropriate MaxRequestWorkers
# Total RAM / (RAM per worker) = MaxRequestWorkers
# Example: 4GB / 10MB = ~400 workers
```

```apache
# event MPM for high-traffic sites
<IfModule mpm_event_module>
    StartServers 4
    MinSpareThreads 75
    MaxSpareThreads 250
    ThreadsPerChild 25
    MaxRequestWorkers 600
    MaxConnectionsPerChild 0
</IfModule>
```
