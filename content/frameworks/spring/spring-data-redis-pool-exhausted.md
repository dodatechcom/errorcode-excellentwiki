---
title: "Spring Data Redis Connection Pool Exhausted"
description: "Spring Data Redis lettuce connection pool runs out of available connections causing requests to block or timeout waiting for a free connection"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when the Spring Data Redis Lettuce or Jedis connection pool cannot provide a connection within the configured timeout because all connections are in use.

## Common Causes

- Connection pool max-active is too low for the application's request volume
- Redis operations are not properly releasing connections back to the pool
- Long-running Redis pipelines or transactions holding connections unnecessarily
- Network latency between the application and Redis server causes slow connection recycling
- Redis server has maxclients set too low and rejects new connections
- Connection pool eviction settings are misconfigured causing stale connections

## How to Fix

1. Increase the connection pool size in your configuration:

```yaml
# application.yml
spring:
  data:
    redis:
      lettuce:
        pool:
          max-active: 16
          max-idle: 8
          min-idle: 2
          max-wait: 2000
      timeout: 5000
```

2. Configure pool eviction to remove stale connections:

```java
@Configuration
public class RedisConfig {
    @Bean
    public LettuceConnectionFactory connectionFactory() {
        GenericObjectPoolConfig<?> poolConfig = new GenericObjectPoolConfig<>();
        poolConfig.setMaxTotal(16);
        poolConfig.setMaxIdle(8);
        poolConfig.setMinIdle(2);
        poolConfig.setMaxWait(Duration.ofMillis(2000));
        poolConfig.setTimeBetweenEvictionRuns(Duration.ofSeconds(30));
        poolConfig.setMinEvictableIdleTime(Duration.ofSeconds(60));

        LettuceClientConfiguration clientConfig = LettuceClientConfiguration.builder()
            .commandTimeout(Duration.ofSeconds(5))
            .build();

        RedisStandaloneConfiguration serverConfig = new RedisStandaloneConfiguration();
        return new LettuceConnectionFactory(serverConfig,
            ClientOptions.builder().build());
    }
}
```

3. Ensure Redis operations properly close resources:

```java
@Service
public class CacheService {
    private final StringRedisTemplate redisTemplate;

    public CacheService(StringRedisTemplate redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    public String getValue(String key) {
        // Use execute with a callback to ensure proper connection release
        return redisTemplate.execute((RedisCallback<String>) connection -> {
            byte[] value = connection.get(key.getBytes());
            return value != null ? new String(value) : null;
        });
    }
}
```

## Examples

```java
// Common mistake: using connection pool operations in a tight loop
@Service
public class BulkService {
    @Autowired
    private StringRedisTemplate redis;

    public void processItems(List<String> items) {
        for (String item : items) {
            // Each iteration acquires and releases a connection
            // Under high volume this exhausts the pool
            redis.opsForValue().set(item, "processed");
        }
    }
}
```

```text
io.lettuce.core.RedisConnectionTimeoutException:
    Connection pool exhausted -- no available connections
    Pool state: active=16, idle=0, waiters=5
```

## Prevention

1. Monitor Redis connection pool metrics using Micrometer or Spring Boot Actuator
2. Use Redis pipelines for bulk operations to reduce connection acquisition overhead
3. Set connection pool max-wait to a reasonable timeout instead of blocking indefinitely
4. Configure Redis server maxclients higher than the application pool max-active
