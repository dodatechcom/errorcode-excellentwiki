---
title: "[Solution] Java NoClassDefFoundError — transitive dependency excluded or marked optional in dependency tree"
description: "Fix Java NoClassDefFoundError when transitive dependency excluded or marked optional in dependency tree with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoClassDefFoundError — transitive dependency excluded or marked optional in dependency tree

A `NoClassDefFoundError` occurs when <exclusions><exclusion>jsr305</exclusion></exclusions>
// @Nullable from jsr305 now causes NoClassDefFoundError.

## Common Causes

```java
<exclusions><exclusion>jsr305</exclusion></exclusions>
// @Nullable from jsr305 now causes NoClassDefFoundError
```

## Solutions

```java
// Fix: add missing transitive
<dependency>
    <groupId>com.google.code.findbugs</groupId>
    <artifactId>jsr305</artifactId>
    <version>3.0.2</version>
</dependency>

// Fix: analyze
// mvn dependency:tree -Dverbose
// gradle dependencies
```

## Prevention Checklist

- Run dependency tree regularly.
- Never exclude transitives without understanding impact.
- Use dependency management BOMs.

## Related Errors

ClassNotFoundException, LinkageError
