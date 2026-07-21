---
title: "Maven Exclusion Filter Error"
description: "Maven dependency exclusion filters are misconfigured, causing required dependencies to be excluded or unwanted artifacts to be included."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Exclusion Filter Error

Maven dependency exclusions allow you to remove transitive dependencies. An exclusion filter error occurs when the exclusion pattern does not match as intended, excluding too much or too little.

## Common Causes

- The exclusion groupId or artifactId pattern does not match the target
- Wildcard exclusions remove dependencies that are actually needed
- The exclusion is placed on the wrong dependency declaration
- Exclusions use incorrect artifact coordinates

## How to Fix

1. Verify the exclusion coordinates match the transitive dependency:

```xml
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-core</artifactId>
  <version>6.1.3</version>
  <exclusions>
    <exclusion>
      <groupId>commons-logging</groupId>
      <artifactId>commons-logging</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

2. Use the dependency tree to find the exact coordinates:

```bash
mvn dependency:tree -Dincludes=commons-logging
```

3. Check if the exclusion is accidentally removing a required dependency:

```bash
mvn dependency:tree -Dverbose
```

4. Use pattern-based exclusions carefully:

```xml
<exclusion>
  <groupId>org.unwanted</groupId>
  <artifactId>*</artifactId> <!-- excludes all artifacts from this group -->
</exclusion>
```

## Examples

```bash
# Find the dependency to exclude
mvn dependency:tree
# [INFO] +- org.springframework:spring-core:jar:6.1.3:compile
# [INFO]    \- commons-logging:commons-logging:jar:1.3.0:compile
```

```xml
<!-- Correct exclusion of transitive logging dependency -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
  <exclusions>
    <exclusion>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-logging</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependency artifacts
- [Transitive Dependency Conflict]({{< relref "/tools/maven/maven-dependency-resolution-failed" >}}) -- dependency resolution failures
