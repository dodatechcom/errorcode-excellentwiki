---
title: "[Solution] Spring Cache Name Error"
description: "Fix Spring cache name errors when cache operations target wrong or non-existent cache instances."
frameworks: ["spring"]
error-types: ["cache-error"]
severities: ["error"]
---

Cache name errors occur when different cache annotations use different cache names, causing data to be cached in separate cache instances.

## Common Causes

- Cache name mismatch between `@Cacheable` and `@CacheEvict`
- Typo in cache name string
- Cache manager does not create caches on demand
- Different method uses different cache name
- Cache names not configured in cache manager

## How to Fix

### Use Consistent Cache Names

```java
@Service
public class UserService {
    // All operations on "users" cache
    @Cacheable(value = "users", key = "#id")
    public User getUser(Long id) { ... }

    @CacheEvict(value = "users", key = "#id")
    public void updateUser(Long id) { ... }

    @CachePut(value = "users", key = "#id")
    public User refreshUser(Long id) { ... }
}
```

### Define Cache Names in Configuration

```java
@Configuration
@EnableCaching
public class CacheConfig {
    @Bean
    public CacheManager cacheManager() {
        SimpleCacheManager cacheManager = new SimpleCacheManager();
        cacheManager.setCaches(List.of(
            new ConcurrentMapCache("users"),
            new ConcurrentMapCache("products"),
            new ConcurrentMapCache("orders")
        ));
        return cacheManager;
    }
}
```

### Use Constants for Cache Names

```java
public class CacheNames {
    public static final String USERS = "users";
    public static final String PRODUCTS = "products";
    public static final String ORDERS = "orders";
}

@Service
public class UserService {
    @Cacheable(CacheNames.USERS)
    public User getUser(Long id) { ... }

    @CacheEvict(CacheNames.USERS)
    public void updateUser(Long id) { ... }
}
```

## Examples

```java
// Bug -- different cache names
@Cacheable("users")
public User getUser(Long id) { ... }

@CacheEvict("user")  // Typo -- different cache name!
public void updateUser(Long id) { ... }

// Fix -- use same name
@Cacheable("users")
public User getUser(Long id) { ... }

@CacheEvict("users")
public void updateUser(Long id) { ... }
```
