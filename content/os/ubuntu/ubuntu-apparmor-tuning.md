---
title: "Ubuntu AppArmor Profile Tuning Error"
description: "Application performance degraded due to excessive AppArmor checks"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu AppArmor Profile Tuning Error

Application performance degraded due to excessive AppArmor checks

## Common Causes

- Profile contains too many file rules
- Rule matches too broadly causing frequent checks
- Capability rules not optimized
- dbus abstractions overly restrictive

## How to Fix

1. Profile apparmor: `sudo aa-profiles /etc/apparmor.d/usr.sbin.nginx`
2. Reduce rules: combine similar paths with wildcards
3. Check performance: `sudo aa-status` shows profile load times
4. Consider using tunables for common paths

## Examples

```bash
# Check AppArmor profile load times
sudo aa-status | head -20

# Profile a running application
sudo aa-genprof /usr/sbin/nginx
```
