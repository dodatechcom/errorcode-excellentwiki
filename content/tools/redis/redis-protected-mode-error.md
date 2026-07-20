---
title: "[Solution] Redis Protected Mode Error"
description: "How to fix Redis protected mode error when binding to non-loopback interfaces"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Binding to 0.0.0.0 without setting a password
- Protected mode enabled without requirepass
- Client connecting from non-localhost address

## How to Fix

Set a password:

```bash
redis-cli CONFIG SET requirepass "strong_password_here"
```

Or disable protected mode (not recommended):

```bash
redis-cli CONFIG SET protected-mode no
```

Bind to localhost only:

```bash
redis-cli CONFIG SET bind 127.0.0.1
```

Update redis.conf:

```bash
# Option 1: Set password
echo "requirepass your_password" | sudo tee -a /etc/redis/redis.conf

# Option 2: Disable protected mode
sudo sed -i 's/^protected-mode yes/protected-mode no/' /etc/redis/redis.conf
```

## Examples

```bash
# Check protected mode
redis-cli CONFIG GET protected-mode

# Set password
redis-cli CONFIG SET requirepass mypassword

# Test connection after fix
redis-cli -h remote-host -p 6379 -a mypassword PING
```
