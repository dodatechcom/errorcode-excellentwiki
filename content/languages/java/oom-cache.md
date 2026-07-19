---
title: "[Solution] Java OutOfMemoryError — caches like HashMap or Guava that grow without eviction"
description: "Fix Java OutOfMemoryError when caches like hashmap or guava that grow without eviction with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# OutOfMemoryError — caches like HashMap or Guava that grow without eviction

A `OutOfMemoryError` occurs when Map<String,Object> cache = new HashMap<>();
public void cache(String k, Object v) { cache.put(k,v); }  // never evicts.

## Common Causes

```java
Map<String,Object> cache = new HashMap<>();
public void cache(String k, Object v) { cache.put(k,v); }  // never evicts
```

## Solutions

```java
// Fix: bounded cache
Cache<String,Object> cache = CacheBuilder.newBuilder()
    .maximumSize(10_000)
    .expireAfterWrite(30, TimeUnit.MINUTES)
    .build();

// Fix: Caffeine
Cache<String,Object> cache = Caffeine.newBuilder()
    .maximumSize(10_000)
    .expireAfterWrite(Duration.ofMinutes(30))
    .recordStats().build();

// Fix: clean ThreadLocal
try { byte[] buf = BUFFER.get(); }
finally { BUFFER.remove(); }
```

## Prevention Checklist

- Set maximum size for caches.
- Use time-based expiration.
- Monitor cache hit rates.
- Clean ThreadLocal in finally blocks.

## Related Errors

OutOfMemoryError, GC Overhead
