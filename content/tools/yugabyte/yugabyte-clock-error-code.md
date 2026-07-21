---
title: "YugabyteDB Clock Error Code"
description: "Clock error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Clock synchronization returning specific error code.

## Common Causes
- NTP not synchronized
- Virtual machine clock drift
- Hardware clock issue

## How to Fix
```bash
# Check clock sync
timedatectl status

# Sync NTP
ntpdate -u pool.ntp.org
```

## Examples
```bash
# Check clock offset
timedatectl show-timesync
# Monitor clock skew
curl http://localhost:9000/metrics | grep clock
```

