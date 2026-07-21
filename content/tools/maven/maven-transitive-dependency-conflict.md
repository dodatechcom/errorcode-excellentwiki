---
title: "Maven Transitive Dependency Conflict"
description: "Maven build fails or behaves unexpectedly because two transitive dependencies provide the same classes with incompatible versions."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Transitive Dependency Conflict

Maven resolves transitive dependency conflicts using nearest-definition-wins. A conflict error occurs when two paths bring in different versions of the same library, causing classpath issues.

## Common Causes

- Two dependencies transitively depend on different versions of the same library
- The nearest version is older and missing required classes
- A framework requires a specific version of a shared dependency
- Excluding one version breaks another dependency

## How to Fix

1. Analyze the dependency tree for conflicts:

```bash
mvn dependency:tree -Dverbose -Dincludes=com.google.guava
```

2. Explicitly manage the version:

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

3. Use the enforcer plugin to detect conflicts:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-enforcer-plugin</artifactId>
  <version>3.4.1</version>
  <executions>
    <execution>
      <id>enforce</id>
      <goals>
        <goal>enforce</goal>
      </goals>
      <configuration>
        <rules>
          <dependencyConvergence/>
        </rules>
      </configuration>
    </execution>
  </executions>
</plugin>
```

4. Exclude the unwanted transitive dependency:

```xml
<dependency>
  <groupId>com.example</groupId>
  <artifactId>library-a</artifactId>
  <exclusions>
    <exclusion>
      <groupId>com.google.guava</groupId>
      <artifactId>guava</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

## Examples

```bash
# Dependency tree showing conflict
[INFO] com.example:my-app:jar:1.0-SNAPSHOT
[INFO] +- com.example:library-a:jar:1.0:compile
[INFO] |  \- com.google.guava:guava:jar:28.0-jre:compile
[INFO] +- com.example:library-b:jar:2.0:compile
[INFO]    \- com.google.guava:guava:jar:31.1-jre:compile
```

```xml
<!-- Enforcer plugin to fail on dependency conflicts -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-enforcer-plugin</artifactId>
  <executions>
    <execution>
      <id>enforce</id>
      <phase>validate</phase>
      <goals><goal>enforce</goal></goals>
      <configuration>
        <rules>
          <dependencyConvergence/>
        </rules>
      </configuration>
    </execution>
  </executions>
</plugin>
```

## Related Errors

- [Dependency Resolution Failed]({{< relref "/tools/maven/maven-dependency-resolution-failed" >}}) -- resolution failures
- [Enforcer Error]({{< relref "/tools/maven/maven-enforcer-error" >}}) -- enforcer plugin issues
