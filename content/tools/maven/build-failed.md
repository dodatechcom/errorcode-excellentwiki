---
title: "Build Failure: Failed to Execute Goal on Project"
description: "Maven build failed because it could not execute a goal, often due to dependency or plugin resolution issues."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
tags: ["maven", "build", "goal", "failure"]
weight: 5
---

This error indicates that Maven encountered a failure while executing a plugin goal during the build lifecycle. The specific goal and phase are reported in the error message.

## Common Causes

- A required dependency cannot be resolved from any configured repository
- A Maven plugin version is incompatible or missing
- The `pom.xml` contains incorrect configuration for a plugin
- Local repository cache is corrupted

## How to Fix

Force update of snapshots and releases:

```bash
mvn clean install -U
```

Check which dependency is failing and verify it exists:

```bash
mvn dependency:resolve
```

Ensure plugin versions are explicitly declared in your `pom.xml`:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
</plugin>
```

## Examples

```
[ERROR] Failed to execute goal on project my-app: Could not resolve dependencies for project com.example:my-app:jar:1.0-SNAPSHOT: The following artifacts could not be resolved:
[ERROR]   com.example:library:jar:1.0.0: Could not find artifact com.example:library:jar:1.0.0 in central (https://repo.maven.apache.org/maven2)
[ERROR]
[ERROR] -> [Help 1]
```

## Related Errors

- [Dependency Not Found]({{< relref "/tools/maven/dependency-not-found" >}})
