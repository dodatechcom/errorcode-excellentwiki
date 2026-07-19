---
title: "[Solution] Hibernate CacheException — Unknown Cache Region"
description: "Fix org.hibernate.CacheException Unknown cache region. Configure and resolve Hibernate second-level cache errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# CacheException — Unknown Cache Region (Second-Level Cache Miss)

A `CacheException` with message `net.sf.ehcache.CacheException: Unknown cache region` occurs when Hibernate references a cache region that has not been configured in the second-level cache provider (e.g., Ehcache, Hazelcast, or Infinispan). The entity or query is mapped to use caching, but the cache region definition is missing.

## What This Error Means

Hibernate's second-level cache stores entity data and query results across sessions. When an entity or query references a named cache region (e.g., `@Cache(region = "users")`), that region must be defined in the cache provider configuration. If it is not, Hibernate throws this exception.

## Common Causes

```java
// Cause 1: Entity references non-existent cache region
@Entity
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE, region = "userCache")
public class User {
    @Id
    private Long id;
}
// "userCache" region not defined in ehcache.xml

// Cause 2: Query cache referencing undefined region
@QueryHints({@QueryHint(name = "org.hibernate.cacheable", value = "true"),
             @QueryHint(name = "org.hibernate.cache.region", value = "queryResults")})
@Query("SELECT u FROM User u WHERE u.active = true")
List<User> findActiveUsers();
// "queryResults" region not defined

// Cause 3: ehcache.xml missing region definition
// Entity has @Cache(region = "orders") but ehcache.xml has no "orders" entry
```

## How to Fix

### Fix 1: Define cache regions in ehcache.xml

```xml
<ehcache>
    <cache name="com.example.entity.User"
           maxEntriesLocalHeap="10000"
           timeToLiveSeconds="3600"
           memoryStoreEvictionPolicy="LRU"/>

    <cache name="com.example.entity.Order"
           maxEntriesLocalHeap="5000"
           timeToLiveSeconds="1800"
           memoryStoreEvictionPolicy="LRU"/>

    <cache name="query.activeUsers"
           maxEntriesLocalHeap="1000"
           timeToLiveSeconds="600"
           memoryStoreEvictionPolicy="LRU"/>
</ehcache>
```

### Fix 2: Use Hibernate's built-in cache region names

```java
// Don't specify custom region — use entity's fully qualified name
@Entity
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
public class User {
    @Id
    private Long id;
}
// Hibernate will use "com.example.entity.User" as the region name
// Define this region in ehcache.xml
```

### Fix 3: Use Hibernate 6+ JCache (JSR-107) configuration

```properties
# application.properties
spring.jpa.properties.hibernate.cache.use_second_level_cache=true
spring.jpa.properties.hibernate.cache.region.factory_class=org.hibernate.cache.jcache.JCacheRegionFactory
spring.jpa.properties.hibernate.javax.cache.provider=org.ehcache.jsr107.EhcacheCachingProvider
spring.jpa.properties.hibernate.cache.use_query_cache=true
```

### Fix 4: Add wildcard cache configuration

```xml
<ehcache>
    <!-- Default cache for all entities -->
    <cache name="com.example.entity.*"
           maxEntriesLocalHeap="5000"
           timeToLiveSeconds="1800"/>

    <!-- Specific overrides -->
    <cache name="com.example.entity.User"
           maxEntriesLocalHeap="10000"
           timeToLiveSeconds="3600"/>
</ehcache>
```

### Fix 5: Validate cache regions at startup

```java
@PostConstruct
public void validateCacheRegions() {
    try {
        CacheManager cacheManager = CacheManager.getInstance();
        String[] cacheNames = cacheManager.getCacheNames();
        log.info("Configured cache regions: {}", Arrays.toString(cacheNames));
    } catch (Exception e) {
        log.warn("Could not validate cache regions", e);
    }
}
```

## Prevention Tips

- Always define cache regions in ehcache.xml before referencing them in entity annotations.
- Use fully qualified entity class names as cache region names by default.
- Test caching configuration in integration tests.
- Monitor cache hit/miss ratios in production to ensure caching is effective.
- Consider using Hibernate 6+ JCache for standardized cache configuration.

## Related Errors

- {{< relref "hibernate-unknown-entity" >}} — Unknown entity mapping
- {{< relref "hibernate-type-error" >}} — Type mapping errors
- {{< relref "hibernate-dialect" >}} — Dialect configuration errors
