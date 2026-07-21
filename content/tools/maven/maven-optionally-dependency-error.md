---
title: "Maven Optional Dependency Error"
description: "Maven optional dependency configuration is incorrect, causing required artifacts to be excluded from downstream transitive resolution."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Optional Dependency Error

Maven optional dependencies are not transitively resolved by consumers. An error occurs when a library declares a dependency as optional but consumers expect it to be available.

## Common Causes

- A library marks a required dependency as `<optional>true</optional>`
- The consumer does not explicitly declare the dependency that was optional
- A BOM import marks a dependency as optional that the consumer needs
- The optional flag was added accidentally during refactoring

## How to Fix

1. Identify which dependencies are marked as optional:

```bash
mvn dependency:tree -Dverbose | grep "optional"
```

2. Explicitly declare the missing dependency in your project:

```xml
<dependencies>
  <!-- The library marked this as optional, so declare it explicitly -->
  <dependency>
    <groupId>com.example</groupId>
    <artifactId>optional-lib</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

3. Check if the library documentation recommends a specific dependency:

```xml
<!-- Library docs say: add this for feature X -->
<dependency>
  <groupId>com.example</groupId>
  <artifactId>feature-x-support</artifactId>
  <version>1.0.0</version>
</dependency>
```

4. Verify with the effective POM:

```bash
mvn help:effective-pom -Doutput=effective-pom.xml
grep -A5 "optional" effective-pom.xml
```

## Examples

```bash
# Dependency tree showing optional
[INFO] +- com.example:library:jar:2.0.0:compile
[INFO] |  \- com.example:optional-lib:jar:1.0.0:compile (optional)
```

```xml
<!-- Library declaring optional dependency -->
<dependency>
  <groupId>com.example</groupId>
  <artifactId>optional-lib</artifactId>
  <version>1.0.0</version>
  <optional>true</optional>
</dependency>
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}}) -- missing dependency artifacts
- [Transitive Dependency Conflict]({{< relref "/tools/maven/maven-dependency-resolution-failed" >}}) -- resolution failures
