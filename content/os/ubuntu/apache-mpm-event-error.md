---
title: "Apache MPM Event Module Error"
description: "Apache event MPM failing to handle concurrent connections properly"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Apache MPM Event Module Error

Apache event MPM failing to handle concurrent connections properly

## Common Causes

- Event MPM not enabled (prefork or worker loaded instead)
- MaxRequestWorkers exceeds available file descriptors
- KeepAlive settings causing connection exhaustion
- Spare threads configuration incorrect

## How to Fix

1. Check MPM: `apachectl -V | grep MPM`
2. Switch MPM: `sudo a2dismod mpm_prefork && sudo a2enmod mpm_event`
3. Adjust settings: `StartServers 3`, `MinSpareThreads 25`, `MaxRequestWorkers 150`
4. Check file limits: `ulimit -n`

## Examples

```bash
# Check which MPM is loaded
apachectl -V | grep MPM

# Switch to event MPM
sudo a2dismod mpm_prefork
sudo a2enmod mpm_event
sudo systemctl restart apache2
```
