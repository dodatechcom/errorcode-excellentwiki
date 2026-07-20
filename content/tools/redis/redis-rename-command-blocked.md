---
title: "[Solution] Redis Rename Command Blocked Error"
description: "How to fix Redis rename-command errors when commands are disabled"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- rename-command used to disable a command
- Application using a renamed/disabled command
- Client sending the original command name

## Fix

Check renamed commands:

```bash
grep rename-command /etc/redis/redis.conf
```

Remove rename-command directives:

```bash
sudo sed -i '/rename-command/d' /etc/redis/redis.conf
sudo systemctl restart redis
```

Use the renamed command:

```bash
# If FLUSHALL was renamed to FLUSHALL_SECRET
redis-cli FLUSHALL_SECRET
```

## Examples

```bash
# Check for renamed commands
redis-cli CONFIG GET rename-command

# Test if command is available
redis-cli FLUSHALL

# View command info
redis-cli COMMAND INFO FLUSHALL
```
