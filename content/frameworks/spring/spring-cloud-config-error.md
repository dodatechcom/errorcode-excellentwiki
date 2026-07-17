---
title: "ConfigDataException - config import failed"
description: "Spring throws ConfigDataException when it fails to load or import externalized configuration"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring Boot's configuration system fails to import or resolve externalized configuration files. It throws `ConfigDataMissingPropertySourceException` or `ConfigDataLocationNotFoundException`.

## Common Causes

- Referenced config server is unreachable
- Config file path in `spring.config.import` is incorrect
- Missing `spring-cloud-config-client` dependency
- Encrypted properties fail to decrypt
- YAML/properties file has syntax errors

## How to Fix

1. Verify the config import location:

```yaml
# application.yml
spring:
  config:
    import:
      - optional:configserver:http://config-server:8888
      - classpath:additional-config.yml
```

2. Use `optional:` prefix to prevent startup failure:

```yaml
spring:
  config:
    import:
      - optional:configserver:http://config-server:8888
```

3. Add fallback configuration:

```java
@Configuration
@PropertySource("classpath:default-properties.properties")
public class ConfigFallback { }
```

## Examples

```yaml
# Config server unreachable
spring:
  config:
    import: configserver:http://config-server:8888
# ConfigDataException: Cannot load config data from 'configserver:http://config-server:8888'
```

## Related Errors

- [Gateway error]({{< relref "/frameworks/spring/cloud-gateway-error" >}})
- [Kafka concurrency error]({{< relref "/frameworks/spring/kafka-concurrency-error" >}})
