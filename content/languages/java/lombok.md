---
title: "[Solution] Lombok Annotation Processing Error — Lombok Fix"
description: "Fix Lombok annotation processing errors in Java. Configure IDE, build tools, and dependency setup for Lombok."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Lombok Annotation Processing Error — Lombok Fix

Lombok annotation processing errors occur when the Java compiler cannot process Lombok annotations. This can manifest as missing getter/setter methods, compilation failures, or IDE warnings.

## What This Error Means

Common messages:

- `cannot find symbol: method getXxx()`
- `Lombok annotation processor ... did not return anything`

## Common Causes

```java
// Cause 1: Lombok not added as dependency
// pom.xml missing Lombok dependency

// Cause 2: Annotation processor not configured
// IDE doesn't know about Lombok annotation processor

// Cause 3: Lombok version incompatible with Java version
// Using Lombok 1.18.20 with Java 21
```

## How to Fix

### Fix 1: Add Lombok dependency (Maven)

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>

<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <annotationProcessorPaths>
            <path>
                <groupId>org.projectlombok</groupId>
                <artifactId>lombok</artifactId>
                <version>${lombok.version}</version>
            </path>
        </annotationProcessorPaths>
    </configuration>
</plugin>
```

### Fix 2: Add Lombok dependency (Gradle)

```groovy
compileOnly 'org.projectlombok:lombok:1.18.30'
annotationProcessor 'org.projectlombok:lombok:1.18.30'
```

### Fix 3: Install Lombok plugin in IDE

- **IntelliJ**: Settings > Plugins > Search "Lombok" > Install
- **Eclipse**: Help > Eclipse Marketplace > Search "Lombok" > Install

### Fix 4: Add Lombok config file

```properties
# lombok.config
config.stopBubbling = true
lombok.addLombokGeneratedAnnotation = true
```

## Related Errors

- {{< relref "classnotfoundexception" >}} — Class not found at runtime
- {{< relref "noclassdeffounderror" >}} — Class definition not found
- {{< relref "unsupportedclassversionerror" >}} — Unsupported class version
