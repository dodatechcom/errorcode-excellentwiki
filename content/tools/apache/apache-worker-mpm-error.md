---
title: "[Solution] Apache Worker MPM Error"
description: "Fix Apache worker MPM errors when thread-based processing fails or becomes unstable."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Worker MPM Error

Apache worker MPM encounters threading errors or crashes.

```
AH00095: child pid XXXX exit signal Segmentation fault (11)
```

## Common Causes

- Not thread-safe modules loaded with worker MPM
- Memory corruption from concurrent threads
- Module incompatibility with threading
- ThreadLimit too high for system resources
- Race conditions in shared modules

## How to Fix

### Verify MPM Configuration

```bash
# Check which MPM is active
apachectl -V | grep MPM
# For worker or event, ensure module is loaded
apachectl -M | grep mpm
```

### Configure Worker MPM

```apache
<IfModule mpm_worker_module>
    StartServers 3
    MinSpareThreads 25
    MaxSpareThreads 75
    ThreadLimit 64
    ThreadsPerChild 25
    MaxRequestWorkers 400
    MaxConnectionsPerChild 10000
</IfModule>
```

### Switch to Event MPM

```bash
# Event MPM is recommended for most workloads
a2dismod mpm_worker
a2enmod mpm_event
systemctl restart apache2
```

### Identify Non-Thread-Safe Modules

```bash
# Common non-thread-safe modules to avoid with worker/event:
# - mod_php (use php-fpm instead)
# - mod_perl
# - Some third-party modules

# Check for segfaults in logs
grep -i segfault /var/log/apache2/error.log
```

### Limit Thread Count

```apache
# Conservative worker configuration
<IfModule mpm_worker_module>
    StartServers 2
    MinSpareThreads 25
    MaxSpareThreads 50
    ThreadLimit 32
    ThreadsPerChild 25
    MaxRequestWorkers 200
    MaxConnectionsPerChild 5000
</IfModule>
```

## Examples

```bash
# Monitor thread usage
curl -s http://localhost/server-status?auto | grep -E "BusyWorkers|IdleWorkers"

# Check for errors
journalctl -u apache2 --since "1 hour ago" | grep -i "worker\|thread\|segfault"
```
