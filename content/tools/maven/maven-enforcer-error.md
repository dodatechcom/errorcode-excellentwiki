---
title: "Maven Enforcer Dependency Convergence Error"
description: "Maven enforcer plugin detects dependency convergence violations."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "enforcer", "convergence", "dependency", "rule"]
weight: 5
---

# Maven Enforcer — Dependency Convergence Error

This error occurs when the Maven enforcer plugin detects dependency convergence violations. Different dependency paths bring in different versions of the same artifact.

## Common Causes

- Multiple versions of the same dependency on the classpath
- Transitive dependencies conflict with direct dependencies
- Enforcer plugin configured with strict convergence rules

## How to Fix

### Analyze Convergence Violations

```bash
mvn enforcer:enforce -Drules=dependency-convergence
```

### Exclude Conflicting Transitive Dependencies

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>module-a</artifactId>
    <version>1.0</version>
    <exclusions>
        <exclusion>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

### Use Dependency Management

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>31.1-jre</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### Configure Enforcer Plugin

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-enforcer-plugin</artifactId>
    <version>3.4.1</version>
    <executions>
        <execution>
            <id>enforce-dependency-convergence</id>
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

### Skip Enforcer Temporarily

```bash
mvn clean install -Denforcer.skip=true
```

## Examples

```text
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-enforcer-plugin:3.4.1:enforce
  Dependency convergence error for com.google.guava:guava:
  - com.google.guava:guava:30.1-jre (from com.example:module-a:1.0)
  - com.google.guava:guava:31.1-jre (from com.example:module-b:1.0)
```

## Related Errors

- [Maven Dependency Tree Error]({{< relref "/tools/maven/maven-dependency-tree-error" >}}) — dependency conflicts
- [Maven Version Error]({{< relref "/tools/maven/maven-version-error" >}}) — version range conflicts
- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
