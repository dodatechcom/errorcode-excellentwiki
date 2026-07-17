---
title: "CacheAccessException - Spring Cache"
description: "Spring throws CacheAccessException when a cache operation fails"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["cache", "spring-cache", "redis", "caffeine", "eviction"]
weight: 5
---

This error occurs when Spring's caching abstraction encounters a failure while reading from or writing to the configured cache provider. It throws `CacheAccessException`.

## Common Causes

- Cache provider (Redis, Caffeine, EHCache) is unavailable
- Cache serialization/deserialization error
- Cache eviction due to memory limits
- Cache key exceeds maximum allowed size
- Connection pool exhaustion for distributed caches

## How to Fix

1. Configure cache with error handling:

```java
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public CacheManager cacheManager() {
        RedisCacheManager manager = RedisCacheManager.builder(redisConnectionFactory())
            .cacheDefaults(RedisCacheConfiguration.defaultCacheConfig()
                .entryTtl(Duration.ofMinutes(30))
                .serializeValuesWith(
                    RedisSerializationContext.SerializationPair
                        .fromSerializer(new GenericJackson2JsonRedisSerializer())
                ))
            .build();
        manager.setTransactionAware(true);
        return manager;
    }
}
```

2. Use `@Cacheable` with fallback handling:

```java
@Service
public class ProductService {

    @Cacheable(value = "products", key = "#id", unless = "#result == null")
    public Product getProduct(Long id) {
        try {
            return productRepository.findById(id).orElse(null);
        } catch (Exception e) {
            log.warn("Cache lookup failed, falling back to DB: {}", e.getMessage());
            return productRepository.findById(id).orElse(null);
        }
    }
}
```

3. Add `CacheErrorHandler`:

```java
@Bean
public CacheErrorHandler errorHandler() {
    return new SimpleCacheErrorHandler() {
        @Override
        public void handleCacheGetError(RuntimeException e, Cache cache, Object key) {
            log.warn("Cache GET error for key {}: {}", key, e.getMessage());
        }
    };
}
```

## Examples

```java
@Cacheable("products")
public Product getProduct(Long id) { ... }
// CacheAccessException: Redis connection refused
```

## Related Errors

- [Elasticsearch error]({{< relref "/frameworks/spring/spring-data-elasticsearch-error" >}})
- [AMQP error]({{< relref "/frameworks/spring/spring-amqp-error" >}})
