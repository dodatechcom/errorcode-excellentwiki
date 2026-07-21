---
title: "Maven Spring Boot DevTools Error"
description: "Maven build fails or restarts unexpectedly because Spring Boot DevTools interferes with the build classloader during packaging."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Spring Boot DevTools Error

Spring Boot DevTools uses a special classloader for automatic restarts. A build error occurs when DevTools is included in the packaged artifact instead of being scoped to development only.

## Common Causes

- DevTools dependency is declared without the `runtime` or `optional` scope
- The DevTools module is included in the final fat JAR
- DevTools interferes with the Maven compiler during incremental builds
- The `restart.exclude` configuration conflicts with the build

## How to Fix

1. Scope DevTools to runtime only:

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-devtools</artifactId>
  <scope>runtime</scope>
  <optional>true</optional>
</dependency>
```

2. Configure the Maven plugin to exclude DevTools:

```xml
<plugin>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-maven-plugin</artifactId>
  <configuration>
    <excludeDevtools>true</excludeDevtools>
  </configuration>
</plugin>
```

3. Use profiles to separate dev and production builds:

```xml
<profiles>
  <profile>
    <id>dev</id>
    <dependencies>
      <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
      </dependency>
    </dependencies>
  </profile>
</profiles>
```

4. Verify DevTools is not in the final JAR:

```bash
jar tf target/my-app.jar | grep devtools
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal repackage
  DevTools detected -- it is not included in the packaged application
```

```xml
<!-- Correct DevTools configuration -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-devtools</artifactId>
  <scope>runtime</scope>
  <optional>true</optional>
</dependency>
```

## Related Errors

- [Spring Boot Error]({{< relref "/tools/maven/maven-spring-boot-error" >}}) -- Spring Boot build issues
- [Spring Boot Maven Error]({{< relref "/tools/maven/maven-spring-boot-maven-error" >}}) -- Spring Boot Maven plugin
