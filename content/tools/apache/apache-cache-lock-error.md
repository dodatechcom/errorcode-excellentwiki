---
title: "[Solution] Apache Cache Lock Error"
description: "Fix Apache cache lock errors when mod_cache cannot acquire the lock for cached content."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache Cache Lock Error

Apache mod_cache fails to acquire a lock for caching an origin resource.

```
AH00769: cache: error locking URL /path/to/resource
```

## Common Causes

- Another request is already fetching the same resource
- Lock file directory permissions wrong
- Cache lock timeout too short
- Shared memory segment not writable
- Cache disk storage not properly initialized

## How to Fix

### Configure Cache Lock

```apache
# Enable cache locking to prevent thundering herd
CacheLock on
CacheLockPath /tmp/mod_cache_locks
CacheLockMaxAge 5
CacheLockTimeout 30
```

### Fix Lock Directory Permissions

```bash
# Ensure Apache can write to lock directory
mkdir -p /tmp/mod_cache_locks
chown www-data:www-data /tmp/mod_cache_locks
chmod 755 /tmp/mod_cache_locks
```

### Adjust Cache Settings

```apache
<IfModule mod_cache.c>
    CacheRoot /var/cache/apache2/
    CacheDirLevels 2
    CacheDirLength 1
    CacheDefaultExpire 3600
    CacheLock on
    CacheLockPath /tmp/mod_cache_locks
    CacheLockMaxAge 5
</IfModule>
```

### Disable Cache for Specific Locations

```apache
<Directory "/var/www/dynamic">
    CacheDisable on
</Directory>
```

## Examples

```apache
# Full cache configuration with locking
<IfModule mod_cache.c>
    <IfModule mod_cache_disk.c>
        CacheRoot /var/cache/apache2/
        CacheDirLevels 2
        CacheDirLength 1
        CacheMaxFileSize 1000000
        CacheMinFileSize 1
    </IfModule>
    CacheLock on
    CacheLockPath /tmp/mod_cache_locks
    CacheIgnoreNoLastMod on
    CacheIgnoreCacheControl on
</IfModule>
```
