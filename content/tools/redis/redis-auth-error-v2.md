---
title: "Redis - ERR invalid password"
description: "Redis rejects authentication attempt because the provided password is incorrect or AUTH command is misconfigured"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

An "ERR invalid password" error occurs when the Redis client sends an AUTH command with incorrect credentials. This can be caused by wrong password, incorrect ACL user, or misconfigured authentication in the connection string.

## Common Causes

- Wrong password in connection configuration
- Password changed in Redis config but not in client
- ACL user does not exist or has wrong password
- Connection string with special characters not escaped
- Redis started without `requirepass` but client sends AUTH

## How to Fix

1. Verify the password in Redis config:

```bash
redis-cli CONFIG GET requirepass
# Or for ACL
redis-cli ACL LIST
```

2. Reset the password if forgotten:

```bash
redis-cli CONFIG SET requirepass "newpassword"
```

3. Test authentication manually:

```bash
redis-cli
> AUTH mypassword
OK
```

4. URL-encode special characters in password:

```javascript
// If password is: p@ss!w0rd
const encodedPassword = encodeURIComponent('p@ss!w0rd');
const redis = new Redis(`redis://:${encodedPassword}@localhost:6379`);
```

5. Check ACL configuration:

```bash
redis-cli ACL WHOAMI
redis-cli ACL GETUSER myuser
# If user doesn't exist, create it
redis-cli ACL SETUSER myuser on >password ~* &* +@all
```

6. Disable authentication for development only:

```conf
# redis.conf
# requirepass mypassword
```

## Examples

```bash
# Error: ERR invalid password
$ redis-cli -a wrongpassword
Error: ERR invalid password

# Fix: use correct password
$ redis-cli -a correctpassword
127.0.0.1:6379>
```

```javascript
// Error with ioredis
const redis = new Redis({ password: 'wrongpassword' });
// Error: ERR invalid password

// Fix: correct password
const redis = new Redis({ password: 'correctpassword' });
```

## Related Errors

- [Connection error]({{< relref "/tools/redis/redis-connection-error" >}})
- [Cluster error]({{< relref "/tools/redis/redis-cluster-error" >}})
