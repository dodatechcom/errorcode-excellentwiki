---
title: "[Solution] Redis AUTH Failed Error"
description: "How to fix Redis AUTH failed error when password authentication is rejected"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Wrong password provided
- Redis configured with `requirepass` but client sends wrong password
- ACL user permissions insufficient
- Connection attempt with no password to a password-protected instance
- Special characters in password not escaped properly

## How to Fix

Authenticate with the correct password:

```bash
redis-cli -a your_password
```

Or use interactive AUTH:

```bash
redis-cli
AUTH your_password
```

Check current ACL users:

```bash
redis-cli ACL LIST
```

Reset the password if forgotten (requires restarting Redis):

```bash
# Remove requirepass from redis.conf
sudo sed -i '/^requirepass/d' /etc/redis/redis.conf
sudo systemctl restart redis
```

Create a new ACL user:

```bash
redis-cli ACL SETUSER newuser on >newpassword ~* +@all
```

## Examples

```bash
# Authenticate
redis-cli AUTH mypassword

# Check if password is required
redis-cli CONFIG GET requirepass

# List ACL users
redis-cli ACL WHOAMI
```
