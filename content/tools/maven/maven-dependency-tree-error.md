---
title: "Maven Dependency Tree Conflict Detected"
description: "Maven dependency tree reveals version conflicts between transitive dependencies."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Dependency Tree — Conflict Detected

This error occurs when Maven detects version conflicts in the dependency tree. Multiple paths to the same artifact require different versions, causing unpredictable behavior.

## Common Causes

- Two dependencies require different versions of the same artifact
- Transitive dependencies pulling conflicting versions
- No version management configured for common libraries

## How to Fix

### Analyze the Dependency Tree

```bash
mvn dependency:tree
mvn dependency:tree -Dverbose
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

### Use BOM for Version Alignment

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-dependencies-bom</artifactId>
            <version>6.1.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### Force Specific Version

```xml
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>31.1-jre</version>
    <scope>compile</scope>
</dependency>
```

### Filter Dependency Tree

```bash
mvn dependency:tree -Dincludes=com.google.guava:guava
```

## Examples

```text
[INFO] com.example:app:jar:1.0
[INFO] +- com.example:module-a:jar:1.0
[INFO] |  \- com.google.guava:guava:jar:30.1-jre
[INFO] \- com.example:module-b:jar:1.0
[INFO]    \- com.google.guava:guava:jar:31.1-jre (managed) -> 31.1-jre
```

## Related Errors

- [Maven Enforcer Error]({{< relref "/tools/maven/maven-enforcer-error" >}}) — dependency convergence enforcement
- [Maven Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — artifact not found
- [Maven Version Error]({{< relref "/tools/maven/maven-version-error" >}}) — version range conflicts
