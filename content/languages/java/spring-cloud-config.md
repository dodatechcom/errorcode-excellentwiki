---
title: "[Solution] ConfigDataException — Spring Cloud Config Fix"
description: "Fix ConfigDataException when Spring Cloud Config cannot load configuration. Check config server connectivity and property sources."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring-cloud", "config", "configuration", "config-data", "property-source"]
weight: 5
---

# ConfigDataException — Spring Cloud Config Fix

A `ConfigDataException` is thrown when Spring Boot cannot load configuration from a ConfigDataLocationResolver or ConfigDataLoader. This is part of the Spring Boot 2.4+ configuration system.

## What This Error Means

Common messages:

- `ConfigDataException: Could not find property source from config data resource`
- `ConfigDataLocationNotFoundException: No config data location found`

## Common Causes

```properties
# Cause 1: Config server unreachable
spring.config.import=configserver:http://config-server:8888

# Cause 2: Application name not set
# spring.application.name not configured

# Cause 3: Config server returns 404
# Application profile not found on config server
```

## How to Fix

### Fix 1: Configure fallback

```properties
spring.config.import=optional:configserver:http://config-server:8888
# optional: prefix prevents startup failure if server is unavailable
```

### Fix 2: Set application name

```yaml
spring:
  application:
    name: my-service
  profiles:
    active: dev
  config:
    import: configserver:http://config-server:8888
```

### Fix 3: Add retry mechanism

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-config</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.retry</groupId>
    <artifactId>spring-retry</artifactId>
</dependency>
```

## Related Errors

- {{< relref "spring-cloud-gateway" >}} — ResponseStatusException: 502
- {{< relref "spring-bean" >}} — NoSuchBeanDefinitionException
- {{< relref "connection-timeout" >}} — Connection timeout
