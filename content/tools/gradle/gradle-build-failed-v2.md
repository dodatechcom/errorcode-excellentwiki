---
title: "Gradle Build Failed Compilation Errors"
description: "Gradle build fails with compilation errors in source code."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "build", "compilation", "compile", "error"]
weight: 5
---

# Gradle Build Failed — Compilation Errors

This error occurs when Gradle encounters compilation errors in your source code during the build process. The compiler reports syntax errors, type mismatches, missing symbols, or other issues that prevent successful compilation.

## Common Causes

- Syntax errors in Java, Kotlin, or Groovy source files
- Missing imports or incorrect package declarations
- Type mismatches and casting errors
- API changes after upgrading dependencies
- Annotation processing failures

## How to Fix

### Run Compilation with Full Error Output

```bash
./gradlew compileJava 2>&1
```

### Use the Kotlin Compiler for Detailed Errors

```bash
./gradlew compileKotlin --warnings=all
```

### Check for Deprecation Warnings

```bash
./gradlew compileJava -Xlint:all
```

### Fix Missing Imports

```java
// Add missing import
import java.util.List;
import java.util.ArrayList;
```

### Resolve Type Mismatches

```java
// Before (error)
int result = getStringValue();

// After (fixed)
String result = getStringValue();
```

### Enable Compiler Arguments in Build

```groovy
tasks.withType(JavaCompile) {
    options.compilerArgs += ['-Xlint:unchecked', '-Xlint:deprecation']
}
```

## Examples

```text
> Task :app:compileJava FAILED
/home/user/project/src/main/java/com/example/App.java:25:
  error: incompatible types: int cannot be converted to String
    String value = getNumber();
                       ^
```

## Related Errors

- [Gradle Task Error]({{< relref "/tools/gradle/gradle-task-error" >}}) — general task failure
- [Gradle Out of Memory]({{< relref "/tools/gradle/gradle-out-of-memory" >}}) — heap space during compilation
- [Gradle Kotlin DSL Error]({{< relref "/tools/gradle/gradle-kotlin-dsl-error" >}}) — DSL script errors
