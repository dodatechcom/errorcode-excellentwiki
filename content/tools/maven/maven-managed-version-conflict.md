---
title: "Maven Managed Version Conflict"
description: "Maven dependency management declares conflicting versions for the same artifact, causing unpredictable resolution behavior."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Managed Version Conflict

Maven uses nearest-definition-wins strategy for dependency version conflicts. A managed version conflict occurs when multiple BOMs or dependency management blocks declare different versions for the same artifact.

## Common Causes

- Multiple BOM imports declare different versions of the same artifact
- A parent POM and a BOM both manage the same dependency
- Dependency management in an imported BOM overrides a local declaration
- The `<dependencyManagement>` section is ordered incorrectly

## How to Fix

1. Analyze the dependency tree to see which version wins:

```bash
mvn dependency:tree -Dverbose -Dincludes=com.google.guava
```

2. Override the managed version explicitly:

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.google.guava</groupId>
      <artifactId>guava</artifactId>
      <version>32.1.3-jre</version>
    </dependency>
  </dependencies>
</dependencyManagement>
```

3. Check BOM ordering for import conflicts:

```xml
<dependencyManagement>
  <dependencies>
    <!-- BOMs are evaluated in order; later ones override earlier -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-dependencies</artifactId>
      <version>3.2.2</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

4. Exclude the unwanted version:

```xml
<dependency>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <version>32.1.3-jre</version>
  <exclusions>
    <exclusion>
      <groupId>com.google.guava</groupId>
      <artifactId>failureaccess</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

## Examples

```bash
# Dependency tree showing conflict
[INFO] com.example:my-app:jar:1.0-SNAPSHOT
[INFO] +- com.google.guava:guava:jar:32.1.3-jre:compile
[INFO] |  \- com.google.guava:failureaccess:jar:1.0.1:compile (managed)
```

```xml
<!-- Explicit version override in dependencyManagement -->
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>com.google.guava</groupId>
      <artifactId>guava</artifactId>
      <version>32.1.3-jre</version>
    </dependency>
  </dependencies>
</dependencyManagement>
```

## Related Errors

- [Dependency Resolution Failed]({{< relref "/tools/maven/maven-dependency-resolution-failed" >}}) -- resolution failures
- [Dependency Management Version]({{< relref "/tools/maven/maven-dependency-management-version" >}}) -- version management issues
