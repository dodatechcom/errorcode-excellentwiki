---
title: "[Solution] Apache mod_evasive False Positive Error"
description: "Fix Apache mod_evasive blocking legitimate traffic due to overly aggressive rate limiting."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Apache mod_evasive False Positive Error

Apache mod_evasive blocks legitimate requests because the DOS threshold is set too low.

```
Access to client denied by server configuration (mod_evasive)
```

## Common Causes

- DOSPageCount threshold too low
- DOSBusyCount triggered by normal traffic spikes
- Network load balancers share source IP
- Legitimate health check requests hitting threshold
- Log rotation causing temporary file issues

## How to Fix

### Adjust Thresholds

```apache
<IfModule mod_evasive20.c>
    DOSHashTableSize 3097
    DOSPageCount 50
    DOSSiteCount 200
    DOSPageInterval 1
    DOSSiteInterval 1
    DOSBlockingPeriod 10
</IfModule>
```

### Whitelist Internal IPs

```apache
<IfModule mod_evasive20.c>
    # Increase thresholds
    DOSPageCount 100
    DOSSiteCount 500
    DOSBlockingPeriod 5

    # Whitelist internal network
    DOSWhitelist 127.0.0.1
    DOSWhitelist 10.0.0.*
    DOSWhitelist 192.168.1.*
</IfModule>
```

### Configure Temp Directory

```apache
<IfModule mod_evasive20.c>
    # Use dedicated temp directory
    DOStemp /tmp/mod_evasive/
    # Ensure writable
</IfModule>
```

```bash
mkdir -p /tmp/mod_evasive
chown www-data:www-data /tmp/mod_evasive
```

### Monitor Blocked Requests

```bash
# Watch for false positives in logs
tail -f /var/log/apache2/error.log | grep evasive
```

## Examples

```apache
# Relaxed configuration for high-traffic sites
<IfModule mod_evasive20.c>
    DOSHashTableSize 8191
    DOSPageCount 200
    DOSSiteCount 1000
    DOSPageInterval 1
    DOSSiteInterval 1
    DOSBlockingPeriod 5
    DOSEmailNotify admin@example.com
    DOSLogStatus on
</IfModule>
```
