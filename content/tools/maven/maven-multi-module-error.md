---
title: "Maven Multi-Module Reactor Build Error"
description: "Maven multi-module reactor build fails during configuration or execution."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "multi-module", "reactor", "aggregator", "parent"]
weight: 5
---

# Maven Multi-Module — Reactor Build Error

This error occurs when a Maven multi-module reactor build fails. Issues with module order, missing modules, or dependency cycles cause the reactor to fail before or during module processing.

## Common Causes

- Module not listed in parent POM `<modules>` section
- Circular dependency between modules
- Module directory does not exist
- Wrong module order in reactor
- Parent POM version mismatch

## How to Fix

### Verify Module List in Parent POM

```xml
<modules>
    <module>core</module>
    <module>data</module>
    <module>api</module>
    <module>app</module>
</modules>
```

### Fix Circular Dependencies

```bash
# Check for circular dependencies
mvn dependency:tree -pl core
```

### Use Correct Module Directory Names

```xml
<modules>
    <module>my-core</module>  <!-- directory must be my-core/ -->
</modules>
```

### Run Specific Module

```bash
mvn clean install -pl core -am  # -am includes dependencies
```

### Validate Reactor Order

```bash
mvn validate
mvn dependency:tree
```

### Fix Parent Version Reference

```xml
<parent>
    <groupId>com.example</groupId>
    <artifactId>parent-pom</artifactId>
    <version>1.0-SNAPSHOT</version>
    <relativePath>../pom.xml</relativePath>
</parent>
```

## Examples

```text
[ERROR] The following artifacts could not be resolved:
  com.example:core:jar:1.0-SNAPSHOT:
  Could not find artifact com.example:core:jar:1.0-SNAPSHOT

[ERROR] Non-resolvable parent POM for com.example:app:1.0-SNAPSHOT:
  Parent 'com.example:parent' not found
```

## Related Errors

- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — dependency resolution failure
- [Maven Release Error]({{< relref "/tools/maven/maven-release-error" >}}) — SNAPSHOT version issues
