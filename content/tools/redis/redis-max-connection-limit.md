---
title: "[Solution] Redis Max Connection Limit Reached"
description: "How to fix Redis error when maximum number of client connections is reached"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Too many concurrent clients connected
- Connection leak in the application (connections not properly closed)
- Low `maxclients` setting (default: 10000)
- High traffic spike

## How to Fix

Check current client count:

```bash
redis-cli INFO clients
```

Increase maxclients temporarily:

```bash
redis-cli CONFIG SET maxclients 50000
```

Make it permanent in `redis.conf`:

```bash
sudo sed -i 's/^# maxclients 10000/maxclients 50000/' /etc/redis/redis.conf
```

Check for connection leaks:

```bash
redis-cli CLIENT LIST
```

Kill idle connections:

```bash
redis-cli CLIENT KILL IDLE 300
```

## Examples

```bash
# View connected clients
redis-cli INFO clients | grep connected_clients

# Kill specific client
redis-cli CLIENT KILL ADDR 127.0.0.1:54321

# Check maxclients setting
redis-cli CONFIG GET maxclients
```
