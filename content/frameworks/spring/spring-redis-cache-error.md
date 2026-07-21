---
title: "[Solution] Spring Redis Cache Error"
description: "Fix Spring Redis cache errors when cached data is stale, missing, or Redis connection fails."
frameworks: ["spring"]
error-types: ["cache-error"]
severities: ["error"]
---

Redis cache errors in Spring occur when the cache backend is unavailable, serialized data is corrupted, or cache configuration is incorrect.

## Common Causes

- Redis server not running or unreachable
- Cache key collision between different data types
- Serialization format mismatch between cache operations
- Cache TTL not configured, causing stale data
- Connection pool exhausted under high load

## How to Fix

### Configure Redis Cache

```java
@Configuration
@EnableCaching
public class CacheConfig {
    @Bean
    public RedisCacheManager cacheManager(RedisConnectionFactory factory) {
        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofMinutes(30))
            .serializeValuesWith(
                RedisSerializationContext.SerializationPair.fromSerializer(
                    new GenericJackson2JsonRedisSerializer()
                )
            );
        return RedisCacheManager.builder(factory)
            .cacheDefaults(config)
            .build();
    }
}
```

### Use Cache Annotations

```java
@Service
public class UserService {
    @Cacheable(value = "users", key = "#userId")
    public User getUser(Long userId) {
        return userRepository.findById(userId).orElse(null);
    }

    @CacheEvict(value = "users", key = "#userId")
    public void updateUser(Long userId, UserDto dto) {
        // Update user
    }

    @CachePut(value = "users", key = "#userId")
    public User updateUserAndCache(Long userId, UserDto dto) {
        // Update and return new user
    }
}
```

### Handle Cache Failures

```java
@Configuration
public class CacheErrorHandlerConfig {
    @Bean
    public CacheErrorHandler errorHandler() {
        return new SimpleCacheErrorHandler() {
            @Override
            public void handleCacheGetError(RuntimeException e, Cache cache, Object key) {
                log.warn("Cache get failed for key {}: {}", key, e.getMessage());
            }
        };
    }
}
```

## Examples

```java
@Service
public class ProductService {
    @Cacheable(value = "products", key = "#id")
    public Product getProduct(Long id) {
        // Called only if cache miss
        return productRepository.findById(id).orElse(null);
    }

    // Bug -- no cache eviction
    public void updateProduct(Long id, ProductDto dto) {
        productRepository.save(dto.toEntity(id));
        // Cache still has old data
    }

    // Fix -- evict cache on update
    @CacheEvict(value = "products", key = "#id")
    public void updateProductEvict(Long id, ProductDto dto) {
        productRepository.save(dto.toEntity(id));
    }
}
```
