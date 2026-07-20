#!/usr/bin/env python3
"""Generate Redis error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/redis'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["redis"]',
        'error-types: ["database-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ]
    return '\n'.join(lines)

PAGES = [
    # ============================================================
    # 1. Connection/Auth errors
    # ============================================================
    (
        "redis-connection-refused-error",
        "Redis Connection Refused Error",
        "How to fix Redis connection refused error when the server is not accepting connections",
        """## Common Causes

- Redis server is not running or has crashed
- Wrong host or port specified in the connection string
- Firewall blocking the Redis port (default: 6379)
- Redis `bind` configuration restricted to localhost
- Too many client connections already established

## How to Fix

Check if Redis is running:

```bash
redis-cli ping
```

If not running, start the server:

```bash
sudo systemctl start redis
```

Verify the bind configuration in `redis.conf`:

```bash
grep "^bind" /etc/redis/redis.conf
```

To allow remote connections, update the bind directive:

```bash
sudo sed -i 's/^bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf
sudo systemctl restart redis
```

Check if the port is listening:

```bash
ss -tlnp | grep 6379
```

Increase the max clients limit if needed:

```bash
redis-cli CONFIG SET maxclients 10000
```

## Examples

```bash
# Test connection
redis-cli -h 127.0.0.1 -p 6379 ping

# Check server status
systemctl status redis

# View active connections
redis-cli INFO clients
```
"""
    ),
    (
        "redis-connection-timeout-error",
        "Redis Connection Timeout Error",
        "How to resolve Redis connection timeout when the client cannot connect within the specified time",
        """## Common Causes

- Server is overloaded or under heavy load
- Network latency between client and server
- `timeout` configuration too low
- Large keys causing blocking operations
- Too many concurrent connections

## How to Fix

Increase the client timeout value:

```bash
redis-cli CONFIG SET timeout 0
```

Check the TCP backlog setting:

```bash
redis-cli CONFIG GET tcp-backlog
```

Increase `tcp-keepalive`:

```bash
redis-cli CONFIG SET tcp-keepalive 60
```

Monitor slow operations:

```bash
redis-cli SLOWLOG GET 10
```

Adjust the `tcp-backlog` in `redis.conf`:

```bash
sudo sed -i 's/^tcp-backlog 511/tcp-backlog 1024/' /etc/redis/redis.conf
```

## Examples

```python
# Python with explicit timeout
import redis
r = redis.Redis(host='localhost', port=6379, socket_timeout=10, socket_connect_timeout=5)
r.ping()
```

```bash
# Test with redis-cli timeout
redis-cli --no-auth-warning -h 127.0.0.1 -p 6379 --latency
```
"""
    ),
    (
        "redis-auth-failed-error",
        "Redis AUTH Failed Error",
        "How to fix Redis AUTH failed error when password authentication is rejected",
        """## Common Causes

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
"""
    ),
    (
        "redis-noauth-authentication-required",
        "Redis NOAUTH Authentication Required",
        "How to fix Redis NOAUTH error when commands are executed before authentication",
        """## Common Causes

- Client sends commands without authenticating first
- Connection pool reusing a stale connection after AUTH timeout
- `requirepass` or ACL configured but client does not send AUTH
- Multi-command pipeline sent before authentication

## How to Fix

Send AUTH command before any data commands:

```bash
redis-cli
AUTH your_password
PING
```

In application code, ensure AUTH is called on new connections:

```python
import redis
r = redis.Redis(host='localhost', port=6379, password='your_password')
r.ping()
```

Check if authentication is enabled:

```bash
redis-cli CONFIG GET requirepass
```

Disable authentication temporarily for debugging:

```bash
redis-cli CONFIG SET requirepass ""
```

## Examples

```bash
# Wrong - sends command without AUTH
redis-cli SET key value
# Error: NOAUTH Authentication required

# Correct - authenticate first
redis-cli
> AUTH mypassword
OK
> SET key value
OK
```
"""
    ),
    (
        "redis-tls-handshake-error",
        "Redis TLS Handshake Error",
        "How to fix Redis TLS handshake failure when establishing encrypted connections",
        """## Common Causes

- Expired or self-signed SSL certificate
- TLS version mismatch between client and server
- Missing or wrong certificate file paths in `redis.conf`
- Certificate chain incomplete
- Cipher suite not supported

## How to Fix

Verify TLS is enabled:

```bash
redis-cli CONFIG GET tls-port
```

Check certificate validity:

```bash
openssl x509 -in /etc/redis/tls/redis.crt -noout -dates
```

Verify the key matches the certificate:

```bash
diff <(openssl x509 -in /etc/redis/tls/redis.crt -noout -modulus) \
     <(openssl rsa -in /etc/redis/tls/redis.key -noout -modulus)
```

Test the TLS connection:

```bash
openssl s_client -connect localhost:6380 -cert /etc/redis/tls/redis.crt -key /etc/redis/tls/redis.key
```

Update `redis.conf` with correct TLS paths:

```bash
tls-cert-file /etc/redis/tls/redis.crt
tls-key-file /etc/redis/tls/redis.key
tls-ca-cert-file /etc/redis/tls/ca.crt
```

## Examples

```bash
# Connect with TLS
redis-cli --tls --cert /etc/redis/tls/redis.crt --key /etc/redis/tls/redis.key --cacert /etc/redis/tls/ca.crt

# Regenerate certificates
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes \
  -keyout redis.key -out redis.crt -subj "/CN=localhost"
```
"""
    ),
    (
        "redis-max-connection-limit",
        "Redis Max Connection Limit Reached",
        "How to fix Redis error when maximum number of client connections is reached",
        """## Common Causes

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
"""
    ),
    (
        "redis-dns-resolution-error",
        "Redis DNS Resolution Error",
        "How to fix Redis DNS resolution failure when the hostname cannot be resolved",
        """## Common Causes

- DNS server unreachable or misconfigured
- Hostname in connection string is incorrect
- `/etc/hosts` missing entry for Redis host
- Docker container cannot resolve hostnames
- DNS cache stale on client

## How to Fix

Test DNS resolution:

```bash
nslookup redis-host.example.com
```

Add entry to `/etc/hosts`:

```bash
echo "192.168.1.100 redis-host" | sudo tee -a /etc/hosts
```

Use IP address directly instead of hostname:

```bash
redis-cli -h 192.168.1.100 -p 6379 ping
```

Check DNS configuration:

```bash
cat /etc/resolv.conf
```

## Examples

```bash
# Test connectivity with IP
redis-cli -h 192.168.1.100 PING

# Flush DNS cache (systemd-resolved)
sudo systemd-resolve --flush-caches

# Verify with dig
dig redis-host.example.com
```
"""
    ),
    (
        "redis-socket-timeout-error",
        "Redis Socket Timeout Error",
        "How to fix Redis socket timeout when operations exceed the configured timeout period",
        """## Common Causes

- Long-running blocking operations (KEYS, SORT on large datasets)
- Network congestion or packet loss
- Server under heavy CPU load
- `socket-timeout` set too low in client config
- Large value sizes exceeding network buffers

## How to Fix

Check the current timeout:

```bash
redis-cli CONFIG GET timeout
```

Increase socket timeout in client:

```python
import redis
r = redis.Redis(host='localhost', socket_timeout=30, socket_connect_timeout=10)
```

Monitor slow operations:

```bash
redis-cli SLOWLOG GET 10
```

Replace blocking commands with non-blocking alternatives:

```bash
# Instead of KEYS pattern (blocking), use SCAN
redis-cli SCAN 0 MATCH pattern:*
```

## Examples

```bash
# Check timeout config
redis-cli CONFIG GET timeout

# Monitor slow log
redis-cli SLOWLOG LEN

# Check network stats
redis-cli INFO stats | grep total_net_input_bytes
```
"""
    ),
    (
        "redis-connection-reset-by-peer",
        "Redis Connection Reset By Peer",
        "How to fix Redis connection reset error when the server unexpectedly closes the connection",
        """## Common Causes

- Redis server restarted or crashed
- `timeout` setting closing idle connections
- Server running out of memory and killing clients
- TCP keepalive not configured properly
- Firewall dropping idle connections

## How to Fix

Check if server is alive:

```bash
redis-cli PING
```

Disable connection timeout (keep connections alive):

```bash
redis-cli CONFIG SET timeout 0
```

Enable TCP keepalive:

```bash
redis-cli CONFIG SET tcp-keepalive 60
```

Check server logs for crash information:

```bash
sudo tail -100 /var/log/redis/redis-server.log
```

Increase OS file descriptor limits:

```bash
ulimit -n 65535
```

## Examples

```bash
# Monitor live connections
watch -n 1 'redis-cli INFO clients | grep connected_clients'

# Check server uptime
redis-cli INFO server | grep uptime_in_seconds

# Test connection stability
for i in {1..100}; do redis-cli PING; done
```
"""
    ),
    (
        "redis-busy-loading-error",
        "Redis Busy Loading Error",
        "How to fix Redis busy loading error when the server is still loading data from disk",
        """## Common Causes

- Large RDB dump file taking long to load
- Server just started and data not yet loaded
- AOF rewrite in progress
- Insufficient I/O bandwidth for loading
- Dataset too large for available memory during load

## How to Fix

Wait for loading to complete:

```bash
# Check loading status
redis-cli INFO persistence | grep loading
```

Check RDB file size:

```bash
ls -lh /var/lib/redis/dump.rdb
```

Switch to AOF for faster startup:

```bash
redis-cli CONFIG SET appendonly yes
```

Increase loading speed with better hardware or by reducing dataset size:

```bash
# Monitor loading progress
redis-cli INFO persistence | grep rdb_last_bgsave_status
```

## Examples

```bash
# Check if Redis is still loading
redis-cli PING
# If loading: LOADING Redis is loading the dataset in memory

# Wait and retry
while [ "$(redis-cli PING)" != "PONG" ]; do sleep 1; done
echo "Redis is ready"
```
"""
    ),
    (
        "redis-busy-writing-error",
        "Redis Busy Writing Error",
        "How to fix Redis busy writing error when the server is blocked by a long-running write operation",
        """## Causes

- Slow RDB save or AOF rewrite blocking other commands
- Large dataset being persisted to disk
- Fork operation for background saves

## Fix

Disable RDB saves temporarily:

```bash
redis-cli CONFIG SET save ""
```

Check RDB background save status:

```bash
redis-cli LASTSAVE
```

Kill a blocking BGSAVE:

```bash
redis-cli CLIENT KILL TYPE NORMAL LADDR <addr>
```

Switch to AOF persistence:

```bash
redis-cli CONFIG SET appendonly yes
```

## Examples

```bash
# Trigger background save
redis-cli BGSAVE

# Check if background operation is running
redis-cli INFO persistence | grep rdb_bgsave_in_progress

# Monitor disk I/O
iostat -x 1
```
"""
    ),
    (
        "redis-invalid-password-format",
        "Redis Invalid Password Format Error",
        "How to fix Redis error when the password contains invalid characters or is malformed",
        """## Causes

- Password contains special characters not properly escaped
- Password has leading or trailing whitespace
- Password was modified in redis.conf with encoding issues

## Fix

Use ACL to set password instead of redis.conf:

```bash
redis-cli ACL SETUSER default on >'p@ssw0rd!'
```

Verify the password in redis.conf:

```bash
grep requirepass /etc/redis/redis.conf
```

Reset password cleanly:

```bash
redis-cli CONFIG SET requirepass ""
redis-cli CONFIG SET requirepass "new_clean_password"
```

## Examples

```bash
# Test with quoted password
redis-cli -a 'my!p@ss#word' --no-auth-warning PING

# Verify current password works
redis-cli -a currentpass PING
```
"""
    ),
    (
        "redis-connection-pool-exhausted",
        "Redis Connection Pool Exhausted",
        "How to fix Redis connection pool exhausted error when all connections in the pool are in use",
        """## Causes

- Application not returning connections to the pool
- Pool size too small for workload
- Slow queries holding connections longer than expected
- Connection leak in application code

## Fix

Increase pool size:

```python
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=50)
r = redis.Redis(connection_pool=pool)
```

Set connection timeout:

```python
pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=20, timeout=5)
```

Check active connections:

```bash
redis-cli CLIENT LIST
```

Use connection pool with context manager:

```python
with redis.Redis(connection_pool=pool) as r:
    r.get("key")
```

## Examples

```bash
# Monitor connection count
watch -n 1 'redis-cli INFO clients | grep connected_clients'

# Kill long-running client connections
redis-cli CLIENT KILL IDLE 300
```
"""
    ),

    # ============================================================
    # 2. Memory errors
    # ============================================================
    (
        "redis-oom-command-not-allowed",
        "Redis OOM Command Not Allowed",
        "How to fix Redis OOM error when used memory exceeds maxmemory limit",
        """## Common Causes

- `maxmemory` limit reached and no eviction policy configured
- Eviction policy set to `noeviction`
- Large number of keys being written rapidly
- Memory fragmentation causing higher usage than expected

## How to Fix

Check current memory usage:

```bash
redis-cli INFO memory | grep used_memory_human
```

Check maxmemory setting:

```bash
redis-cli CONFIG GET maxmemory
```

Set an eviction policy:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

Increase maxmemory:

```bash
redis-cli CONFIG SET maxmemory 4gb
```

Analyze memory usage:

```bash
redis-cli MEMORY USAGE mykey
redis-cli MEMORY DOCTOR
```

## Examples

```bash
# Check memory breakdown
redis-cli INFO memory

# Find keys using most memory
redis-cli --bigkeys

# Force memory defragmentation
redis-cli MEMORY PURGE
```
"""
    ),
    (
        "redis-misconf-rdb-snapshots",
        "Redis MISCONF RDB Snapshots Error",
        "How to fix Redis MISCONF error about RDB snapshot persistence failures",
        """## Common Causes

- Disk is full or has no write permissions
- Background save (BGSAVE) failed
- Redis cannot fork a child process for RDB
- `/var/lib/redis/` directory not writable
- Disk quota exceeded

## How to Fix

Check the Redis data directory permissions:

```bash
ls -la /var/lib/redis/
sudo chown redis:redis /var/lib/redis/
sudo chmod 755 /var/lib/redis/
```

Check disk space:

```bash
df -h /var/lib/redis/
```

Verify the last save status:

```bash
redis-cli LASTSAVE
redis-cli INFO persistence | grep rdb_last_bgsave_status
```

Check system limits for forking:

```bash
sysctl vm.overcommit_memory
sysctl vm.max_map_count
```

Set `vm.overcommit_memory`:

```bash
sudo sysctl vm.overcommit_memory=1
```

## Examples

```bash
# Monitor background save
redis-cli INFO persistence

# Free disk space
sudo journalctl --vacuum-size=100M

# Test save manually
redis-cli BGSAVE
```
"""
    ),
    (
        "redis-maxmemory-limit-hit",
        "Redis Maxmemory Limit Hit",
        "How to handle Redis maxmemory limit being reached with proper eviction",
        """## Common Causes

- Data set growing beyond configured maxmemory
- Eviction policy not aggressive enough
- No key expiration (TTL) set on keys

## How to Fix

Check maxmemory and policy:

```bash
redis-cli CONFIG GET maxmemory
redis-cli CONFIG GET maxmemory-policy
```

Set appropriate eviction policy:

```bash
# For caching workload
redis-cli CONFIG SET maxmemory-policy allkeys-lru

# For mixed workload
redis-cli CONFIG SET maxmemory-policy volatile-lru
```

Increase maxmemory if more RAM is available:

```bash
redis-cli CONFIG SET maxmemory 8gb
```

Find and remove unnecessary keys:

```bash
redis-cli --bigkeys
redis-cli --memkeys
```

## Examples

```bash
# Monitor eviction events
redis-cli INFO stats | grep evicted_keys

# Set TTL on keys
redis-cli EXPIRE mykey 3600

# Check memory usage of a key
redis-cli MEMORY USAGE mykey
```
"""
    ),
    (
        "redis-allocator-error",
        "Redis Allocator Error",
        "How to fix Redis memory allocator errors when the system cannot allocate memory",
        """## Common Causes

- System running out of physical memory and swap
- `vm.overcommit_memory` set to 0 (strict overcommit)
- Redis dataset too large for available memory
- Memory fragmentation causing allocation failure

## How to Fix

Set overcommit memory:

```bash
sudo sysctl vm.overcommit_memory=1
```

Make it persistent:

```bash
echo "vm.overcommit_memory=1" | sudo tee -a /etc/sysctl.conf
```

Check available memory:

```bash
free -h
```

Reduce Redis memory usage:

```bash
redis-cli MEMORY PURGE
redis-cli CONFIG SET maxmemory 2gb
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

## Examples

```bash
# Check memory stats
redis-cli INFO memory | grep mem_allocator

# Monitor allocation failures
redis-cli INFO memory | grep used_memory_peak_human

# Set swap for Redis
sudo sysctl vm.swappiness=10
```
"""
    ),
    (
        "redis-swap-file-full",
        "Redis Swap File Full Error",
        "How to fix Redis swap file or swap space exhaustion errors",
        """## Causes

- System swap space exhausted
- Redis using swap due to insufficient physical memory
- Disk full preventing swap file growth

## Fix

Check swap usage:

```bash
free -h
swapon --show
```

Reduce Redis memory footprint:

```bash
redis-cli MEMORY PURGE
redis-cli CONFIG SET maxmemory 1gb
```

Add more swap space:

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Disable swap for Redis:

```bash
sudo swapoff /swapfile
sudo sysctl vm.swappiness=10
```

## Examples

```bash
# Check if Redis is swapping
redis-cli INFO memory | grep used_memory_rss_human

# Monitor swap usage
watch -n 2 'free -h'

# Disable swap temporarily
sudo swapoff -a
```
"""
    ),
    (
        "redis-memory-fragmentation",
        "Redis Memory Fragmentation Error",
        "How to fix Redis memory fragmentation ratio issues",
        """## Common Causes

- Fragmentation ratio > 1.5 indicates external fragmentation
- Frequent updates to keys of different sizes
- jemalloc allocator not optimizing properly
- Large key operations creating fragmentation

## How to Fix

Check fragmentation ratio:

```bash
redis-cli INFO memory | grep mem_fragmentation_ratio
```

Trigger memory defragmentation:

```bash
redis-cli MEMORY PURGE
```

Restart Redis to defragment (if persistent storage is safe):

```bash
sudo systemctl restart redis
```

Use active defragmentation (Redis 4.0+):

```bash
redis-cli CONFIG SET activedefrag yes
redis-cli CONFIG SET active-defrag-enabled yes
```

Analyze key sizes:

```bash
redis-cli --bigkeys
redis-cli --memkeys
```

## Examples

```bash
# Monitor fragmentation
watch -n 5 'redis-cli INFO memory | grep -E "used_memory_rss_human|mem_fragmentation_ratio"'

# Check allocator
redis-cli INFO memory | grep mem_allocator

# Manual defrag
redis-cli MEMORY PURGE
```
"""
    ),
    (
        "redis-out-of-memory-kill",
        "Redis Out of Memory Process Kill",
        "How to handle Redis being killed by the Linux OOM killer",
        """## Causes

- Redis using too much system memory
- OOM killer targeting Redis process
- Overcommit memory disabled

## Fix

Check OOM killer logs:

```bash
dmesg | grep -i oom
journalctl -k | grep -i oom
```

Protect Redis from OOM killer:

```bash
echo -17 > /proc/$(pidof redis-server)/oom_adj
```

Set overcommit memory:

```bash
sudo sysctl vm.overcommit_memory=1
```

Limit Redis memory:

```bash
redis-cli CONFIG SET maxmemory 3gb
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

## Examples

```bash
# Check Redis RSS memory
redis-cli INFO memory | grep used_memory_rss_human

# Set memory limit
redis-cli CONFIG SET maxmemory 4gb

# Monitor process memory
ps aux | grep redis-server
```
"""
    ),
    (
        "redis-memory-overhead-error",
        "Redis Memory Overhead Too High",
        "How to fix Redis memory overhead when per-key overhead is consuming too much memory",
        """## Causes

- Many small keys with high per-key overhead
- Using Redis data structures inefficiently
- Key names too long
- Excessive number of keys

## Fix

Check memory overhead:

```bash
redis-cli INFO memory | grep mem_allocator
redis-cli MEMORY USAGE key
```

Reduce key name lengths:

```bash
# Instead of: user:profile:123456789:settings:theme
# Use: u:p:12345:s:t
```

Use Hash for small objects instead of String:

```bash
# Bad - three keys
SET user:1:name "John"
SET user:1:email "john@example.com"
SET user:1:age "30"

# Better - one hash
HSET user:1 name "John" email "john@example.com" age "30"
```

Check overhead ratio:

```bash
redis-cli MEMORY DOCTOR
```

## Examples

```bash
# Check key memory usage
redis-cli MEMORY USAGE user:1

# Find large keys
redis-cli --bigkeys

# Check number of keys
redis-cli DBSIZE
```
"""
    ),
    (
        "redis-memory-limit-exceeded",
        "Redis Memory Limit Exceeded",
        "How to fix Redis memory limit being exceeded across multiple databases",
        """## Causes

- Memory spread across multiple Redis databases
- Key expiration disabled or not configured
- Data accumulation over time

## Fix

Check memory per database:

```bash
for i in $(seq 0 15); do
  echo "DB $i: $(redis-cli -n $i DBSIZE)"
done
```

Set maxmemory:

```bash
redis-cli CONFIG SET maxmemory 4gb
```

Enable eviction:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

Find and clean unused keys:

```bash
redis-cli --bigkeys
redis-cli --memkeys --samples 100
```

## Examples

```bash
# Check total keys
redis-cli INFO keyspace

# Set TTL on old keys
redis-cli SCAN 0 MATCH temp:* COUNT 100 | while read key; do
  redis-cli EXPIRE "$key" 3600
done
```
"""
    ),

    # ============================================================
    # 3. Persistence errors
    # ============================================================
    (
        "redis-rdb-save-failed",
        "Redis RDB Save Failed",
        "How to fix Redis RDB snapshot save failure during background save operations",
        """## Common Causes

- Disk full or no write permissions
- Fork failed due to memory constraints
- I/O error writing to RDB file
- Child process killed by OOM killer

## How to Fix

Check disk space:

```bash
df -h /var/lib/redis/
```

Check last save status:

```bash
redis-cli LASTSAVE
redis-cli INFO persistence | grep rdb_last_bgsave_status
```

Check permissions:

```bash
ls -la /var/lib/redis/dump.rdb
```

Check fork capability:

```bash
sysctl vm.overcommit_memory
```

Try manual save:

```bash
redis-cli BGSAVE
```

## Examples

```bash
# Monitor save progress
redis-cli INFO persistence | grep rdb_bgsave_in_progress

# Check disk I/O
iostat -x 1

# View save configuration
redis-cli CONFIG GET save
```
"""
    ),
    (
        "redis-aof-rewrite-failed",
        "Redis AOF Rewrite Failed",
        "How to fix Redis AOF rewrite failure during background AOF rewriting",
        """## Common Causes

- Insufficient disk space for new AOF file
- Fork operation failed due to memory pressure
- Rewrite buffer exceeded memory limit
- Child process terminated abnormally

## How to Fix

Check AOF rewrite status:

```bash
redis-cli INFO persistence | grep aof_rewrite_in_progress
```

Check disk space:

```bash
df -h /var/lib/redis/
```

Disable AOF rewrite temporarily:

```bash
redis-cli CONFIG SET auto-aof-rewrite-percentage 0
```

Check AOF file integrity:

```bash
redis-check-aof /var/lib/redis/appendonly.aof
```

## Examples

```bash
# Trigger manual rewrite
redis-cli BGREWRITEAOF

# Monitor AOF rewrite
watch -n 1 'redis-cli INFO persistence | grep aof'

# Check AOF size
ls -lh /var/lib/redis/appendonly.aof
```
"""
    ),
    (
        "redis-aof-file-corrupted",
        "Redis AOF File Corrupted",
        "How to fix Redis AOF file corruption issues",
        """## Common Causes

- Server crashed during AOF write
- Power failure during persistence
- Disk I/O error
- Incomplete write due to disk full

## How to Fix

Check AOF file integrity:

```bash
redis-check-aof --fix /var/lib/redis/appendonly.aof
```

If the AOF is too corrupted, truncate and rebuild from RDB:

```bash
redis-check-aof /var/lib/redis/appendonly.aof
# If truncated, fix it:
echo -n "" | sudo tee /var/lib/redis/appendonly.aof
```

Start Redis and let it rebuild:

```bash
sudo systemctl start redis
```

Prevent future corruption with AOF fsync:

```bash
redis-cli CONFIG SET appendfsync everysec
```

## Examples

```bash
# Check AOF integrity
redis-check-aof /var/lib/redis/appendonly.aof

# Fix corrupted AOF
redis-check-aof --fix /var/lib/redis/appendonly.aof

# Verify RDB backup
redis-check-rdb /var/lib/redis/dump.rdb
```
"""
    ),
    (
        "redis-append-only-file-write-error",
        "Redis AOF Write Error",
        "How to fix Redis append-only file write errors",
        """## Causes

- Disk full
- I/O error on the storage device
- AOF file permissions changed

## Fix

Check disk space:

```bash
df -h /var/lib/redis/
```

Check disk health:

```bash
sudo smartctl -a /dev/sda
```

Verify file permissions:

```bash
ls -la /var/lib/redis/appendonly.aof
sudo chown redis:redis /var/lib/redis/appendonly.aof
```

Check AOF configuration:

```bash
redis-cli CONFIG GET appendfsync
redis-cli CONFIG GET appendonly
```

## Examples

```bash
# Check I/O errors
dmesg | grep -i error

# Test disk write
dd if=/dev/zero of=/var/lib/redis/test_write bs=1M count=100
rm /var/lib/redis/test_write

# Monitor AOF size
watch -n 5 'ls -lh /var/lib/redis/appendonly.aof'
```
"""
    ),
    (
        "redis-fork-failed-error",
        "Redis Fork Failed Error",
        "How to fix Redis fork failure when creating child processes for persistence",
        """## Common Causes

- Insufficient virtual memory for fork
- `vm.overcommit_memory` set to 0
- System running low on memory
- PID max limit reached

## How to Fix

Set overcommit memory:

```bash
sudo sysctl vm.overcommit_memory=1
```

Check PID limits:

```bash
cat /proc/sys/kernel/pid_max
```

Increase if needed:

```bash
sudo sysctl kernel.pid_max=65535
```

Check available memory:

```bash
free -h
```

Reduce Redis memory for safer forking:

```bash
redis-cli CONFIG SET maxmemory 2gb
```

## Examples

```bash
# Check fork stats
redis-cli INFO stats | grep latest_fork_usec

# Monitor memory during fork
watch -n 1 'free -h'

# Check overcommit setting
cat /proc/sys/vm/overcommit_memory
```
"""
    ),
    (
        "redis-cant-open-file-error",
        "Redis Cannot Open File Error",
        "How to fix Redis error when it cannot open required files",
        """## Causes

- RDB or AOF file path incorrect in config
- File does not exist or was deleted
- Permission denied on file
- File descriptor limit reached

## Fix

Check file existence:

```bash
ls -la /var/lib/redis/dump.rdb
ls -la /var/lib/redis/appendonly.aof
```

Check Redis config paths:

```bash
redis-cli CONFIG GET dir
redis-cli CONFIG GET dbfilename
```

Fix permissions:

```bash
sudo chown -R redis:redis /var/lib/redis/
sudo chmod 660 /var/lib/redis/dump.rdb
```

Check file descriptor limit:

```bash
ulimit -n
```

## Examples

```bash
# Check open file descriptors
ls /proc/$(pidof redis-server)/fd | wc -l

# Check file descriptor limit
cat /proc/$(pidof redis-server)/limits | grep "open files"

# View Redis data directory
redis-cli CONFIG GET dir
```
"""
    ),
    (
        "redis-disk-quota-exceeded",
        "Redis Disk Quota Exceeded Error",
        "How to fix Redis disk quota exceeded when the filesystem runs out of space",
        """## Causes

- Redis data files growing too large
- AOF file continuously growing
- System logs consuming disk space
- Insufficient partition size

## Fix

Check disk usage:

```bash
du -sh /var/lib/redis/
df -h /var/lib/redis/
```

Trim the AOF:

```bash
redis-cli BGREWRITEAOF
```

Find large keys:

```bash
redis-cli --bigkeys
```

Clean up old data:

```bash
redis-cli FLUSHDB
```

Add disk space or relocate data:

```bash
redis-cli CONFIG SET dir /data/redis/
```

## Examples

```bash
# Check disk usage by file type
find /var/lib/redis/ -type f -exec ls -lh {} \\;

# Monitor disk usage
watch -n 10 'df -h /var/lib/redis/'

# Check inode usage
df -i /var/lib/redis/
```
"""
    ),
    (
        "redis-rdb-checksum-mismatch",
        "Redis RDB Checksum Mismatch Error",
        "How to fix Redis RDB checksum mismatch when loading a corrupted RDB file",
        """## Causes

- RDB file corrupted during write
- Disk sector failure
- File truncated during server crash
- Filesystem corruption

## Fix

Check RDB file integrity:

```bash
redis-check-rdb /var/lib/redis/dump.rdb
```

Attempt repair:

```bash
redis-check-rdb --fix /var/lib/redis/dump.rdb
```

If unfixable, remove the RDB and restart:

```bash
sudo mv /var/lib/redis/dump.rdb /var/lib/redis/dump.rdb.bak
sudo systemctl restart redis
```

Enable AOF for additional safety:

```bash
redis-cli CONFIG SET appendonly yes
```

## Examples

```bash
# Verify RDB checksum
redis-check-rdb /var/lib/redis/dump.rdb

# Check RDB file size
ls -lh /var/lib/redis/dump.rdb

# Monitor RDB save
redis-cli INFO persistence | grep rdb_last_bgsave_status
```
"""
    ),
    (
        "redis-aof-format-error",
        "Redis AOF Format Error",
        "How to fix Redis AOF format parsing errors",
        """## Causes

- AOF file contains invalid Redis protocol
- Partial write during crash
- Manual editing of AOF file
- Version incompatibility

## Fix

Check AOF integrity:

```bash
redis-check-aof /var/lib/redis/appendonly.aof
```

Fix the AOF:

```bash
redis-check-aof --fix /var/lib/redis/appendonly.aof
```

Start with RDB only:

```bash
sudo mv /var/lib/redis/appendonly.aof /var/lib/redis/appendonly.aof.bak
sudo systemctl start redis
# Re-enable AOF
redis-cli CONFIG SET appendonly yes
```

## Examples

```bash
# Check AOF format
redis-check-aof /var/lib/redis/appendonly.aof

# View AOF tail
tail -20 /var/lib/redis/appendonly.aof

# Restart with AOF disabled
redis-server /etc/redis/redis.conf --appendonly no
```
"""
    ),
    (
        "redis-persistence-permission-denied",
        "Redis Persistence Permission Denied",
        "How to fix Redis file permission errors during persistence operations",
        """## Causes

- Redis process does not own the data directory
- SELinux or AppArmor blocking access
- Read-only filesystem

## Fix

Check ownership:

```bash
ls -la /var/lib/redis/
sudo chown -R redis:redis /var/lib/redis/
```

Check SELinux:

```bash
sudo getenforce
sudo ausearch -m avc -ts recent | grep redis
```

Set correct SELinux context:

```bash
sudo semanage fcontext -a -t redis_var_lib_t "/var/lib/redis(/.*)?"
sudo restorecon -Rv /var/lib/redis/
```

## Examples

```bash
# Check file system permissions
namei -l /var/lib/redis/dump.rdb

# Check process user
ps aux | grep redis

# Verify writable directory
sudo -u redis touch /var/lib/redis/test_file && rm /var/lib/redis/test_file
```
"""
    ),
    (
        "redis-bgsave-fork-error",
        "Redis BGSAVE Fork Error",
        "How to fix Redis BGSAVE fork-related errors during background saves",
        """## Causes

- Insufficient memory for fork operation
- vm.overcommit_memory not set
- System load too high for fork
- PID limit reached

## Fix

Set overcommit memory:

```bash
sudo sysctl vm.overcommit_memory=1
```

Check system load:

```bash
uptime
```

Reduce fork overhead by reducing dataset:

```bash
redis-cli CONFIG SET maxmemory 2gb
```

Check fork statistics:

```bash
redis-cli INFO stats | grep fork
```

## Examples

```bash
# Monitor latest fork time
redis-cli INFO stats | grep latest_fork_usec

# Check system memory
free -h

# Trigger and monitor BGSAVE
redis-cli BGSAVE
watch -n 1 'redis-cli INFO persistence | grep rdb_bgsave_in_progress'
```
"""
    ),
    (
        "redis-rdb-background-save-timeout",
        "Redis RDB Background Save Timeout",
        "How to fix Redis RDB background save timeout when BGSAVE takes too long",
        """## Causes

- Large dataset requiring extended save time
- Slow disk I/O
- CPU contention from client operations
- Network storage (NFS) causing slow writes

## Fix

Check save progress:

```bash
redis-cli INFO persistence | grep rdb_bgsave_in_progress
```

Check disk performance:

```bash
iostat -x 1 5
```

Move to local SSD if using network storage:

```bash
redis-cli CONFIG SET dir /mnt/ssd/redis/
```

Monitor save duration:

```bash
redis-cli INFO stats | grep latest_fork_usec
```

## Examples

```bash
# Check BGSAVE status
redis-cli LASTSAVE
redis-cli INFO persistence | grep rdb_last_bgsave_time_sec

# Check disk I/O
iotop -p $(pidof redis-server)

# Benchmark disk write speed
dd if=/dev/zero of=/var/lib/redis/test bs=1M count=1024 oflag=direct
rm /var/lib/redis/test
```
"""
    ),

    # ============================================================
    # 4. Cluster errors
    # ============================================================
    (
        "redis-clusterdown-cluster-is-down",
        "Redis CLUSTERDOWN Cluster Is Down",
        "How to fix Redis CLUSTERDOWN error when the cluster is in a down state",
        """## Common Causes

- Cluster has unassigned slots due to node failure
- Too many master nodes are down
- Cluster state is `fail`
- Minimum number of nodes not met

## How to Fix

Check cluster state:

```bash
redis-cli CLUSTER INFO
```

Check node status:

```bash
redis-cli CLUSTER NODES
```

Bring failed nodes back online:

```bash
sudo systemctl start redis@7001
```

Reassign slots if node is permanently removed:

```bash
redis-cli CLUSTER FORGET <node-id>
```

Force cluster rebuild:

```bash
redis-cli --cluster fix <host>:<port>
```

## Examples

```bash
# Check cluster health
redis-cli CLUSTER INFO | grep cluster_state

# View all nodes
redis-cli CLUSTER NODES | grep -v connected

# Repair cluster
redis-cli --cluster fix 127.0.0.1:7001
```
"""
    ),
    (
        "redis-moved-redirection-error",
        "Redis MOVED Redirection Error",
        "How to fix Redis MOVED redirection error when keys are on a different slot",
        """## Common Causes

- Client does not support cluster protocol
- Hash slot calculation mismatch
- Keys migrated to different node during resharding
- Client cache of slot mappings is stale

## How to Fix

Use a Redis cluster-aware client:

```bash
# Python with redis-py cluster
from redis.cluster import RedisCluster
rc = RedisCluster(host='localhost', port=7001)
```

Check which node owns the slot:

```bash
redis-cli CLUSTER KEYSLOT mykey
redis-cli CLUSTER SLOTS
```

Use hash tags to keep keys in the same slot:

```bash
# Both keys will be in slot 2775
SET {user:1000}.name "John"
SET {user:1000}.email "john@example.com"
```

Update client cluster topology:

```bash
redis-cli CLUSTER SLOTS
```

## Examples

```bash
# Check slot for a key
redis-cli CLUSTER KEYSLOT mykey

# View slot to node mapping
redis-cli CLUSTER SLOTS

# Use hash tags
redis-cli SET {tag}.key1 value1
redis-cli SET {tag}.key2 value2
```
"""
    ),
    (
        "redis-ask-redirection-error",
        "Redis ASK Redirection Error",
        "How to fix Redis ASK redirection error during slot migration",
        """## Common Causes

- Slot is being migrated to another node
- Client sending commands to wrong node during migration
- Client not handling ASK redirection correctly

## How to Fix

Handle ASK redirection in client:

```bash
# The client should:
# 1. Send ASKING command to the target node
# 2. Then retry the command on the target node
```

Check migration status:

```bash
redis-cli CLUSTER NODES | grep migrating
```

Wait for migration to complete:

```bash
redis-cli CLUSTER INFO | grep cluster_slots_assigned
```

## Examples

```bash
# Check slot migration
redis-cli CLUSTER NODES | grep -E "importing|migrating"

# Manually set slot
redis-cli CLUSTER SETSLOT 5000 NODE <node-id>

# Check cluster slots
redis-cli CLUSTER SLOTS
```
"""
    ),
    (
        "redis-crossslot-keys-error",
        "Redis CROSSSLOT Keys Error",
        "How to fix Redis CROSSSLOT error when multi-key operations span multiple slots",
        """## Common Causes

- Keys in a multi-key operation are on different hash slots
- MGET, SUNION, and similar commands operating on keys in different slots
- No hash tag used to force keys into the same slot

## How to Fix

Use hash tags to ensure keys are in the same slot:

```bash
# Use {} hash tag
SET {user:1}.name "Alice"
SET {user:1}.email "alice@example.com"
MGET {user:1}.name {user:1}.email
```

Check which slots the keys belong to:

```bash
redis-cli CLUSTER KEYSLOT key1
redis-cli CLUSTER KEYSLOT key2
```

Move keys to same slot (requires migration):

```bash
redis-cli CLUSTER SETSLOT 1234 MIGRATING <target-node-id>
```

## Examples

```bash
# Check slots for multiple keys
redis-cli CLUSTER KEYSLOT user:1:name
redis-cli CLUSTER KEYSLOT user:1:email

# Use hash tags in commands
redis-cli MGET {user:1}.name {user:1}.email

# Check cluster topology
redis-cli CLUSTER SLOTS
```
"""
    ),
    (
        "redis-slot-not-served-error",
        "Redis Slot Not Served Error",
        "How to fix Redis error when a hash slot is not served by any node",
        """## Causes

- Cluster node failed and its slots are unassigned
- Incomplete cluster setup
- Slot migration failed and left orphaned slots

## Fix

Check unassigned slots:

```bash
redis-cli CLUSTER INFO | grep cluster_slots_ok
redis-cli CLUSTER SLOTS
```

Assign orphaned slots:

```bash
redis-cli CLUSTER ADDSLOTS 0 1 2 3 ... 5460
```

Or use cluster management:

```bash
redis-cli --cluster reshard 127.0.0.1:7001
```

## Examples

```bash
# Check which slots are assigned
redis-cli CLUSTER SLOTS

# Add slots to a node
redis-cli CLUSTER ADDSLOTS 5000 5001 5002

# Check cluster state
redis-cli CLUSTER INFO
```
"""
    ),
    (
        "redis-cluster-state-changed-error",
        "Redis Cluster State Changed Error",
        "How to handle Redis cluster state transitions between ok and fail",
        """## Causes

- Node joining or leaving the cluster
- Network partition between nodes
- Node failure or recovery
- Resharding in progress

## Fix

Monitor cluster state:

```bash
watch -n 2 'redis-cli CLUSTER INFO | grep cluster_state'
```

Check node status:

```bash
redis-cli CLUSTER NODES
```

Wait for cluster to stabilize:

```bash
sleep 15 && redis-cli CLUSTER INFO | grep cluster_state
```

If cluster is in fail, check which nodes are down:

```bash
redis-cli CLUSTER NODES | grep "fail"
```

## Examples

```bash
# Monitor cluster changes
redis-cli CLUSTER INFO

# Check node connectivity
redis-cli CLUSTER NODES | grep -v "connected"

# Check cluster epoch
redis-cli CLUSTER INFO | grep cluster_current_epoch
```
"""
    ),
    (
        "redis-cluster-node-not-reachable",
        "Redis Cluster Node Not Reachable",
        "How to fix Redis cluster node unreachable errors",
        """## Causes

- Node process crashed or was stopped
- Network partition between nodes
- Firewall blocking cluster bus port (port + 10000)
- DNS resolution failure

## Fix

Check if node is running:

```bash
redis-cli -h node-host -p 7001 PING
```

Check cluster bus port:

```bash
ss -tlnp | grep 17001
```

Verify inter-node connectivity:

```bash
redis-cli --cluster check 127.0.0.1:7001
```

Check firewall rules:

```bash
sudo iptables -L -n | grep 7001
```

## Examples

```bash
# Test node connectivity
redis-cli -h 192.168.1.101 -p 7001 PING

# Check cluster bus
redis-cli -h 192.168.1.101 -p 17001 PING

# Verify all nodes see each other
redis-cli CLUSTER NODES | wc -l
```
"""
    ),
    (
        "redis-failover-timeout-error",
        "Redis Cluster Failover Timeout Error",
        "How to fix Redis cluster failover timeout when automatic failover takes too long",
        """## Causes

- Cluster nodes cannot agree on failover
- Network latency between nodes
- Not enough replicas to perform failover
- `cluster-node-timeout` set too low

## Fix

Check cluster node timeout:

```bash
redis-cli CONFIG GET cluster-node-timeout
```

Increase timeout:

```bash
redis-cli CONFIG SET cluster-node-timeout 15000
```

Check cluster state:

```bash
redis-cli CLUSTER NODES | grep -E "fail|fail?"
```

Force manual failover:

```bash
redis-cli CLUSTER FAILOVER
```

## Examples

```bash
# Check failover status
redis-cli CLUSTER INFO | grep cluster_state

# Trigger manual failover
redis-cli -h replica-host -p 7001 CLUSTER FAILOVER

# Check node timeout
redis-cli CONFIG GET cluster-node-timeout
```
"""
    ),
    (
        "redis-gossip-communication-error",
        "Redis Gossip Protocol Communication Error",
        "How to fix Redis cluster gossip protocol communication failures",
        """## Causes

- Cluster bus port (port+10000) not reachable between nodes
- Firewall blocking gossip traffic
- Too many nodes causing gossip overhead
- Network latency affecting protocol timing

## Fix

Check gossip port connectivity:

```bash
redis-cli -h node2 -p 17001 PING
```

Verify cluster bus communication:

```bash
sudo tcpdump -i any port 17001
```

Check cluster bus stats:

```bash
redis-cli INFO cluster | grep cluster_slots
```

Ensure all nodes can reach each other:

```bash
for node in node1 node2 node3; do
  redis-cli -h $node -p 17001 PING
done
```

## Examples

```bash
# Check cluster bus stats
redis-cli CLUSTER INFO

# Test bus connectivity
nc -zv node2 17001

# Monitor gossip messages
sudo tcpdump -i any port 17001 -c 20
```
"""
    ),
    (
        "redis-resharding-error",
        "Redis Cluster Resharding Error",
        "How to fix Redis cluster resharding failures when moving slots between nodes",
        """## Causes

- Target node cannot accept slots (insufficient memory)
- Source node cannot migrate keys
- Network timeout during migration
- Slot already being migrated

## Fix

Check resharding status:

```bash
redis-cli CLUSTER NODES | grep migrating
```

Complete or abort resharding:

```bash
# Complete migration by setting slot to target node
redis-cli CLUSTER SETSLOT 5000 STABLE
```

Check cluster health:

```bash
redis-cli --cluster check 127.0.0.1:7001
```

Use interactive reshard:

```bash
redis-cli --cluster reshard 127.0.0.1:7001
```

## Examples

```bash
# Check migrating slots
redis-cli CLUSTER NODES | grep -i migrating

# Check cluster balance
redis-cli CLUSTER SLOTS | grep -c "127.0.0.1:7001"

# Repair cluster
redis-cli --cluster fix 127.0.0.1:7001
```
"""
    ),
    (
        "redis-cluster-replicas-not-ready",
        "Redis Cluster Replicas Not Ready",
        "How to fix Redis cluster replicas not being in sync with masters",
        """## Causes

- Replicas just started and still doing full sync
- Network latency causing replication delay
- Master overloaded with writes

## Fix

Check replica status:

```bash
redis-cli INFO replication | grep slave
```

Check replication offset:

```bash
redis-cli INFO replication | grep master_repl_offset
redis-cli INFO replication | grep slave_repl_offset
```

Monitor replication lag:

```bash
watch -n 2 'redis-cli INFO replication'
```

## Examples

```bash
# Check master-replica sync
redis-cli INFO replication

# Force replica sync
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master-host master-port

# Check replication backlog
redis-cli INFO replication | grep backlog_active
```
"""
    ),
    (
        "redis-cluster-auth-failed",
        "Redis Cluster AUTH Failed Error",
        "How to fix Redis cluster authentication failures between nodes",
        """## Causes

- Cluster nodes have different passwords
- CLUSTER-AUTH password not configured
- ACL credentials mismatch between nodes

## Fix

Set cluster auth password on all nodes:

```bash
redis-cli -h node1 -p 7001 CONFIG SET cluster-require-full-coverage yes
```

Ensure all nodes have same password:

```bash
# Set on all nodes
redis-cli -h node1 -p 7001 CONFIG SET requirepass "samepassword"
redis-cli -h node2 -p 7002 CONFIG SET requirepass "samepassword"
redis-cli -h node3 -p 7003 CONFIG SET requirepass "samepassword"
```

Update redis.conf on all nodes:

```bash
cluster-auth-pass samepassword
```

## Examples

```bash
# Test node auth
redis-cli -h node1 -p 7001 -a samepassword PING

# Check cluster auth config
redis-cli CONFIG GET cluster-auth

# Test inter-node communication
redis-cli --cluster check 127.0.0.1:7001 -a samepassword
```
"""
    ),

    # ============================================================
    # 5. Sentinel errors
    # ============================================================
    (
        "redis-sentinel-failover-abort",
        "Redis Sentinel Failover Aborted",
        "How to fix Redis Sentinel failover abort errors",
        """## Common Causes

- Target replica too old (replication lag too high)
- Sentinel cannot reach the new master after promotion
- No healthy replica available for promotion
- Network partition during failover

## How to Fix

Check Sentinel status:

```bash
redis-cli -p 26379 SENTINEL masters
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
```

Check replica health:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

View Sentinel logs:

```bash
tail -100 /var/log/redis/sentinel.log
```

Manually trigger failover:

```bash
redis-cli -p 26379 SENTINEL failover mymaster
```

## Examples

```bash
# Check Sentinel masters
redis-cli -p 26379 SENTINEL masters

# View replica info
redis-cli -p 26379 SENTINEL replicas mymaster

# Check failover count
redis-cli -p 26379 SENTINEL failover-count
```
"""
    ),
    (
        "redis-sentinel-no-good-slave",
        "Redis Sentinel No Good Slave Error",
        "How to fix Sentinel no good slave error during failover selection",
        """## Causes

- All replicas are down or unreachable
- Replicas have too high replication lag
- Replica is on the same node as the master
- Replica priority set incorrectly

## Fix

Check replica status:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

Ensure replicas have correct priority:

```bash
redis-cli CONFIG SET replica-priority 100
```

Add more replicas:

```bash
# On new replica
redis-cli REPLICAOF master-host master-port
```

Monitor replica lag:

```bash
redis-cli INFO replication | grep master_repl_offset
```

## Examples

```bash
# Check replica count
redis-cli -p 26379 SENTINEL replicas mymaster | grep -c ip

# Verify replica priority
redis-cli CONFIG GET replica-priority

# Check replication offset
redis-cli INFO replication
```
"""
    ),
    (
        "redis-sentinel-down-error",
        "Redis Sentinel Down Error",
        "How to fix Redis Sentinel down errors when sentinel process is unreachable",
        """## Causes

- Sentinel process crashed
- Port 26379 not listening
- System resource exhaustion
- Configuration error in sentinel.conf

## Fix

Check Sentinel process:

```bash
systemctl status redis-sentinel
```

Start Sentinel:

```bash
sudo systemctl start redis-sentinel
```

Check Sentinel configuration:

```bash
redis-check-sentinel /etc/redis/sentinel.conf
```

Verify Sentinel is listening:

```bash
ss -tlnp | grep 26379
```

## Examples

```bash
# Test Sentinel connection
redis-cli -p 26379 PING

# Check Sentinel ID
redis-cli -p 26379 SENTINEL myid

# View Sentinel info
redis-cli -p 26379 INFO sentinel
```
"""
    ),
    (
        "redis-sentinel-quorum-not-reached",
        "Redis Sentinel Quorum Not Reached Error",
        "How to fix Sentinel quorum not reached errors during failover decisions",
        """## Causes

- Too few Sentinel instances running
- Network partition between Sentinels
- Quorum value higher than available Sentinels
- Sentinel processes unable to communicate

## Fix

Check Sentinel count:

```bash
redis-cli -p 26379 SENTINEL masters | grep num-other-sentinels
```

Adjust quorum:

```bash
redis-cli -p 26379 SENTINEL set mymaster quorum 2
```

Ensure all Sentinels are running:

```bash
for port in 26379 26380 26381; do
  redis-cli -p $port PING
done
```

Check Sentinel connectivity:

```bash
redis-cli -p 26379 SENTINEL sentinels mymaster
```

## Examples

```bash
# Check quorum
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# Verify Sentinel peers
redis-cli -p 26379 SENTINEL sentinels mymaster | grep ip

# Update quorum
redis-cli -p 26379 SENTINEL set mymaster quorum 2
```
"""
    ),
    (
        "redis-sentinel-monitor-duplicate",
        "Redis Sentinel Monitor Duplicate Error",
        "How to fix Sentinel duplicate monitor errors when trying to add duplicate monitoring",
        """## Causes

- Sentinel already monitoring the specified master
- Configuration file contains duplicate MONITOR directives
- Multiple Sentinel instances with overlapping configs

## Fix

Check current monitoring:

```bash
redis-cli -p 26379 SENTINEL masters | grep name
```

Remove duplicate MONITOR from sentinel.conf:

```bash
sudo sed -i '/^sentinel monitor/d' /etc/redis/sentinel.conf
```

Reload Sentinel:

```bash
sudo systemctl restart redis-sentinel
```

## Examples

```bash
# List all monitored masters
redis-cli -p 26379 SENTINEL masters

# Check specific master
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# View Sentinel config
grep monitor /etc/redis/sentinel.conf
```
"""
    ),
    (
        "redis-sentinel-connection-error",
        "Redis Sentinel Connection Error",
        "How to fix Redis Sentinel connection errors when clients cannot connect to Sentinel",
        """## Causes

- Sentinel not listening on the configured port
- Firewall blocking port 26379
- Sentinel bound to wrong interface
- Too many connections to Sentinel

## Fix

Check Sentinel port:

```bash
ss -tlnp | grep 26379
```

Verify Sentinel bind address:

```bash
grep "^bind" /etc/redis/sentinel.conf
```

Test connection:

```bash
redis-cli -h sentinel-host -p 26379 PING
```

Increase maxclients for Sentinel:

```bash
redis-cli -p 26379 CONFIG SET maxclients 10000
```

## Examples

```bash
# Test Sentinel connectivity
redis-cli -h 192.168.1.100 -p 26379 PING

# Check Sentinel clients
redis-cli -p 26379 INFO clients | grep connected_clients

# Check Sentinel config
redis-cli -p 26379 CONFIG GET port
```
"""
    ),
    (
        "redis-sentinel-master-is-down",
        "Redis Sentinel Master Is Down Error",
        "How to fix Redis Sentinel master-is-down notifications and ensure proper failover",
        """## Causes

- Master Redis process crashed
- Master node unreachable due to network issue
- Master ran out of memory and was killed

## Fix

Check Sentinel notification:

```bash
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
```

View master status:

```bash
redis-cli -p 26379 SENTINEL masters
```

Monitor failover progress:

```bash
tail -f /var/log/redis/sentinel.log
```

Check if new master was promoted:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

## Examples

```bash
# Check master status
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# View failover count
redis-cli -p 26379 SENTINEL failover-count

# Check master age
redis-cli -p 26379 SENTINEL masters | grep info-refresh
```
"""
    ),
    (
        "redis-sentinel-slave-not-found",
        "Redis Sentinel Slave Not Found Error",
        "How to fix Sentinel slave not found errors when replica is not registered",
        """## Causes

- Replica not configured with SLAVEOF/REPLICAOF
- Sentinel cannot reach the replica
- Replica is not started

## Fix

Check registered replicas:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

Configure replica in sentinel.conf:

```bash
echo 'sentinel monitor mymaster 127.0.0.1 6379 2' | sudo tee -a /etc/redis/sentinel.conf
```

Add replica to Sentinel monitoring:

```bash
redis-cli -p 26379 SENTINEL set mymaster slave-priority 100
```

## Examples

```bash
# Check replica count
redis-cli -p 26379 SENTINEL replicas mymaster | grep ip

# Verify replica connection
redis-cli -h replica-host -p 6379 INFO replication

# Check Sentinel monitoring
redis-cli -p 26379 SENTINEL masters | grep -A5 name
```
"""
    ),
    (
        "redis-sentinel-config-conflict",
        "Redis Sentinel Configuration Conflict",
        "How to fix Redis Sentinel configuration conflicts between multiple sentinel instances",
        """## Causes

- Different quorum values across Sentinel configs
- Different monitor configurations
- Inconsistent down-after-milliseconds settings

## Fix

Standardize sentinel.conf across all instances:

```bash
# Copy same config to all Sentinel instances
scp /etc/redis/sentinel.conf sentinel2:/etc/redis/sentinel.conf
scp /etc/redis/sentinel.conf sentinel3:/etc/redis/sentinel.conf
```

Restart all Sentinels:

```bash
sudo systemctl restart redis-sentinel
```

Verify consistent configuration:

```bash
for port in 26379 26380 26381; do
  redis-cli -p $port SENTINEL masters
done
```

## Examples

```bash
# Compare Sentinel configurations
diff <(redis-cli -p 26379 SENTINEL masters) \
     <(redis-cli -p 26380 SENTINEL masters)

# Check quorum
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# Verify all Sentinels see same master
for port in 26379 26380 26381; do
  echo "Sentinel $port: $(redis-cli -p $port SENTINEL get-master-addr-by-name mymaster)"
done
```
"""
    ),
    (
        "redis-sentinel-repl-down-error",
        "Redis Sentinel Replication Down Error",
        "How to fix Redis Sentinel error when replica-serve-stale-data affects sentinel decisions",
        """## Causes

- Replica cannot reach master but is still serving
- Stale data being served to clients
- Sentinel not aware of replication state change

## Fix

Check replication state:

```bash
redis-cli -h replica-host -p 6379 INFO replication
```

Check replica-serve-stale-data:

```bash
redis-cli CONFIG GET replica-serve-stale-data
```

Disable stale data serving:

```bash
redis-cli CONFIG SET replica-serve-stale-data no
```

Monitor Sentinel detection:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster | grep slave_repl_offset
```

## Examples

```bash
# Check if replica is stale
redis-cli -h replica-host -p 6379 INFO replication | grep master_link_status

# Force replica to stop serving stale data
redis-cli -h replica-host -p 6379 CONFIG SET replica-serve-stale-data no

# Check Sentinel replica monitoring
redis-cli -p 26379 SENTINEL replicas mymaster
```
"""
    ),

    # ============================================================
    # 6. Data type errors
    # ============================================================
    (
        "redis-wrongtype-operation-error",
        "Redis WRONGTYPE Operation Error",
        "How to fix Redis WRONGTYPE error when operating on a key with wrong data type",
        """## Common Causes

- Trying to use String commands on a Hash key
- Trying to use List commands on a Set key
- Key was overwritten with a different type
- Application logic error causing type mismatch

## How to Fix

Check the key type:

```bash
redis-cli TYPE mykey
```

Use type-appropriate commands:

```bash
# For Hash
redis-cli HGET mykey field

# For List
redis-cli LINDEX mykey 0

# For Set
redis-cli SMEMBERS mykey
```

Delete and recreate with correct type:

```bash
redis-cli DEL mykey
redis-cli HSET mykey field1 value1
```

Use OBJECT ENCODING to check internal type:

```bash
redis-cli OBJECT ENCODING mykey
```

## Examples

```bash
# Wrong - String command on Hash
redis-cli SET myhash key
redis-cli HGET myhash field
# WRONGTYPE Operation against a key holding the wrong kind of value

# Correct
redis-cli HSET myhash field value
redis-cli HGET myhash field
```
"""
    ),
    (
        "redis-hash-field-not-found",
        "Redis Hash Field Not Found Error",
        "How to fix Redis errors when accessing a hash field that does not exist",
        """## Causes

- Field name is incorrect or has typo
- Field was deleted by another process
- Hash key does not exist (returns nil)

## Fix

Check if the field exists:

```bash
redis-cli HEXISTS myhash myfield
```

List all fields:

```bash
redis-cli HGETALL myhash
```

Use HSETNX to set field only if not exists:

```bash
redis-cli HSETNX myhash myfield defaultvalue
```

## Examples

```bash
# Check field existence
redis-cli HEXISTS user:1 email

# Get all fields
redis-cli HGETALL user:1

# Set default value
redis-cli HSETNX user:1 email "unknown@example.com"
```
"""
    ),
    (
        "redis-list-index-out-of-range",
        "Redis List Index Out of Range Error",
        "How to fix Redis list index out of range errors",
        """## Causes

- Index exceeds list length
- List is empty
- Using positive index on a short list

## Fix

Check list length:

```bash
redis-cli LLEN mylist
```

Use negative indices to access from end:

```bash
redis-cli LINDEX mylist -1  # Last element
```

Safely access with index check:

```bash
length=$(redis-cli LLEN mylist)
if [ "$index" -lt "$length" ]; then
  redis-cli LINDEX mylist $index
fi
```

## Examples

```bash
# Check list length
redis-cli LLEN mylist

# Access last element
redis-cli LINDEX mylist -1

# Get range of elements
redis-cli LRANGE mylist 0 10
```
"""
    ),
    (
        "redis-set-member-not-found",
        "Redis Set Member Not Found Error",
        "How to fix Redis errors when set member is not found",
        """## Causes

- Member was removed from the set
- Member name misspelled
- Case sensitivity issues

## Fix

Check set membership:

```bash
redis-cli SISMEMBER myset "member"
```

List all members:

```bash
redis-cli SMEMBERS myset
```

Add member if not exists:

```bash
redis-cli SADD myset "member"
```

## Examples

```bash
# Check if member exists
redis-cli SISMEMBER myset "user1"

# List all members
redis-cli SMEMBERS myset

# Count members
redis-cli SCARD myset
```
"""
    ),
    (
        "redis-sorted-set-score-error",
        "Redis Sorted Set Score Error",
        "How to fix Redis sorted set score-related errors",
        """## Causes

- Score is not a valid floating point number
- Trying to increment score on a member that does not exist
- NAN or INF values in score

## Fix

Verify member exists before incrementing:

```bash
redis-cli ZSCORE myzset member
```

Add member with score:

```bash
redis-cli ZADD myzset 1.0 member
```

Increment score:

```bash
redis-cli ZINCRBY myzset 1.0 member
```

## Examples

```bash
# Check member score
redis-cli ZSCORE myzset player1

# Get rank
redis-cli ZRANK myzset player1

# Increment score
redis-cli ZINCRBY myzset 10 player1
```
"""
    ),
    (
        "redis-hyperloglog-error",
        "Redis HyperLogLog Error",
        "How to fix Redis HyperLogLog merge and configuration errors",
        """## Causes

- PFMERGE with wrong number of arguments
- Source keys do not exist
- Key exists but is not a HyperLogLog

## Fix

Verify key type:

```bash
redis-cli TYPE pfkey
redis-cli OBJECT ENCODING pfkey
```

Add elements before merging:

```bash
redis-cli PFADD pf1 "elem1" "elem2"
redis-cli PFADD pf2 "elem3" "elem4"
redis-cli PFMERGE pfmerged pf1 pf2
```

Check count:

```bash
redis-cli PFCOUNT pfmerged
```

## Examples

```bash
# Add elements
redis-cli PFADD unique_visitors "user1" "user2" "user3"

# Get count
redis-cli PFCOUNT unique_visitors

# Merge two HyperLogLogs
redis-cli PFMERGE merged pf1 pf2
```
"""
    ),
    (
        "redis-stream-id-error",
        "Redis Stream ID Error",
        "How to fix Redis stream ID errors when working with streams",
        """## Causes

- Invalid stream ID format (must be `<millisecondsTime>-<sequenceNumber>`)
- ID already exists (duplicate)
- Trying to read from non-existent stream
- XPENDING with wrong stream ID

## Fix

Generate valid ID:

```bash
# Let Redis auto-generate ID
redis-cli XADD mystream * field value

# Use specific valid ID
redis-cli XADD mystream 1234567890-0 field value
```

Read stream:

```bash
redis-cli XREAD COUNT 10 STREAMS mystream 0
```

Check stream info:

```bash
redis-cli XINFO STREAM mystream
```

## Examples

```bash
# Add to stream with auto ID
redis-cli XADD mystream * name "event1" data "payload"

# Read from specific ID
redis-cli XREAD COUNT 5 STREAMS mystream 1234567890-0

# Check stream length
redis-cli XLEN mystream
```
"""
    ),
    (
        "redis-geospatial-error",
        "Redis Geospatial Command Error",
        "How to fix Redis geospatial command errors",
        """## Causes

- Invalid longitude/latitude values
- GEOADD with wrong number of arguments
- GEOSEARCH with invalid parameters

## Fix

Verify coordinates:

```bash
# Longitude: -180 to 180, Latitude: -85 to 85
redis-cli GEOADD locations 2.3522 48.8566 "Paris"
```

Search within radius:

```bash
redis-cli GEORADIUS locations 2.3522 48.8566 100 km
```

Get distance between points:

```bash
redis-cli GEODIST locations "Paris" "London" km
```

## Examples

```bash
# Add location
redis-cli GEOADD locations 2.3522 48.8566 "Paris"
redis-cli GEOADD locations -0.1278 51.5074 "London"

# Search nearby
redis-cli GEORADIUS locations 2.3522 48.8566 500 km WITHCOORD

# Get distance
redis-cli GEODIST locations "Paris" "London" km
```
"""
    ),
    (
        "redis-bitfield-overflow-error",
        "Redis Bitfield Overflow Error",
        "How to fix Redis bitfield overflow errors",
        """## Causes

- Integer overflow when setting bitfield value
- Bitfield size too small for the value
- Signed/unsigned type mismatch

## Fix

Use overflow handling:

```bash
redis-cli BITFIELD mykey OVERFLOW SAT SET u8 0 255
```

Check available overflow behaviors:

```bash
# WRAP - wrap around
# SAT - saturate at min/max
# FAIL - return nil on overflow
```

Use larger bit size:

```bash
redis-cli BITFIELD mykey SET u16 0 65535
```

## Examples

```bash
# Set with wrap overflow
redis-cli BITFIELD mykey OVERFLOW WRAP SET u8 0 300

# Set with saturation
redis-cli BITFIELD mykey OVERFLOW SAT SET i8 0 127

# Get value
redis-cli BITFIELD mykey GET u8 0
```
"""
    ),
    (
        "redis-string-too-large-error",
        "Redis String Value Too Large Error",
        "How to fix Redis string too large errors when storing values",
        """## Causes

- Value exceeds 512 MB maximum string size
- Client buffer limit exceeded
- Memory allocation failure for large values

## Fix

Check max value size:

```bash
redis-cli CONFIG GET maxmemory
```

Split large values into smaller chunks:

```bash
# Store as hash fields instead of one large string
redis-cli HSET bigdata chunk:0 "part1"
redis-cli HSET bigdata chunk:1 "part2"
```

Use client-side chunking:

```python
import redis
r = redis.Redis()
chunk_size = 1024 * 1024  # 1MB chunks
for i in range(0, len(data), chunk_size):
    r.SET(f"key:{i}", data[i:i+chunk_size])
```

## Examples

```bash
# Check string length
redis-cli STRLEN mykey

# Check max memory
redis-cli CONFIG GET maxmemory

# Use MEMORY USAGE to check size
redis-cli MEMORY USAGE mykey
```
"""
    ),
    (
        "redis-key-type-mismatch",
        "Redis Key Type Mismatch Error",
        "How to fix Redis errors when key type does not match expected type",
        """## Causes

- Key was recreated with a different type
- Concurrent operations changed key type
- Application logic error

## Fix

Check key type and encoding:

```bash
redis-cli TYPE mykey
redis-cli OBJECT ENCODING mykey
redis-cli OBJECT IDLETIME mykey
```

Delete and recreate:

```bash
redis-cli DEL mykey
redis-cli HSET mykey field1 value1
```

Use WATCH to detect concurrent changes:

```bash
redis-cli WATCH mykey
redis-cli TYPE mykey
```

## Examples

```bash
# Check multiple properties of a key
redis-cli TYPE user:1
redis-cli OBJECT ENCODING user:1
redis-cli OBJECT REFCOUNT user:1
redis-cli TTL user:1

# Delete and recreate
redis-cli DEL user:1
redis-cli HSET user:1 name "John"
```
"""
    ),

    # ============================================================
    # 7. Scripting/Lua errors
    # ============================================================
    (
        "redis-busykey-script-running",
        "Redis BUSYKEY Script Running Error",
        "How to fix Redis BUSYKEY error when a Lua script is blocking operations",
        """## Common Causes

- Lua script running for too long
- Script contains infinite loop
- Script performing too many operations
- `lua-time-limit` reached

## How to Fix

Check script timeout setting:

```bash
redis-cli CONFIG GET lua-time-limit
```

Kill the running script:

```bash
redis-cli SCRIPT KILL
```

Increase script time limit:

```bash
redis-cli CONFIG SET lua-time-limit 10000
```

Optimize the Lua script to be faster:

```lua
-- Instead of calling redis.call in a loop, use batch operations
local results = {}
for i, key in ipairs(ARGV) do
    results[i] = redis.call('GET', key)
end
return results
```

## Examples

```bash
# Kill running script
redis-cli SCRIPT KILL

# Check timeout
redis-cli CONFIG GET lua-time-limit

# Monitor script execution
redis-cli INFO stats | grep instantaneousops_per_sec
```
"""
    ),
    (
        "redis-script-killed-error",
        "Redis Script Killed Error",
        "How to fix Redis script killed error when Lua scripts are terminated by timeout",
        """## Causes

- Script exceeded `lua-time-limit`
- Script performed blocking operations
- NOSCRIPT after script was evicted from cache

## Fix

Increase timeout for long scripts:

```bash
redis-cli CONFIG SET lua-time-limit 5000
```

Optimize script to run faster:

```lua
-- Use KEYS and ARGV instead of redis.call inside loops
local val = redis.call('GET', KEYS[1])
return val
```

Cache script with EVALSHA:

```bash
redis-cli EVAL "return redis.call('PING')" 0
redis-cli EVALSHA <sha1> 0
```

## Examples

```bash
# Check script timeout
redis-cli CONFIG GET lua-time-limit

# Find scripts in cache
redis-cli SCRIPT EXISTS

# Clear script cache
redis-cli SCRIPT FLUSH
```
"""
    ),
    (
        "redis-lua-script-timeout",
        "Redis Lua Script Timeout Error",
        "How to fix Redis Lua script timeout when scripts exceed the configured time limit",
        """## Common Causes

- Script doing heavy computation
- Script making too many redis.call() invocations
- Script accessing large datasets
- `lua-time-limit` too low

## How to Fix

Check current timeout:

```bash
redis-cli CONFIG GET lua-time-limit
```

Increase timeout:

```bash
redis-cli CONFIG SET lua-time-limit 10000
```

Rewrite script to be efficient:

```lua
-- Bad: calling EVALSHA multiple times in loop
-- Good: single script with KEYS
local results = {}
for i = 1, #KEYS do
    results[i] = redis.call('GET', KEYS[i])
end
return results
```

Monitor slow scripts:

```bash
redis-cli SLOWLOG GET 10
```

## Examples

```bash
# Increase timeout
redis-cli CONFIG SET lua-time-limit 10000

# Check slow log
redis-cli SLOWLOG GET 5

# Test script execution time
time redis-cli EVAL "return redis.call('PING')" 0
```
"""
    ),
    (
        "redis-lua-syntax-error",
        "Redis Lua Syntax Error",
        "How to fix Redis Lua script syntax errors",
        """## Causes

- Invalid Lua syntax in script
- Missing or extra parentheses/brackets
- Incorrect use of redis.call() or redis.pcall()

## Fix

Validate Lua syntax offline:

```bash
luac -p script.lua
```

Common Lua syntax issues:

```lua
-- Wrong: missing 'local' keyword for local variables
result = redis.call('GET', KEYS[1])  -- will pollute global scope

-- Correct:
local result = redis.call('GET', KEYS[1])
```

Use redis-cli to test script:

```bash
redis-cli EVAL "return 1+1" 0
```

## Examples

```bash
# Test simple script
redis-cli EVAL "return redis.call('PING')" 0

# Test syntax
redis-cli EVAL "
  local x = 1
  local y = 2
  return x + y
" 0

# Find syntax error in log
redis-cli CLIENT LOG GET
```
"""
    ),
    (
        "redis-lua-stack-overflow",
        "Redis Lua Stack Overflow Error",
        "How to fix Redis Lua script stack overflow errors",
        """## Causes

- Too many nested function calls in Lua script
- Deep recursion in Lua script
- Script processing too many nested elements

## Fix

Limit recursion depth:

```lua
local function safe_get(key, depth)
    if depth > 100 then return nil end
    return redis.call('GET', key)
end
```

Use iteration instead of recursion:

```lua
-- Instead of recursive traversal, use iterative approach
local stack = {root_key}
while #stack > 0 do
    local key = table.remove(stack)
    -- process key
end
```

Increase Lua stack size (compile-time change):

```bash
# Requires recompiling Redis with larger LUA_MAXCSTACK
```

## Examples

```bash
# Test recursive script (will fail with deep recursion)
redis-cli EVAL "
  local function f(n) if n == 0 then return 1 end return f(n-1) end
  return f(10000)
" 0

# Use iterative approach
redis-cli EVAL "
  local sum = 0
  for i = 1, 10000 do sum = sum + i end
  return sum
" 0
```
"""
    ),
    (
        "redis-lua-no-writes-allowed",
        "Redis Lua No Writes Allowed Error",
        "How to fix Redis Lua script read-only mode errors",
        """## Causes

- Script uses redis.call() write commands in read-only replica
- Replica configured with `replica-read-only yes`

## Fix

Check replica read-only setting:

```bash
redis-cli CONFIG GET replica-read-only
```

Use redis.pcall() to handle errors gracefully:

```lua
local result = redis.pcall('SET', KEYS[1], ARGV[1])
if result.err then
    return {err = result.err}
end
return result
```

Run write scripts on master:

```bash
redis-cli -h master-host -p 6379 EVAL "..." 0
```

## Examples

```bash
# Check read-only mode
redis-cli CONFIG GET replica-read-only

# Disable read-only (not recommended for replicas)
redis-cli CONFIG SET replica-read-only no

# Run on master
redis-cli -h master-host EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 mykey myvalue
```
"""
    ),
    (
        "redis-evalsha-noscript-error",
        "Redis EVALSHA NOSCRIPT Error",
        "How to fix Redis EVALSHA NOSCRIPT error when script is not in cache",
        """## Causes

- Script was evicted from cache after SCRIPT FLUSH
- Redis server restarted (script cache is in-memory only)
- SHA1 hash mismatch between EVALSHA and actual script

## Fix

Register script first with EVAL:

```bash
redis-cli EVAL "return redis.call('GET', KEYS[1])" 1 mykey
```

Then use EVALSHA with the returned SHA1:

```bash
# Get SHA1
echo -n "return redis.call('GET', KEYS[1])" | sha1sum

# Use EVALSHA
redis-cli EVALSHA <sha1> 1 mykey
```

Handle NOSCRIPT in application:

```python
try:
    r.evalsha(script_sha, 1, 'mykey')
except redis.exceptions.NoScriptError:
    r.eval(script, 1, 'mykey')
```

## Examples

```bash
# Register script
redis-cli EVAL "return redis.call('GET', KEYS[1])" 1 mykey

# Verify script is cached
redis-cli SCRIPT EXISTS <sha1>

# Flush script cache
redis-cli SCRIPT FLUSH
```
"""
    ),
    (
        "redis-lua-wrong-number-of-args",
        "Redis Lua Script Wrong Number of Arguments",
        "How to fix Redis Lua script errors when wrong number of arguments is provided",
        """## Causes

- Number of KEYS does not match declared count in EVAL
- ARGV count mismatch
- Script expects different argument count

## Fix

Check the EVAL call:

```bash
# KEYS count must match the number passed after script
redis-cli EVAL "return KEYS[1]" 1 mykey
# Correct: 1 KEYS argument

# Wrong: passing 2 keys when script expects 1
redis-cli EVAL "return KEYS[1]" 1 key1 key2  # Wrong!
redis-cli EVAL "return KEYS[1] .. KEYS[2]" 2 key1 key2  # Correct
```

Validate in script:

```lua
if #KEYS ~= 2 then
    return {err = "Expected 2 keys"}
end
```

## Examples

```bash
# Correct usage
redis-cli EVAL "return {KEYS[1], ARGV[1]}" 1 mykey myvalue

# Wrong usage (will error)
redis-cli EVAL "return {KEYS[1], KEYS[2]}" 1 key1 key2

# Fix: specify correct KEYS count
redis-cli EVAL "return {KEYS[1], KEYS[2]}" 2 key1 key2
```
"""
    ),
    (
        "redis-lua-redis-call-error",
        "Redis Lua redis.call Error",
        "How to fix Redis Lua script errors from redis.call() failures",
        """## Causes

- redis.call() returns error response
- Invalid command passed to redis.call()
- Wrong number of arguments to redis.call()

## Fix

Use redis.pcall() for error handling:

```lua
local result = redis.pcall('HGET', KEYS[1], ARGV[1])
if result then
    return result
else
    return nil
end
```

Check return type:

```lua
local result = redis.call('GET', KEYS[1])
if result == false then return nil end
if type(result) == 'table' and result.err then
    return {err = result.err}
end
return result
```

## Examples

```bash
# Script with error handling
redis-cli EVAL "
  local ok, result = pcall(redis.call, 'GET', KEYS[1])
  if not ok then return {err = result} end
  return result
" 1 mykey

# Check script error in slow log
redis-cli SLOWLOG GET 5
```
"""
    ),
    (
        "redis-lua-global-variable-error",
        "Redis Lua Global Variable Error",
        "How to fix Redis Lua script global variable errors",
        """## Causes

- Using global variables in Lua scripts
- Missing `local` keyword
- Accidentally polluting global namespace

## Fix

Always use `local` for variables:

```lua
-- Wrong
x = redis.call('GET', KEYS[1])

-- Correct
local x = redis.call('GET', KEYS[1])
```

Check for globals:

```lua
-- Add at start of script
local function main()
    -- all logic here
end
return main()
```

## Examples

```bash
# Good script with local variables
redis-cli EVAL "
  local key = KEYS[1]
  local val = redis.call('GET', key)
  return val
" 1 mykey

# Bad script (global variable)
redis-cli EVAL "
  key = KEYS[1]
  val = redis.call('GET', key)
  return val
" 1 mykey
```
"""
    ),

    # ============================================================
    # 8. Transaction errors
    # ============================================================
    (
        "redis-exec-without-multi-error",
        "Redis EXEC Without MULTI Error",
        "How to fix Redis EXEC without MULTI error when EXEC is called without starting a transaction",
        """## Common Causes

- Client sends EXEC without prior MULTI command
- Connection state lost between MULTI and EXEC
- Client library bug

## How to Fix

Always start transaction with MULTI:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli SET key2 value2
redis-cli EXEC
```

Check if in transaction mode:

```bash
redis-cli EXEC
# If not in MULTI, returns: ERR EXEC without MULTI
```

Use pipeline instead of transaction:

```python
pipe = r.pipeline()
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.execute()
```

## Examples

```bash
# Correct transaction
redis-cli MULTI
OK
redis-cli SET a 1
QUEUED
redis-cli SET b 2
QUEUED
redis-cli EXEC
1) OK
2) OK

# Wrong - EXEC without MULTI
redis-cli EXEC
# ERR EXEC without MULTI
```
"""
    ),
    (
        "redis-watch-inside-multi-error",
        "Redis WATCH Inside MULTI Error",
        "How to fix Redis WATCH inside MULTI error when WATCH is used inside a transaction",
        """## Common Causes

- WATCH command used after MULTI
- Client library error in transaction handling

## How to Fix

Use WATCH before MULTI:

```bash
# Correct order
redis-cli WATCH mykey
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```

For multiple keys:

```bash
redis-cli WATCH key1 key2
redis-cli MULTI
redis-cli SET key1 value1
redis-cli SET key2 value2
redis-cli EXEC
```

## Examples

```bash
# Wrong: WATCH inside MULTI
redis-cli MULTI
redis-cli WATCH mykey
# ERR WATCH inside MULTI

# Correct: WATCH before MULTI
redis-cli WATCH mykey
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```
"""
    ),
    (
        "redis-discard-without-multi-error",
        "Redis DISCARD Without MULTI Error",
        "How to fix Redis DISCARD without MULTI error",
        """## Common Causes

- Client sends DISCARD without starting a transaction with MULTI
- Connection state issue

## Fix

Start transaction first:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli DISCARD
```

Check if in transaction mode:

```bash
redis-cli DISCARD
# ERR DISCARD without MULTI
```

## Examples

```bash
# Correct usage
redis-cli MULTI
OK
redis-cli SET key1 value1
QUEUED
redis-cli DISCARD
OK

# Wrong usage
redis-cli DISCARD
# ERR DISCARD without MULTI
```
"""
    ),
    (
        "redis-queued-failed-error",
        "Redis QUEUED Command Failed Error",
        "How to fix Redis command queuing failure inside a transaction",
        """## Causes

- Command syntax error in queued command
- Wrong number of arguments for a queued command
- Command not supported inside MULTI

## Fix

Verify commands before queuing:

```bash
redis-cli MULTI
redis-cli SET key1 value1
# Check for syntax errors
redis-cli EXEC
```

Non-queueable commands in MULTI:

```bash
# These commands cannot be queued
redis-cli MULTI
redis-cli MULTI  # will fail
redis-cli EXEC
```

## Examples

```bash
# Correct transaction
redis-cli MULTI
OK
redis-cli SET key1 value1
QUEUED
redis-cli SET key2 value2
QUEUED
redis-cli EXEC

# Command with error (will fail at EXEC)
redis-cli MULTI
redis-cli SET key1 value1
QUEUED
redis-cli INCR key1  # OK if key1 is string
redis-cli EXEC
```
"""
    ),
    (
        "redis-transaction-aborted-error",
        "Redis Transaction Aborted Error",
        "How to fix Redis transaction aborted errors due to WATCH failures",
        """## Causes

- WATCHed key was modified between WATCH and EXEC
- Another client modified the watched key
- Optimistic lock conflict

## Fix

Retry the transaction:

```python
import redis
r = redis.Redis()

while True:
    try:
        pipe = r.pipeline()
        pipe.watch('mykey')
        val = pipe.get('mykey')
        pipe.multi()
        pipe.set('mykey', new_value)
        pipe.execute()
        break
    except redis.exceptions.WatchError:
        continue  # Retry
```

Check watched keys:

```bash
redis-cli WATCH mykey
redis-cli MULTI
redis-cli EXEC
# If WATCHed key changed: EXECABORT Transaction discarded
```

## Examples

```bash
# Transaction with retry logic
# Terminal 1:
redis-cli WATCH counter
redis-cli GET counter
redis-cli MULTI
redis-cli INCR counter
redis-cli EXEC
# May return: EXECABORT if counter changed

# Terminal 2 (during Terminal 1's WATCH):
redis-cli INCR counter  # This causes Terminal 1's EXEC to fail
```
"""
    ),
    (
        "redis-optimistic-lock-failure",
        "Redis Optimistic Lock Failure Error",
        "How to fix Redis optimistic lock failure when concurrent modifications are detected",
        """## Causes

- High contention on a single key
- Multiple clients trying to update same key simultaneously
- Long processing time between WATCH and EXEC

## Fix

Implement retry with backoff:

```python
import time
import redis

r = redis.Redis()

for attempt in range(5):
    try:
        with r.pipeline() as pipe:
            pipe.watch('balance')
            balance = int(pipe.get('balance'))
            pipe.multi()
            pipe.set('balance', balance - 100)
            pipe.execute()
            break
    except redis.exceptions.WatchError:
        time.sleep(0.1 * (attempt + 1))
```

Reduce contention window:

```bash
# Quick WATCH-MULTI-EXEC
redis-cli WATCH mykey
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```

## Examples

```bash
# Fast transaction to reduce contention
redis-cli WATCH account:balance
redis-cli MULTI
redis-cli DECRBY account:balance 100
redis-cli EXEC
```
"""
    ),
    (
        "redis-multi-exec-nested-error",
        "Redis MULTI EXEC Nested Transaction Error",
        "How to fix Redis nested transaction errors when MULTI is called inside a transaction",
        """## Causes

- Attempting to start a new MULTI inside an active MULTI block
- Client library error

## Fix

Do not nest MULTI:

```bash
# Wrong
redis-cli MULTI
redis-cli MULTI  # ERR MULTI calls can not be nested
redis-cli EXEC

# Correct - single MULTI block
redis-cli MULTI
redis-cli SET key1 value1
redis-cli EXEC
```

Use pipelining for batching:

```python
pipe = r.pipeline(transaction=False)
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
pipe.execute()
```

## Examples

```bash
# Correct transaction
redis-cli MULTI
OK
redis-cli SET a 1
QUEUED
redis-cli EXEC
1) OK

# Wrong - nested MULTI
redis-cli MULTI
redis-cli MULTI
# ERR MULTI calls can not be nested
```
"""
    ),
    (
        "redis-watch-timeout-error",
        "Redis WATCH Timeout Error",
        "How to fix Redis WATCH timeout when the optimistic lock hold time expires",
        """## Causes

- Too long between WATCH and EXEC
- Application processing delay
- Network latency

## Fix

Minimize time between WATCH and EXEC:

```bash
redis-cli WATCH mykey
# Do minimal processing
redis-cli MULTI
redis-cli SET mykey newvalue
redis-cli EXEC
```

Use WATCH with timeout handling:

```python
import redis
r = redis.Redis()
r.execute_command('CLIENT', 'SETNAME', 'myapp')
```

## Examples

```bash
# Fast transaction
redis-cli WATCH counter && redis-cli MULTI && redis-cli INCR counter && redis-cli EXEC

# Monitor WATCH operations
redis-cli MONITOR | grep WATCH
```
"""
    ),
    (
        "redis-exec-abort-error",
        "Redis EXECABORT Transaction Discarded Error",
        "How to fix Redis EXECABORT error when transaction is automatically discarded",
        """## Causes

- WATCHed key modified during transaction
- Server rejecting transaction due to memory
- Command syntax error inside MULTI block

## Fix

Check what commands were queued:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli EXEC
```

Retry without WATCH if not needed:

```bash
redis-cli MULTI
redis-cli SET key1 value1
redis-cli EXEC
```

Use UNWATCH to cancel:

```bash
redis-cli WATCH mykey
redis-cli UNWATCH
```

## Examples

```bash
# Simple transaction without WATCH
redis-cli MULTI
redis-cli SET name "John"
redis-cli SET age "30"
redis-cli EXEC

# Cancel WATCH if not needed
redis-cli WATCH mykey
redis-cli UNWATCH
```
"""
    ),

    # ============================================================
    # 9. Replication errors
    # ============================================================
    (
        "redis-masterdown-replica-stale-error",
        "Redis MASTERDOWN Replica Stale Data Error",
        "How to fix Redis MASTERDOWN error when replica-serve-stale-data is set to no",
        """## Common Causes

- Master is down and replica-serve-stale-data is set to no
- Replica is not serving any data during master outage
- Connection to master lost

## How to Fix

Check replica status:

```bash
redis-cli INFO replication | grep master_link_status
```

Check stale data setting:

```bash
redis-cli CONFIG GET replica-serve-stale-data
```

Temporarily allow stale data:

```bash
redis-cli CONFIG SET replica-serve-stale-data yes
```

Check master connection:

```bash
redis-cli INFO replication | grep master_host
```

## Examples

```bash
# Check master link status
redis-cli INFO replication | grep master_link_status

# Allow stale data temporarily
redis-cli CONFIG SET replica-serve-stale-data yes

# Check replica offset
redis-cli INFO replication | grep slave_repl_offset
```
"""
    ),
    (
        "redis-replication-delay-error",
        "Redis Replication Delay Error",
        "How to fix Redis replication delay and lag issues",
        """## Common Causes

- High write throughput on master
- Network latency between master and replica
- Replica disk I/O bottleneck
- Replication backlog too small

## How to Fix

Check replication lag:

```bash
redis-cli INFO replication | grep master_repl_offset
redis-cli INFO replication | grep slave_repl_offset
```

Increase replication backlog:

```bash
redis-cli CONFIG SET repl-backlog-size 256mb
```

Check network latency:

```bash
redis-cli --latency -h master-host
```

Monitor replica offset:

```bash
watch -n 1 'redis-cli INFO replication | grep -E "master_repl_offset|slave_repl_offset"'
```

## Examples

```bash
# Check replication status
redis-cli INFO replication

# Increase backlog
redis-cli CONFIG SET repl-backlog-size 256mb

# Check replica ping
redis-cli INFO replication | grep master_last_io_seconds_ago
```
"""
    ),
    (
        "redis-replication-backlog-not-available",
        "Redis Replication Backlog Not Available Error",
        "How to fix Redis replication backlog not available errors",
        """## Causes

- Replication backlog disabled (repl-backlog-size set to 0)
- Backlog too small for the write volume
- Backlog flushed after long disconnection

## Fix

Enable and size the backlog:

```bash
redis-cli CONFIG SET repl-backlog-size 128mb
```

Check backlog status:

```bash
redis-cli INFO replication | grep repl_backlog_active
```

Monitor backlog usage:

```bash
redis-cli INFO replication | grep repl_backlog_histlen
```

Set appropriate backlog TTL:

```bash
redis-cli CONFIG SET repl-backlog-ttl 3600
```

## Examples

```bash
# Check backlog size
redis-cli INFO replication | grep repl_backlog_size

# Set backlog to 256MB
redis-cli CONFIG SET repl-backlog-size 256mb

# Check if backlog is active
redis-cli INFO replication | grep repl_backlog_active
```
"""
    ),
    (
        "redis-partial-resync-failed",
        "Redis Partial Resync Failed Error",
        "How to fix Redis partial resynchronization failure during replication",
        """## Common Causes

- Replication ID changed (master failover occurred)
- Backlog does not contain the needed offset
- Replica was disconnected too long
- Master restarted and changed replication ID

## Fix

Check replication IDs:

```bash
redis-cli INFO replication | grep master_replid
```

Force full resync:

```bash
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master-host master-port
```

Increase backlog size:

```bash
redis-cli CONFIG SET repl-backlog-size 512mb
```

Monitor resync status:

```bash
redis-cli INFO replication | grep master_sync_in_progress
```

## Examples

```bash
# Check replication status
redis-cli INFO replication

# Force full resync
redis-cli -h replica REPLICAOF NO ONE
redis-cli -h replica REPLICAOF master 6379

# Check replid
redis-cli INFO replication | grep master_replid
```
"""
    ),
    (
        "redis-full-sync-failed",
        "Redis Full Resync Failed Error",
        "How to fix Redis full synchronization failure during initial replica setup",
        """## Causes

- Master cannot fork process for RDB save
- Network timeout during large dataset transfer
- Disk full on replica for RDB storage
- Master overloaded

## Fix

Check disk space on replica:

```bash
df -h /var/lib/redis/
```

Check master fork capability:

```bash
sysctl vm.overcommit_memory
```

Monitor sync progress:

```bash
redis-cli INFO replication | grep master_sync_in_progress
```

Increase timeout for large datasets:

```bash
redis-cli CONFIG SET repl-timeout 600
```

## Examples

```bash
# Check sync status
redis-cli INFO replication | grep -E "master_sync|master_repl"

# Monitor disk usage during sync
watch -n 2 'df -h /var/lib/redis/'

# Check master CPU during sync
top -p $(pidof redis-server)
```
"""
    ),
    (
        "redis-psync-invalid-id-error",
        "Redis PSYNC Invalid Replication ID Error",
        "How to fix Redis PSYNC invalid replication ID errors during resynchronization",
        """## Causes

- Replica has stale replication ID after master failover
- Replication ID mismatch between master and replica

## Fix

Check current replication ID:

```bash
redis-cli INFO replication | grep master_replid
```

Reset replication on replica:

```bash
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master-host master-port
```

Verify new replication ID:

```bash
redis-cli INFO replication | grep master_replid2
```

## Examples

```bash
# Check replication IDs
redis-cli INFO replication | grep replid

# Reset and re-sync
redis-cli -h replica REPLICAOF NO ONE
sleep 2
redis-cli -h replica REPLICAOF new-master 6379

# Check sync status
redis-cli -h replica INFO replication | grep master_link_status
```
"""
    ),
    (
        "redis-replica-priority-error",
        "Redis Replica Priority Error",
        "How to fix Redis replica-priority configuration errors during failover",
        """## Causes

- Replica-priority set to 0 (ineligible for promotion)
- All replicas have priority 0
- Sentinel cannot find a suitable replica to promote

## Fix

Check replica priority:

```bash
redis-cli CONFIG GET replica-priority
```

Set correct priority:

```bash
# Primary replica (higher priority = less likely to be promoted first)
redis-cli CONFIG SET replica-priority 100

# Replica that should never be promoted
redis-cli CONFIG SET replica-priority 0
```

## Examples

```bash
# Check priority
redis-cli CONFIG GET replica-priority

# Set priority for sentinel failover
redis-cli CONFIG SET replica-priority 50

# Check Sentinel view
redis-cli -p 26379 SENTINEL replicas mymaster | grep priority
```
"""
    ),
    (
        "redis-replication-connection-error",
        "Redis Replication Connection Error",
        "How to fix Redis replication connection errors between master and replica",
        """## Causes

- Master IP/port changed in replica config
- Firewall blocking replication port
- Master authentication required but replica not configured
- Network unreachable

## Fix

Check replication config:

```bash
redis-cli CONFIG GET replicaof
```

Update replica to point to master:

```bash
redis-cli REPLICAOF master-ip master-port
```

Set master auth password:

```bash
redis-cli CONFIG SET masterauth "master_password"
```

Check connectivity:

```bash
redis-cli -h master-host -p 6379 PING
```

## Examples

```bash
# Check current master
redis-cli INFO replication | grep master_host

# Update master
redis-cli REPLICAOF 192.168.1.100 6379

# Set master auth
redis-cli CONFIG SET masterauth "password123"
```
"""
    ),
    (
        "redis-replica-read-only-error",
        "Redis Replica Read Only Error",
        "How to fix Redis replica read-only errors when trying to write to a replica",
        """## Causes

- Replica configured with replica-read-only yes
- Application writing to replica instead of master

## Fix

Check read-only setting:

```bash
redis-cli CONFIG GET replica-read-only
```

Disable read-only (not recommended):

```bash
redis-cli CONFIG SET replica-read-only no
```

Route writes to master:

```bash
redis-cli -h master-host -p 6379 SET key value
```

## Examples

```bash
# Check if replica is read-only
redis-cli CONFIG GET replica-read-only

# Write to master
redis-cli -h master-host SET key value

# Read from replica
redis-cli -h replica-host GET key
```
"""
    ),
    (
        "redis-replication-reconnect-error",
        "Redis Replication Reconnect Error",
        "How to fix Redis replication reconnection errors after temporary disconnection",
        """## Causes

- Master restarted and lost replication state
- Network partition resolved but backlog expired
- Replication ID changed on master

## Fix

Check connection status:

```bash
redis-cli INFO replication | grep master_link_status
```

Force reconnection:

```bash
redis-cli REPLICAOF NO ONE
sleep 1
redis-cli REPLICAOF master-host master-port
```

Increase backlog TTL:

```bash
redis-cli CONFIG SET repl-backlog-ttl 86400
```

Monitor reconnection:

```bash
watch -n 2 'redis-cli INFO replication | grep master_link_status'
```

## Examples

```bash
# Check replication status
redis-cli INFO replication | grep -E "master_link|master_last_io"

# Force full resync
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master 6379

# Monitor reconnection
tail -f /var/log/redis/redis-server.log | grep -i replic
```
"""
    ),

    # ============================================================
    # 10. Pub/Sub errors
    # ============================================================
    (
        "redis-pubsub-subscribe-timeout",
        "Redis Pub/Sub Subscribe Timeout Error",
        "How to fix Redis Pub/Sub subscribe timeout when subscription connection times out",
        """## Common Causes

- Network issue blocking subscribe connection
- Server not responding to SUBSCRIBE
- Client timeout set too low
- Too many subscriptions on single connection

## Fix

Check subscription count:

```bash
redis-cli PUBSUB NUMSUB channel1 channel2
```

Use dedicated connection for Pub/Sub:

```python
import redis
pubsub_r = redis.Redis(host='localhost', port=6379, socket_timeout=None)
pubsub = pubsub_r.pubsub()
pubsub.subscribe('mychannel')
```

Monitor subscriptions:

```bash
redis-cli CLIENT LIST | grep subscribe
```

## Examples

```bash
# Test subscribe
redis-cli SUBSCRIBE mychannel

# Check active subscriptions
redis-cli INFO clients | grep blocked_clients

# Check channel count
redis-cli PUBSUB CHANNELS
```
"""
    ),
    (
        "redis-pubsub-too-many-patterns",
        "Redis Pub/Sub Too Many Patterns Error",
        "How to fix Redis Pub/Sub pattern subscription limit errors",
        """## Causes

- Too many PSUBSCRIBE patterns active
- Pattern matching memory overhead too high
- Pattern subscription leak in application

## Fix

Check pattern count:

```bash
redis-cli PUBSUB NUMPAT
```

Unsubscribe unused patterns:

```bash
redis-cli PUNSUBSCRIBE pattern:*
```

Use specific channels instead of patterns:

```bash
# Instead of PSUBSCRIBE user:*
redis-cli SUBSCRIBE user:1000 user:1001 user:1002
```

## Examples

```bash
# Check pattern count
redis-cli PUBSUB NUMPAT

# List active patterns
redis-cli PSUBSCRIBE "test*"
redis-cli PUNSUBSCRIBE "test*"

# Use direct channel subscription
redis-cli SUBSCRIBE specific_channel
```
"""
    ),
    (
        "redis-pubsub-channel-not-found",
        "Redis Pub/Sub Channel Not Found Error",
        "How to fix Redis Pub/Sub channel not found when publishing to non-existent channel",
        """## Causes

- Channel name mismatch (case-sensitive)
- Subscribers disconnected before publish
- Channel was never subscribed to

## Fix

Check active channels:

```bash
redis-cli PUBSUB CHANNELS
```

Verify channel name:

```bash
redis-cli PUBSUB CHANNELS "pattern*"
```

Subscribe before publishing:

```bash
# Terminal 1 (subscriber)
redis-cli SUBSCRIBE mychannel

# Terminal 2 (publisher)
redis-cli PUBLISH mychannel "hello"
```

## Examples

```bash
# List active channels
redis-cli PUBSUB CHANNELS

# Check channel subscriber count
redis-cli PUBSUB NUMSUB mychannel

# Test publish
redis-cli PUBLISH mychannel "test message"
```
"""
    ),
    (
        "redis-pubsub-unsubscribe-error",
        "Redis Pub/Sub Unsubscribe Error",
        "How to fix Redis Pub/Sub unsubscribe errors",
        """## Causes

- Trying to unsubscribe from channel not subscribed to
- Connection closed before unsubscribe
- Protocol error in unsubscribe command

## Fix

Check subscriptions:

```bash
redis-cli SUBSCRIBE  # enters subscribe mode, shows active channels
```

Unsubscribe cleanly:

```bash
redis-cli UNSUBSCRIBE channel1 channel2
```

Use PUNSUBSCRIBE for pattern:

```bash
redis-cli PUNSUBSCRIBE "pattern*"
```

## Examples

```bash
# Subscribe to channels
redis-cli SUBSCRIBE ch1 ch2 ch3

# Unsubscribe from specific channels
redis-cli UNSUBSCRIBE ch1

# Unsubscribe from all
redis-cli UNSUBSCRIBE
```
"""
    ),
    (
        "redis-pubsub-pattern-mismatch",
        "Redis Pub/Sub Pattern Mismatch Error",
        "How to fix Redis Pub/Sub pattern mismatch when PSUBSCRIBE patterns don't match expected channels",
        """## Causes

- Pattern syntax incorrect
- Channel name format changed
- Wildcard placement wrong

## Fix

Test pattern match:

```bash
redis-cli PUBSUB CHANNELS "user:*"
```

Common patterns:

```bash
# Match all channels
redis-cli PSUBSCRIBE *

# Match channels starting with user:
redis-cli PSUBSCRIBE "user:*"

# Match channels ending with :events
redis-cli PSUBSCRIBE "*:events"
```

Check matching channels:

```bash
redis-cli PUBSUB CHANNELS "pattern"
```

## Examples

```bash
# Subscribe with pattern
redis-cli PSUBSCRIBE "notifications:*"

# Check matching channels
redis-cli PUBSUB CHANNELS "notifications:*"

# Publish to matching channel
redis-cli PUBLISH notifications:email "new message"
```
"""
    ),
    (
        "redis-pubsub-message-too-large",
        "Redis Pub/Sub Message Too Large Error",
        "How to fix Redis Pub/Sub message too large errors",
        """## Causes

- Message exceeds max message size
- Client buffer overflow
- Memory pressure on subscribers

## Fix

Check max message size:

```bash
redis-cli CONFIG GET maxmemory
```

Split large messages:

```python
import json
data = {"large_payload": "..." * 10000}
chunks = [data[i:i+1000] for i in range(0, len(data), 1000)]
for chunk in chunks:
    r.publish('channel', json.dumps(chunk))
```

Monitor message size:

```bash
redis-cli MEMORY USAGE channel
```

## Examples

```bash
# Check memory usage of channel
redis-cli MEMORY USAGE channel

# Publish small message
redis-cli PUBLISH channel "small message"

# Monitor pubsub memory
redis-cli INFO memory | grep used_memory_human
```
"""
    ),
    (
        "redis-pubsub-no-subscribers-error",
        "Redis Pub/Sub No Subscribers Error",
        "How to handle Redis Pub/Sub messages sent to channels with no subscribers",
        """## Causes

- All subscribers disconnected
- Publishing before subscribing
- Channel name mismatch

## Fix

Check subscriber count:

```bash
redis-cli PUBSUB NUMSUB mychannel
```

Ensure subscriber connects first:

```python
# Subscriber must connect first
pubsub = r.pubsub()
pubsub.subscribe('mychannel')
# Then publisher sends
r.publish('mychannel', 'message')
```

Monitor subscriber count:

```bash
watch -n 1 'redis-cli PUBSUB NUMSUB mychannel'
```

## Examples

```bash
# Check subscribers
redis-cli PUBSUB NUMSUB mychannel

# List all channels with subscribers
redis-cli PUBSUB NUMSUB

# Publish and check result (returns 0 if no subscribers)
redis-cli PUBLISH mychannel "test"
```
"""
    ),
    (
        "redis-pubsub-buffer-full",
        "Redis Pub/Sub Client Buffer Full Error",
        "How to fix Redis Pub/Sub client output buffer full errors",
        """## Causes

- Subscriber consuming messages too slowly
- Buffer limit exceeded for subscriber
- Network congestion causing message buildup

## Fix

Check buffer configuration:

```bash
redis-cli CONFIG GET client-output-buffer-limit
```

Increase buffer for pub/sub clients:

```bash
redis-cli CONFIG SET client-output-buffer-limit "pubsub 0 0 0"
```

Monitor client buffer:

```bash
redis-cli CLIENT LIST
```

Speed up subscriber processing:

```python
pubsub = r.pubsub()
pubsub.subscribe('channel')
for message in pubsub.listen():
    process(message)  # Fast processing
```

## Examples

```bash
# Check buffer config
redis-cli CONFIG GET client-output-buffer-limit

# Monitor client output
redis-cli CLIENT LIST | grep pubsub

# Check buffer usage
redis-cli INFO clients | grep client_recent_max_output_buffer_size
```
"""
    ),

    # ============================================================
    # 11. Configuration errors
    # ============================================================
    (
        "redis-unknown-config-parameter",
        "Redis Unknown Config Parameter Error",
        "How to fix Redis unknown configuration parameter errors",
        """## Common Causes

- Typo in redis.conf parameter name
- Using config parameter from wrong Redis version
- Deprecated configuration option

## How to Fix

Check valid parameters:

```bash
redis-cli CONFIG GET *
```

Search documentation for correct parameter:

```bash
redis-cli CONFIG SET maxmemory 4gb  # valid
redis-cli CONFIG SET max_mem 4gb    # invalid: unknown config parameter
```

View current config file:

```bash
grep -v "^#" /etc/redis/redis.conf | grep -v "^$"
```

## Examples

```bash
# List all config parameters
redis-cli CONFIG GET * | head -20

# Test parameter
redis-cli CONFIG SET maxmemory-policy allkeys-lru

# Check parameter exists
redis-cli CONFIG GET maxmemory-policy
```
"""
    ),
    (
        "redis-invalid-port-error",
        "Redis Invalid Port Error",
        "How to fix Redis invalid port configuration errors",
        """## Causes

- Port number out of valid range (1-65535)
- Port already in use by another service
- Port requires root privileges (< 1024)

## Fix

Check port availability:

```bash
ss -tlnp | grep 6379
```

Use valid port range:

```bash
# Valid ports: 1-65535
# Common: 6379 (default), 6380, 6381, etc.
```

Check redis.conf:

```bash
grep "^port" /etc/redis/redis.conf
```

Test port binding:

```bash
redis-server --port 6380
```

## Examples

```bash
# Check if port is in use
ss -tlnp | grep 6379

# Start Redis on different port
redis-server --port 6380

# Check listening ports
netstat -tlnp | grep redis
```
"""
    ),
    (
        "redis-bind-address-failed",
        "Redis Bind Address Failed Error",
        "How to fix Redis bind address configuration errors",
        """## Causes

- Trying to bind to non-existent interface
- Permission denied for privileged ports
- Multiple bind addresses conflicting
- Network interface down

## Fix

Check available interfaces:

```bash
ip addr show
```

Bind to all interfaces:

```bash
redis-cli CONFIG SET bind 0.0.0.0
```

Or specific interface:

```bash
redis-cli CONFIG SET bind 192.168.1.100
```

Update redis.conf:

```bash
sudo sed -i 's/^bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf
sudo systemctl restart redis
```

## Examples

```bash
# Check listening addresses
ss -tlnp | grep 6379

# Test bind to specific address
redis-server --bind 192.168.1.100 --port 6379

# Check interfaces
ip addr show | grep inet
```
"""
    ),
    (
        "redis-protected-mode-error",
        "Redis Protected Mode Error",
        "How to fix Redis protected mode error when binding to non-loopback interfaces",
        """## Common Causes

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
"""
    ),
    (
        "redis-daemonize-error",
        "Redis Daemonize Error",
        "How to fix Redis daemonize configuration errors",
        """## Causes

- Cannot daemonize when run with systemd
- PID file directory not writable
- Already running as daemon

## Fix

Check daemonize setting:

```bash
redis-cli CONFIG GET daemonize
```

Disable daemonize when using systemd:

```bash
sudo sed -i 's/^daemonize yes/daemonize no/' /etc/redis/redis.conf
```

Check PID file:

```bash
ls -la /var/run/redis/
cat /var/run/redis/redis-server.pid
```

Start Redis properly with systemd:

```bash
sudo systemctl start redis
```

## Examples

```bash
# Check if Redis is running as daemon
ps aux | grep redis-server

# Check PID file
cat /var/run/redis/redis-server.pid

# Start with systemd
sudo systemctl start redis
```
"""
    ),
    (
        "redis-logfile-permission-error",
        "Redis Log File Permission Error",
        "How to fix Redis log file permission and access errors",
        """## Causes

- Log file directory not writable by redis user
- Log file owned by wrong user
- Disk full preventing log writes

## Fix

Check log file permissions:

```bash
ls -la /var/log/redis/
sudo chown redis:redis /var/log/redis/redis-server.log
sudo chmod 644 /var/log/redis/redis-server.log
```

Check disk space:

```bash
df -h /var/log/
```

Update log configuration:

```bash
redis-cli CONFIG SET logfile /var/log/redis/redis-server.log
redis-cli CONFIG SET loglevel verbose
```

## Examples

```bash
# Check log file
ls -la /var/log/redis/

# View Redis logs
sudo tail -50 /var/log/redis/redis-server.log

# Set log level
redis-cli CONFIG SET loglevel verbose
```
"""
    ),
    (
        "redis-slowlog-error",
        "Redis Slowlog Configuration Error",
        "How to fix Redis slowlog configuration and retention issues",
        """## Causes

- Slowlog-max-len too small (losing entries)
- Slowlog-log-slower-than set too high
- Slowlog consuming too much memory

## Fix

Check slowlog configuration:

```bash
redis-cli CONFIG GET slowlog-log-slower-than
redis-cli CONFIG GET slowlog-max-len
```

Adjust slowlog settings:

```bash
# Log queries slower than 10ms
redis-cli CONFIG SET slowlog-log-slower-than 10000

# Keep last 1000 entries
redis-cli CONFIG SET slowlog-max-len 1000
```

View slow log:

```bash
redis-cli SLOWLOG GET 10
redis-cli SLOWLOG LEN
```

## Examples

```bash
# Check slowlog entries
redis-cli SLOWLOG GET 5

# Reset slowlog
redis-cli SLOWLOG RESET

# Check slowlog length
redis-cli SLOWLOG LEN
```
"""
    ),
    (
        "redis-rename-command-blocked",
        "Redis Rename Command Blocked Error",
        "How to fix Redis rename-command errors when commands are disabled",
        """## Causes

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
"""
    ),
    (
        "redis-acl-parse-error",
        "Redis ACL Parse Error",
        "How to fix Redis ACL configuration parsing errors",
        """## Causes

- Invalid ACL syntax in redis.conf
- Wrong permission format
- Invalid channel pattern

## Fix

Check ACL file:

```bash
cat /etc/redis/users.acl
```

Test ACL command:

```bash
redis-cli ACL SETUSER testuser on >password ~* +@all
```

View current ACL:

```bash
redis-cli ACL LIST
```

Validate ACL syntax:

```bash
redis-cli ACL WHOAMI
redis-cli ACL LOG
```

## Examples

```bash
# Create user with correct ACL syntax
redis-cli ACL SETUSER myuser on >password123 ~data:* +get +set

# Check ACL errors
redis-cli ACL LOG

# List all users
redis-cli ACL LIST
```
"""
    ),
    (
        "redis-user-not-found-error",
        "Redis ACL User Not Found Error",
        "How to fix Redis ACL user not found errors",
        """## Causes

- User does not exist in ACL
- Wrong username in AUTH command
- ACL file not loaded

## Fix

List all users:

```bash
redis-cli ACL LIST
```

Create user:

```bash
redis-cli ACL SETUSER newuser on >password ~* +@all
```

Check user permissions:

```bash
redis-cli ACL GETUSER newuser
```

Load ACL file:

```bash
redis-cli ACL LOAD
```

## Examples

```bash
# Check users
redis-cli ACL LIST

# Create user
redis-cli ACL SETUSER appuser on >apppass ~app:* +get +set +hset +hget

# Get user details
redis-cli ACL GETUSER appuser
```
"""
    ),
    (
        "redis-maxmemory-policy-invalid",
        "Redis Maxmemory Policy Invalid Error",
        "How to fix Redis invalid maxmemory-policy configuration errors",
        """## Causes

- Policy name misspelled
- Using volatile-* policy with no keys having TTL
- Policy not compatible with Redis version

## Fix

Check valid policies:

```bash
redis-cli CONFIG GET maxmemory-policy
```

Valid values:

```bash
noeviction       # return errors when memory limit reached
allkeys-lru      # evict any key using LRU
volatile-lru     # evict keys with TTL using LRU
allkeys-random   # evict random keys
volatile-random  # evict random keys with TTL
volatile-ttl     # evict keys with shortest TTL
allkeys-lfu      # evict least frequently used keys (Redis 4.0+)
volatile-lfu     # evict least frequently used keys with TTL (Redis 4.0+)
```

Set valid policy:

```bash
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

## Examples

```bash
# Check current policy
redis-cli CONFIG GET maxmemory-policy

# Set appropriate policy
redis-cli CONFIG SET maxmemory-policy volatile-lru

# Set TTL on keys for volatile policies
redis-cli EXPIRE mykey 3600
```
"""
    ),
    (
        "redis-config-file-not-found",
        "Redis Config File Not Found Error",
        "How to fix Redis configuration file not found errors",
        """## Causes

- Redis config file deleted or moved
- Wrong path specified in systemd unit
- Docker container missing config file

## Fix

Locate config file:

```bash
find /etc -name "redis.conf" 2>/dev/null
```

Create default config:

```bash
sudo cp /etc/redis/redis.conf.bak /etc/redis/redis.conf
```

Start Redis with specific config:

```bash
redis-server /path/to/redis.conf
```

Check systemd unit:

```bash
cat /etc/systemd/system/redis.service | grep ExecStart
```

## Examples

```bash
# Find Redis config
find / -name "redis.conf" 2>/dev/null

# Check Redis startup command
systemctl cat redis

# Start with custom config
redis-server /etc/redis/redis.conf
```
"""
    ),
    (
        "redis-tcp-backlog-error",
        "Redis TCP Backlog Error",
        "How to fix Redis TCP backlog overflow errors",
        """## Causes

- TCP backlog queue full during connection spikes
- Operating system tcp backlog limit exceeded
- High connection rate overwhelming backlog

## Fix

Check current backlog:

```bash
redis-cli CONFIG GET tcp-backlog
```

Increase TCP backlog:

```bash
redis-cli CONFIG SET tcp-backlog 1024
```

Make permanent in redis.conf:

```bash
sudo sed -i 's/^tcp-backlog 511/tcp-backlog 2048/' /etc/redis/redis.conf
```

Check system limits:

```bash
sysctl net.core.somaxconn
```

Increase system backlog:

```bash
sudo sysctl net.core.somaxconn=4096
```

## Examples

```bash
# Check TCP backlog
redis-cli CONFIG GET tcp-backlog

# Check system max connections
cat /proc/sys/net/core/somaxconn

# Monitor connection rate
redis-cli INFO clients | grep connected_clients
```
"""
    ),
    (
        "redis-hz-config-error",
        "Redis Hz Configuration Error",
        "How to fix Redis hz (server frequency) configuration errors",
        """## Causes

- hz value too low causing slow background tasks
- hz value too high causing CPU overhead
- Invalid hz value

## Fix

Check current hz:

```bash
redis-cli CONFIG GET hz
```

Set appropriate hz (default 10):

```bash
redis-cli CONFIG SET hz 10
```

For high-performance systems:

```bash
redis-cli CONFIG SET hz 50
```

Dynamic hz (Redis 7.0+):

```bash
redis-cli CONFIG SET dynamic-hz yes
```

## Examples

```bash
# Check hz
redis-cli CONFIG GET hz

# Set hz
redis-cli CONFIG SET hz 10

# Check if dynamic-hz is enabled
redis-cli CONFIG GET dynamic-hz
```
"""
    ),
    (
        "redis-maxmemory-samples-error",
        "Redis Maxmemory Samples Configuration Error",
        "How to fix Redis maxmemory-samples configuration for eviction policies",
        """## Causes

- maxmemory-samples too low causing poor eviction decisions
- maxmemory-samples too high causing CPU overhead
- Invalid sample count

## Fix

Check current setting:

```bash
redis-cli CONFIG GET maxmemory-samples
```

Set appropriate sample count:

```bash
# Default: 5 (good balance)
redis-cli CONFIG SET maxmemory-samples 5

# Higher accuracy (more CPU)
redis-cli CONFIG SET maxmemory-samples 10
```

Check eviction efficiency:

```bash
redis-cli INFO stats | grep evicted_keys
```

## Examples

```bash
# Check maxmemory-samples
redis-cli CONFIG GET maxmemory-samples

# Set samples for better eviction
redis-cli CONFIG SET maxmemory-samples 7

# Monitor eviction rate
watch -n 5 'redis-cli INFO stats | grep evicted_keys'
```
"""
    ),
    (
        "redis-list-max-ziplist-size",
        "Redis List Max Ziplist Size Error",
        "How to fix Redis list-max-ziplist-size configuration errors",
        """## Causes

- Value too large for ziplist encoding
- Incorrect ziplist size configuration
- Memory overhead from ziplist-to-listpack conversion

## Fix

Check current encoding:

```bash
redis-cli OBJECT ENCODING mylist
```

Adjust list-max-ziplist-size:

```bash
redis-cli CONFIG SET list-max-ziplist-size -2
```

Check listpack threshold:

```bash
redis-cli CONFIG GET list-max-ziplist-size
```

Monitor encoding changes:

```bash
redis-cli OBJECT ENCODING mylist
```

## Examples

```bash
# Check encoding
redis-cli OBJECT ENCODING mylist

# Set ziplist size
redis-cli CONFIG SET list-max-ziplist-size -2

# Check memory impact
redis-cli MEMORY USAGE mylist
```
"""
    ),
    (
        "redis-io-threads-error",
        "Redis IO Threads Configuration Error",
        "How to fix Redis io-threads configuration errors for multi-threaded I/O",
        """## Causes

- io-threads set higher than CPU cores
- io-threads-do-reads not enabled
- System not supporting multi-threaded I/O

## Fix

Check CPU cores:

```bash
nproc
```

Set io-threads:

```bash
redis-cli CONFIG SET io-threads 4
redis-cli CONFIG SET io-threads-do-reads yes
```

Check if multi-threading is active:

```bash
redis-cli INFO server | grep io_threads
```

## Examples

```bash
# Check CPU cores
nproc

# Set io-threads
redis-cli CONFIG SET io-threads 4

# Verify settings
redis-cli CONFIG GET io-threads
redis-cli CONFIG GET io-threads-do-reads
```
"""
    ),
    (
        "redis-active-defrag-error",
        "Redis Active Defrag Configuration Error",
        "How to fix Redis active defragmentation configuration errors",
        """## Causes

- activedefrag enabled without sufficient CPU
- Active defrag thresholds not set properly
- Memory fragmentation ratio incorrect

## Fix

Check defrag settings:

```bash
redis-cli CONFIG GET activedefrag
redis-cli CONFIG GET active-defrag-enabled
```

Configure defrag thresholds:

```bash
redis-cli CONFIG SET active-defrag-threshold-lower 10
redis-cli CONFIG SET active-defrag-threshold-upper 100
redis-cli CONFIG SET active-defrag-cycle-min 1
redis-cli CONFIG SET active-defrag-cycle-max 25
```

Enable active defrag:

```bash
redis-cli CONFIG SET activedefrag yes
```

## Examples

```bash
# Check fragmentation
redis-cli INFO memory | grep mem_fragmentation_ratio

# Check defrag status
redis-cli INFO stats | grep active_defrag

# Configure defrag
redis-cli CONFIG SET activedefrag yes
```
"""
    ),
    (
        "redis-latency-tracking-error",
        "Redis Latency Tracking Configuration Error",
        "How to fix Redis latency tracking and percentile calculation errors",
        """## Causes

- latency-tracking disabled
- Percentile list too large consuming memory
- Invalid percentile values

## Fix

Check latency tracking config:

```bash
redis-cli CONFIG GET latency-tracking
redis-cli CONFIG GET latency-tracking-info-percentiles
```

Enable latency tracking:

```bash
redis-cli CONFIG SET latency-tracking yes
```

Set percentile list:

```bash
redis-cli CONFIG SET latency-tracking-info-percentiles "50 99 99.9"
```

View latency data:

```bash
redis-cli LATENCY LATEST
redis-cli LATENCY HISTORY command
```

## Examples

```bash
# Check latency
redis-cli LATENCY LATEST

# Set percentiles
redis-cli CONFIG SET latency-tracking-info-percentiles "50 95 99"

# Reset latency data
redis-cli LATENCY RESET
```
"""
    ),
    (
        "redis-lazyfree-error",
        "Redis Lazy Free Configuration Error",
        "How to fix Redis lazy free configuration errors for asynchronous key deletion",
        """## Causes

- Lazy free not enabled causing blocking deletes
- DEL on large keys blocking server
- Memory not reclaimed after deletion

## Fix

Check lazy free settings:

```bash
redis-cli CONFIG GET lazyfree-lazy-expire
redis-cli CONFIG SET lazyfree-lazy-expire yes
redis-cli CONFIG SET lazyfree-lazy-server-del yes
redis-cli CONFIG SET lazyfree-lazy-user-del yes
```

Use UNLINK instead of DEL:

```bash
redis-cli UNLINK mykey
```

Enable lazy free for all operations:

```bash
redis-cli CONFIG SET lazyfree-lazy-expire yes
redis-cli CONFIG SET lazyfree-lazy-server-del yes
redis-cli CONFIG SET lazyfree-lazy-user-flush yes
```

## Examples

```bash
# Check lazy free settings
redis-cli CONFIG GET lazyfree-*

# Use UNLINK
redis-cli UNLINK largekey

# Monitor memory after delete
redis-cli INFO memory | grep used_memory_human
```
"""
    ),
    (
        "redis-list-compress-depth-error",
        "Redis List Compress Depth Configuration Error",
        "How to fix Redis list-compress-depth configuration errors",
        """## Causes

- Compress depth set too high causing memory overhead
- Compression failing for certain data types
- Invalid compress depth value

## Fix

Check compress depth:

```bash
redis-cli CONFIG GET list-compress-depth
```

Set appropriate value:

```bash
# 0: disable compression (default)
redis-cli CONFIG SET list-compress-depth 0

# 1: compress all nodes except head and tail
redis-cli CONFIG SET list-compress-depth 1
```

Check encoding:

```bash
redis-cli OBJECT ENCODING mylist
```

## Examples

```bash
# Check compress depth
redis-cli CONFIG GET list-compress-depth

# Set compress depth
redis-cli CONFIG SET list-compress-depth 2

# Check encoding
redis-cli OBJECT ENCODING mylist
```
"""
    ),
    (
        "redis-oom-score-adj-error",
        "Redis OOM Score Adjust Configuration Error",
        "How to fix Redis oom-score-adj configuration for Linux OOM killer behavior",
        """## Causes

- oom-score-adj set too low causing Redis to be killed first
- oom-score-adj value out of range (-1000 to 1000)
- OOM killer targeting Redis in memory pressure

## Fix

Check oom-score-adj:

```bash
redis-cli CONFIG GET oom-score-adj
```

Set lower oom-score-adj (less likely to be killed):

```bash
redis-cli CONFIG SET oom-score-adj -500
```

Check Redis OOM score:

```bash
cat /proc/$(pidof redis-server)/oom_score
```

## Examples

```bash
# Check OOM score
cat /proc/$(pidof redis-server)/oom_score

# Set oom-score-adj
redis-cli CONFIG SET oom-score-adj -500

# Check OOM adj
cat /proc/$(pidof redis-server)/oom_score_adj
```
"""
    ),
    (
        "redis-close-files-after-write-error",
        "Redis Close Files After Write Error",
        "How to fix Redis close-files-after configuration issues",
        """## Causes

- File descriptors not being closed after writes
- File descriptor leak
- Too many open files

## Fix

Check open files:

```bash
ls /proc/$(pidof redis-server)/fd | wc -l
```

Set close-files-after-write:

```bash
redis-cli CONFIG SET close-files-after-write yes
```

Check file descriptor limits:

```bash
cat /proc/$(pidof redis-server)/limits | grep "open files"
```

Increase FD limit:

```bash
ulimit -n 65535
```

## Examples

```bash
# Check open FDs
ls /proc/$(pidof redis-server)/fd | wc -l

# Check FD limit
ulimit -n

# Monitor file descriptors
watch -n 5 'ls /proc/$(pidof redis-server)/fd | wc -l'
```
"""
    ),
    (
        "redis-syslog-enabled-error",
        "Redis Syslog Enabled Error",
        "How to fix Redis syslog configuration errors",
        """## Causes

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
"""
    ),
    (
        "redis-setproctitle-error",
        "Redis Set Proctitle Configuration Error",
        "How to fix Redis setproctitle configuration issues",
        """## Causes

- Invalid proctitle format
- Proctitle contains unsupported characters
- setproctitle not supported on platform

## Fix

Check setproctitle:

```bash
redis-cli CONFIG GET setproctitle
```

Set proctitle:

```bash
redis-cli CONFIG SET setproctitle "redis-server"
```

Check process title:

```bash
ps aux | grep redis
```

## Examples

```bash
# Check process title
ps aux | grep redis-server

# Set proctitle
redis-cli CONFIG SET setproctitle "redis-custom"

# Verify
ps aux | grep redis
```
"""
    ),
]

count = 0
skipped = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    content = make_page(title, desc, body)
    path = os.path.join(BASE, f"{slug}.md")
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {skipped}")
print(f"Total pages in PAGES list: {len(PAGES)}")
print(f"Previously existing: {len(EXISTING)}")
print(f"New total in directory: {len(EXISTING) + count}")
