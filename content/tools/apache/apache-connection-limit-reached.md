---
title: "[Solution] Apache Connection Limit Reached"
description: "Fix Apache connection limit errors when MaxClients or MaxRequestWorkers is exceeded."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Apache connection limit reached when the number of concurrent connections exceeds the configured maximum.

## Common Causes

- MaxClients or MaxRequestWorkers set too low
- KeepAliveTimeout too high holding connections
- Slow client connections consuming slots
- DDoS or traffic spike
- MPM module misconfiguration

## How to Fix

- Increase MaxRequestWorkers in MPM config
- Reduce KeepAliveTimeout to free connections faster
- Use mod_reqtimeout to drop slow clients

## Examples

```
# prefork MPM
<IfModule mpm_prefork_module>
    StartServers            5
    MinSpareServers         5
    MaxSpareServers        10
    MaxRequestWorkers     256
    MaxConnectionsPerChild   0
</IfModule>

# event MPM
<IfModule mpm_event_module>
    StartServers            3
    MinSpareThreads        75
    MaxSpareThreads       250
    ThreadLimit            64
    ThreadsPerChild        25
    MaxRequestWorkers     400
    MaxConnectionsPerChild   0
</IfModule>
```
