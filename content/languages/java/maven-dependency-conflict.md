---
title: "[Solution] ExecutionException — Maven Dependency Version Conflict Fix"
description: "Fix Maven dependency tree conflicts and resolution errors. Resolve version mismatches and transitive dependency issues."
languages: ["java"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# ExecutionException — Maven Dependency Version Conflict Fix

An `ExecutionException` from the Maven dependency plugin means Maven could not resolve version conflicts between dependencies. This happens when multiple dependency trees require incompatible versions of the same library.

## What This Error Means

Common messages:

- `org.apache.maven.plugins.maven.dependency.trees.ExecutionException: Could not resolve dependencies`
- `Could not find artifact com.google.guava:guava:jar:31.1-jre in central`
- `Dependency convergence error for com.fasterxml.jackson.core:jackson-databind`

## Common Causes

```xml
<!-- Cause 1: Transitive dependency version conflict -->
<!-- Library A requires Guava 31.1 -->
<!-- Library B requires Guava 30.0 -->
<!-- Maven picks one, potentially breaking the other -->

<!-- Cause 2: SNAPSHOT version not available in repository -->
<dependency>
    <groupId>com.example</groupId>
    <artifactId>lib</artifactId>
    <version>1.0-SNAPSHOT</version> <!-- May not exist in remote -->
</dependency>

<!-- Cause 3: Dependency not in any configured repository -->
```

## How to Fix

### Fix 1: Use mvn dependency:tree to identify conflicts

Analyze the dependency tree to find which libraries are pulling in conflicting versions.

```java
# Show the full dependency tree
mvn dependency:tree

# Filter for a specific artifact
mvn dependency:tree -Dincludes=com.fasterxml.jackson.core

# Show verbose output with conflict markers
mvn dependency:tree -Dverbose -Dincludes=commons-logs
```

### Fix 2: Exclude transitive dependencies and specify versions

Explicitly exclude the conflicting transitive dependency and declare the version you need.

```java
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library-a</artifactId>
    <version>2.0</version>
    <exclusions>
        <exclusion>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
        </exclusion>
    </exclusions>
</dependency>

<dependency>
    <groupId>com.example</groupId>
    <artifactId>library-b</artifactId>
    <version>3.0</version>
    <exclusions>
        <exclusion>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
        </exclusion>
    </exclusions>
</dependency>

<!-- Declare the version you need explicitly -->
<dependency>
    <groupId>com.google.guava</groupId>
    <artifactId>guava</artifactId>
    <version>31.1-jre</version>
</dependency>
```

### Fix 3: Use Maven Enforcer plugin to prevent conflicts

Add the enforcer plugin to your build to automatically detect dependency convergence issues.

```java
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

## Related Errors

- {{< relref "maven-plugin-error" >}} — Plugin Execution Error
- {{< relref "gradle-dependency-lock" >}} — Gradle Dependency Lock Error
