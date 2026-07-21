---
title: "Maven Dependency Scope Error"
description: "Maven dependency scope is misconfigured, causing compile-time or runtime classpath issues and missing artifacts at deployment."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Dependency Scope Error

Maven dependency scopes control when and where a dependency is available. A scope error occurs when the wrong scope is used, causing dependencies to be missing at compile time or included unnecessarily at runtime.

## Common Causes

- A `compile` scope dependency should be `provided` (like servlet-api)
- A `test` scope dependency is needed at runtime but is excluded from the classpath
- The `runtime` scope is used for a dependency needed during compilation
- The `import` scope is used outside of `<dependencyManagement>`

## How to Fix

1. Use the correct scope for the dependency:

```xml
<!-- compile scope (default) -- available everywhere -->
<dependency>
  <groupId>com.google.guava</groupId>
  <artifactId>guava</artifactId>
  <version>31.1-jre</version>
  <scope>compile</scope>
</dependency>

<!-- provided -- available during compilation, not packaged -->
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>

<!-- test -- only available during test compilation/execution -->
<dependency>
  <groupId>junit</groupId>
  <artifactId>junit</artifactId>
  <version>4.13</version>
  <scope>test</scope>
</dependency>
```

2. Check which scope is causing the issue:

```bash
mvn dependency:tree -Dscope=compile
mvn dependency:tree -Dscope=test
```

3. Verify the effective dependency scopes:

```bash
mvn help:effective-pom | grep -A3 "scope"
```

4. Use the `provided` scope for container-provided libraries:

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

## Examples

```bash
# Dependency tree showing scopes
[INFO] +- com.google.guava:guava:jar:31.1-jre:compile
[INFO] +- javax.servlet:javax.servlet-api:jar:4.0.1:provided
[INFO] +- junit:junit:jar:4.13:test
```

```xml
<!-- Wrong scope -- needs to be compile, not test -->
<dependency>
  <groupId>com.example</groupId>
  <artifactId>model</artifactId>
  <version>1.0.0</version>
  <scope>test</scope> <!-- should be compile for main source -->
</dependency>
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependency artifacts
- [System Scope Dependency Error]({{< relref "/tools/maven/maven-system-scope-dependency-error" >}}) -- system scope issues
