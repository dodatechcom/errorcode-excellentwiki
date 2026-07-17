---
title: "Maven Java Heap Space Error"
description: "Maven fails with OutOfMemoryError: Java heap space during build execution."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Java Heap Space Error

This error means Maven's JVM ran out of heap memory during build execution. The build process tried to allocate more memory than the JVM was configured to allow.

## Common Causes

- Large projects with many dependencies exceed default heap limits
- Memory leaks in custom Maven plugins
- Too many parallel compilation threads
- Large resource processing (big XML files, databases)

## How to Fix

### Increase Maven Memory

```bash
export MAVEN_OPTS="-Xmx4g -XX:MaxMetaspaceSize=512m"
mvn clean install
```

### Configure in .mvn/jvm.config

```bash
# .mvn/jvm.config
-Xmx4g -XX:MaxMetaspaceSize=512m
```

### Reduce Parallel Compilation

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <fork>true</fork>
        <maxmem>2g</maxmem>
    </configuration>
</plugin>
```

### Build Modules Sequentially

```bash
mvn clean install -T 1
```

### Skip Resource Processing

```bash
mvn clean compile -Dmaven.resources.skip=true
```

### Check Available Memory

```bash
free -h
```

## Examples

```bash
mvn clean install
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.11.0:compile
[ERROR] Java heap space
[ERROR] GC overhead limit exceeded
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Test Error]({{< relref "/tools/maven/maven-test-error" >}}) — test failure
