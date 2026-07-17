---
title: "Maven Compiler Error"
description: "Maven compiler plugin fails during Java source code compilation."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
tags: ["maven", "compiler", "compile", "java", "syntax"]
weight: 5
---

# Maven Compiler Error

A Maven compiler error occurs when the `maven-compiler-plugin` fails to compile Java source code. The error messages identify specific compilation failures with file paths and line numbers.

## Common Causes

- Java source code syntax errors
- Missing imports or undefined classes
- Java version mismatch (source vs. compiler version)
- Missing dependencies on the classpath

## How to Fix

### Check Compilation Output

```bash
mvn compile 2>&1 | grep "ERROR"
```

### Fix Source Code Errors

The compiler output will show specific errors:

```
[ERROR] /src/main/java/com/example/App.java:[10,5] error: cannot find symbol
[ERROR] symbol:   class MissingClass
```

### Verify Java Version Configuration

```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
</properties>
```

### Add Missing Dependencies

```xml
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>missing-library</artifactId>
        <version>1.0.0</version>
    </dependency>
</dependencies>
```

### Run Compiler with Debug

```bash
mvn compile -X 2>&1 | grep "compiler"
```

### Use Annotation Processing

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <annotationProcessorPaths>
            <path>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <version>1.18.28</version>
            </path>
        </annotationProcessorPaths>
    </configuration>
</plugin>
```

## Examples

```bash
mvn compile
[ERROR] /src/main/java/com/example/App.java:[5,1] error: class, interface, or enum expected
[ERROR] /src/main/java/com/example/App.java:[10,25] error: cannot find symbol
[ERROR] symbol:   class List
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Version Error]({{< relref "/tools/maven/maven-version-error" >}}) — version mismatch
- [Test Error]({{< relref "/tools/maven/maven-test-error" >}}) — test failure
