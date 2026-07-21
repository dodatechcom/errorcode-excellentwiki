---
title: "[Solution] Apache ServerLimit Error"
description: "Fix Apache ServerLimit errors when the maximum number of child processes is exceeded."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache ServerLimit Error

Apache cannot spawn additional child processes because the ServerLimit is reached.

```
AH00484: server reached ServerLimit setting, consider raising ServerLimit
```

## Common Causes

- ServerLimit too low for concurrent connections
- High KeepAlive timeout keeping idle servers
- Backend slowness keeping servers busy
- Insufficient RAM for more processes
- Traffic spike exceeding expected load

## How to Fix

### Increase ServerLimit

```apache
<IfModule mpm_prefork_module>
    ServerLimit 512
    MaxRequestWorkers 512
</IfModule>

<IfModule mpm_worker_module>
    ServerLimit 50
    MaxRequestWorkers 400
    ThreadsPerChild 8
</IfModule>
```

### Calculate Required Limit

```bash
# Estimate peak concurrent connections
# Check current usage
apachectl -t status 2>&1 | grep "Total accesses"

# For worker/event MPM
# MaxRequestWorkers = ServerLimit * ThreadsPerChild
```

### Reduce KeepAlive Impact

```apache
KeepAliveTimeout 2
MaxKeepAliveRequests 100
```

### Switch to Event MPM for Better Efficiency

```bash
a2dismod mpm_prefork
a2enmod mpm_event
systemctl restart apache2
```

### Monitor Server Usage

```bash
# Enable mod_status
a2enmod status

# Check scoreboard
curl -s http://localhost/server-status?auto
```

## Examples

```apache
# High-traffic event MPM configuration
<IfModule mpm_event_module>
    StartServers 4
    MinSpareThreads 75
    MaxSpareThreads 250
    ThreadLimit 64
    ThreadsPerChild 25
    MaxRequestWorkers 1000
    ServerLimit 40
    MaxConnectionsPerChild 10000
</IfModule>
```
