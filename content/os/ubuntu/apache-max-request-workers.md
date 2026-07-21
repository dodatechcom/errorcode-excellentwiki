---
title: "Apache Max Request Workers Reached"
description: "Apache has exhausted all worker processes and cannot serve new requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Apache Max Request Workers Reached

Apache has exhausted all worker processes and cannot serve new requests

## Common Causes

- MaxRequestWorkers set too low for traffic
- KeepAliveTimeout too high holding workers
- Slow CGI/FastCGI requests consuming workers
- Insufficient system RAM for configured workers

## How to Fix

1. Check current: `apachectl -V | grep MaxRequestWorkers`
2. Calculate: each worker uses ~15-20MB RAM, so MaxRequestWorkers * 20MB < total RAM
3. Adjust in mpm_prefork or mpm_worker config
4. Reduce KeepAliveTimeout: `KeepAliveTimeout 5`

## Examples

```apache
# Adjust MaxRequestWorkers (mpm_prefork)
<IfModule mpm_prefork_module>
    MaxRequestWorkers 150
    ServerLimit 150
    KeepAliveTimeout 5
</IfModule>
```
