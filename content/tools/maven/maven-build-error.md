---
title: "Maven Build Failed"
description: "Maven build fails with a BUILD FAILURE message during compilation, testing, or packaging."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Maven Build Failed

A Maven build failure means the build process encountered a fatal error. The `BUILD FAILURE` message identifies the specific goal that failed and the root cause.

## Common Causes

- Compilation errors in source code
- Test failures
- Dependency resolution issues
- Plugin execution errors
- Insufficient disk space or memory

## How to Fix

### Run with Debug Output

```bash
mvn clean install -X
```

### Skip Tests Temporarily

```bash
mvn clean install -DskipTests
```

### Read the Error Report

```bash
mvn clean install
# Look for [ERROR] lines in the output
# The first [ERROR] usually identifies the root cause
```

### Fix Compilation Errors

```bash
mvn compile 2>&1 | grep "ERROR"
```

### Increase Maven Memory

```bash
export MAVEN_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"
mvn clean install
```

### Clean and Rebuild

```bash
mvn clean install -U  # force update snapshots
```

### Check Java Version

```bash
java -version
mvn -version
```

## Examples

```bash
mvn clean install
[INFO] BUILD FAILURE
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.11.0:compile
[ERROR] /src/main/java/com/example/App.java:[5,25] error: cannot find symbol
[ERROR] BUILD FAILURE
[ERROR] Tests run: 3, Failures: 1, Errors: 0, Skipped: 0
```

## Related Errors

- [Dependency Error]({{< relref "/tools/maven/maven-dependency-error" >}}) — resolution failure
- [Plugin Error]({{< relref "/tools/maven/maven-plugin-error" >}}) — plugin execution failure
- [Out of Memory]({{< relref "/tools/maven/maven-out-of-memory" >}}) — heap space exhausted
