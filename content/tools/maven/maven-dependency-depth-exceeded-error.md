---
title: "Maven Dependency Depth Exceeded Error"
description: "Maven enforcer plugin rejects the build because the dependency tree depth exceeds the configured maximum allowed depth."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Dependency Depth Exceeded Error

Maven enforcer rules can limit dependency tree depth to prevent complex dependency chains. An error occurs when a transitive dependency path exceeds the configured threshold.

## Common Causes

- The enforcer plugin has a `maxDepth` rule configured too restrictively
- A deeply nested transitive dependency chain triggers the rule
- A dependency引入了 many levels of transitive dependencies
- The rule is inherited from a parent POM with strict settings

## How to Fix

1. Check the current enforcer configuration:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-enforcer-plugin</artifactId>
  <configuration>
    <rules>
      <banDuplicatePomDependencyVersions/>
    </rules>
  </configuration>
</plugin>
```

2. Increase the depth limit or remove it:

```xml
<rules>
  <dependencyDepth>
    <maxDepth>10</maxDepth>
  </dependencyDepth>
</rules>
```

3. Analyze the deep dependency chain:

```bash
mvn dependency:tree -Dverbose | grep -c "+-\|\\-"
```

4. Exclude the deep transitive dependency:

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>deep-dep</artifactId>
  <exclusions>
    <exclusion>
      <groupId>com.example</groupId>
      <artifactId>very-deep-nested-dep</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

## Examples

```bash
# Error output
[ERROR] Rule 0: org.apache.maven.plugins.enforcer.BanDuplicatePomDependencyVersions failed
  Dependency tree depth exceeds maximum: 12 > 8
```

```xml
<!-- Enforcer plugin with depth configuration -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-enforcer-plugin</artifactId>
  <executions>
    <execution>
      <id>enforce-depth</id>
      <phase>validate</phase>
      <goals><goal>enforce</goal></goals>
      <configuration>
        <rules>
          <requireReleaseVersion/>
          <banDuplicatePomDependencyVersions/>
        </rules>
      </configuration>
    </execution>
  </executions>
</plugin>
```

## Related Errors

- [Enforcer Error]({{< relref "/tools/maven/maven-enforcer-error" >}}) -- enforcer plugin issues
- [Transitive Dependency Conflict]({{< relref "/tools/maven/maven-transitive-dependency-conflict" >}}) -- dependency conflicts
