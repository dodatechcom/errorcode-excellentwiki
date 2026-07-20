---
title: "[Solution] Redis Syslog Enabled Error"
description: "How to fix Redis syslog configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- syslog-facility set to invalid value
- syslog-enabled but syslog not running
- Permission denied for syslog socket

## Fix

Check syslog configuration:

```bash
redis-cli CONFIG GET syslog-enabled
redis-cli CONFIG GET syslog-facility
```

Disable syslog:

```bash
redis-cli CONFIG SET syslog-enabled no
```

Check syslog facility:

```bash
redis-cli CONFIG SET syslog-facility local0
```

## Examples

```bash
# Check syslog config
redis-cli CONFIG GET syslog-*

# Test syslog
logger -p local0.info "Redis test message"

# Check syslog socket
ls -la /dev/log
```
