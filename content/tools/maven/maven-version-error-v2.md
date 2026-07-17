---
title: "Maven Version Range Conflict"
description: "Maven encounters version range conflicts during dependency resolution."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["maven", "version", "range", "conflict", "dependency"]
weight: 5
---

# Maven Version Range Conflict in Maven

This error occurs when Maven encounters conflicting version range requirements from different dependencies. Maven cannot find a version that satisfies all version range constraints simultaneously.

## Common Causes

- Dependency A requires version [1.0, 2.0)
- Dependency B requires version [1.5, 3.0)
- Ranges are mutually exclusive or have no overlap
- SNAPSHOT versions in version ranges

## How to Fix

### Pin Specific Versions Instead of Ranges

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>1.5.0</version>  <!-- exact version instead of range -->
</dependency>
```

### Use Dependency Management

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>library</artifactId>
            <version>1.5.0</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### Resolve Version Conflict

```bash
mvn dependency:tree -Dverbose
```

### Force Specific Version

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>library</artifactId>
    <version>[1.0,)</version>
</dependency>
```

### Exclude Conflicting Transitive Dependencies

```xml
<dependency>
    <groupId>com.example</groupId>
    <artifactId>module-a</artifactId>
    <version>1.0</version>
    <exclusions>
        <exclusion>
            <groupId>com.example</groupId>
            <artifactId>library</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

## Examples

```text
[ERROR] Failed to execute goal on project app:
  Could not resolve version conflict:
  com.example:lib:jar:[1.0,2.0) requested by module-a
  com.example:lib:jar:[2.0,3.0) requested by module-b
  Version range conflict: no version satisfies both constraints
```

## Related Errors

- [Maven Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — artifact not found
- [Maven Dependency Tree Error]({{< relref "/tools/maven/maven-dependency-tree-error" >}}) — dependency conflicts
- [Maven Enforcer Error]({{< relref "/tools/maven/maven-enforcer-error" >}}) — dependency convergence
