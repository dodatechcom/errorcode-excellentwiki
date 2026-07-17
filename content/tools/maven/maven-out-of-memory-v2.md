---
title: "Maven Java Heap Space Error"
description: "Maven build fails with Java heap space out of memory error."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Java Heap Space Error

This error occurs when Maven runs out of JVM heap memory during a build. Large projects with many dependencies or heavy annotation processing can exhaust the default memory allocation.

## Common Causes

- Default heap size too small for project
- Large number of dependencies being resolved
- Memory leaks in Maven plugins
- Annotation processors consuming excessive memory
- Test suites with large data sets

## How to Fix

### Increase Maven JVM Memory

```bash
export MAVEN_OPTS="-Xmx4g -XX:MaxMetaspaceSize=512m"
mvn clean install
```

### Configure in Maven Options File

```properties
# .mvn/jvm.config
-Xmx4g
-XX:MaxMetaspaceSize=512m
```

### Set in POM Configuration

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <fork>true</fork>
        <compilerArgs>
            <arg>-J-Xmx2g</arg>
        </compilerArgs>
    </configuration>
</plugin>
```

### Reduce Memory Usage

```bash
# Skip tests to reduce memory
mvn clean package -DskipTests

# Use parallel builds
mvn clean install -T 4
```

### Configure Surefire for Less Memory

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <argLine>-Xmx2g</argLine>
    </configuration>
</plugin>
```

### Create .mvn/jvm.config

```bash
echo "-Xmx4g" > .mvn/jvm.config
echo "-XX:MaxMetaspaceSize=512m" >> .mvn/jvm.config
```

## Examples

```text
java.lang.OutOfMemoryError: Java heap space
    at java.util.Arrays.copyOf(Arrays.java:3236)
    at org.apache.maven...

java.lang.OutOfMemoryError: Metaspace
```

## Related Errors

- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Test Error]({{< relref "/tools/maven/maven-test-error" >}}) — test execution failure
- [Maven Compiler Error]({{< relref "/tools/maven/maven-compiler-error" >}}) — compiler issues
