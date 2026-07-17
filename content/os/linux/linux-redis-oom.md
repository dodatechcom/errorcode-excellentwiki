---
title: "[Solution] Linux Redis OOM Command Not Allowed"
description: "Fix Linux Redis 'OOM command not allowed' errors. Resolve Redis out-of-memory issues, configure eviction policies, and tune memory limits."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: Redis — OOM command not allowed

The `OOM command not allowed when used memory > 'maxmemory'` error means Redis has reached its configured maximum memory limit (`maxmemory`) and the current eviction policy does not allow the command to proceed. Redis refuses write operations when memory is full and no eviction policy is set to free space.

## What This Error Means

Redis uses `maxmemory` to cap its memory usage. When this limit is reached, Redis behavior depends on the `maxmemory-policy` setting. If the policy is `noeviction` (the default), Redis rejects all write commands with an OOM error. Other policies (like `allkeys-lru`) evict existing keys to make room for new writes. The OOM error is a safety mechanism to prevent Redis from consuming all system memory.

## Common Causes

- `maxmemory` set too low for the workload
- `maxmemory-policy` set to `noeviction` (default)
- Memory leak in the application (keys not being expired)
- Large keys or data structures accumulating
- No TTL set on cached keys
- Redis used as both cache and persistent store

## How to Fix

### 1. Check Current Memory Usage

```bash
# Connect to Redis
redis-cli

# Check memory usage
INFO memory

# Key metrics:
# used_memory: 1073741824 (1GB)
# maxmemory: 1073741824 (1GB)
# maxmemory_policy: noeviction
```

### 2. Increase maxmemory

```bash
# Set maxmemory at runtime
redis-cli CONFIG SET maxmemory 2gb

# Or edit the configuration file
sudo nano /etc/redis/redis.conf

# Change:
# maxmemory 1gb
# To:
# maxmemory 4gb

# Restart Redis
sudo systemctl restart redis-server
```

### 3. Set an Eviction Policy

```bash
# Set eviction policy at runtime
redis-cli CONFIG SET maxmemory-policy allkeys-lru

# Common policies:
# noeviction     - Return errors when memory limit reached (default)
# allkeys-lru    - Evict least recently used keys (best for cache)
# volatile-lru   - Evict LRU keys with expire set
# allkeys-random - Evict random keys
# volatile-ttl   - Evict keys with shortest TTL
# allkeys-lfu    - Evict least frequently used keys

# Edit permanently in redis.conf
# maxmemory-policy allkeys-lru
```

### 4. Find and Remove Large Keys

```bash
# Find keys using the most memory
redis-cli --bigkeys

# Find keys by memory usage
redis-cli MEMORY USAGE <key>

# Scan for keys with large values
redis-cli --memkeys

# Delete a specific large key
redis-cli DEL <large-key>
```

### 5. Set TTL on Keys

```bash
# Set expiration on keys
redis-cli SET mykey myvalue EX 3600  # Expires in 1 hour

# Check TTL
redis-cli TTL mykey

# Set TTL on existing key
redis-cli EXPIRE mykey 3600

# Use a hash with expiration for batch operations
redis-cli EXPIRE myhash 86400
```

### 6. Monitor Memory Usage Over Time

```bash
# Log memory usage periodically
redis-cli INFO memory | grep -E 'used_memory|maxmemory'

# Use Redis memory usage in monitoring
redis-cli MEMORY DOCTOR

# Check for memory fragmentation
redis-cli INFO memory | grep mem_fragmentation_ratio
```

### 7. Use Redis as Cache-Only

```bash
# If using Redis only as a cache, set appropriate policy
# and ensure all keys have TTL

redis-cli CONFIG SET maxmemory-policy allkeys-lru

# In the application, always set TTL:
redis-cli SET session:abc123 data EX 1800
```

## Examples

```bash
$ redis-cli SET cache:large-data "..."
(error) OOM command not allowed when used memory > 'maxmemory'.

$ redis-cli INFO memory | grep -E 'used_memory|maxmemory'
used_memory:1073741824
maxmemory:1073741824
used_memory_peak:1073741824

$ redis-cli CONFIG SET maxmemory 2gb
OK

$ redis-cli CONFIG SET maxmemory-policy allkeys-lru
OK

$ redis-cli SET cache:large-data "..."
OK

$ redis-cli --bigkeys
[00.00%] Biggest string: 50MB (key: cache:old-data)
# Delete or set TTL
$ redis-cli DEL cache:old-data
$ redis-cli EXPIRE cache:large-data 3600
```

## Related Errors

- [Cannot allocate memory]({{< relref "/os/linux/cannot-allocate-memory" >}}) — System memory allocation failures
- [OOM killer]({{< relref "/os/linux/oom-killer" >}}) — Linux OOM killer
- [Redis connection error]({{< relref "/os/linux/linux-redis-oom" >}}) — Redis connectivity issues
