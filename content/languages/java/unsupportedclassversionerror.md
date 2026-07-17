---
title: "[Solution] Java UnsupportedClassVersionError — Class Version Fix"
description: "Fix Java UnsupportedClassVersionError by compiling with a compatible JDK version, using --release flag, and matching compile target with runtime JVM."
languages: ["java"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# UnsupportedClassVersionError — Class Version Fix

An `UnsupportedClassVersionError` is thrown when the JVM attempts to load a class file that was compiled with a newer JDK version than the runtime JVM supports. This is a subclass of `LinkageError`.

## Description

Each JDK version produces class files with a specific major version number. A JVM can only run class files up to its supported major version. For example, JDK 11 (major version 55) cannot run class files compiled with JDK 17 (major version 61).

Common version mappings:

- JDK 8: major version 52
- JDK 11: major version 55
- JDK 17: major version 61
- JDK 21: major version 65

## Common Causes

```java
// Cause 1: Class compiled with newer JDK than runtime JVM
// Compiled with JDK 21, running on JDK 11

// Cause 2: Docker image uses older JDK than build environment
// Build: JDK 21, Runtime: openjdk:11

// Cause 3: Mixed JDK versions in multi-module project
// Module A compiled with JDK 21, Module B with JDK 17

// Cause 4: IDE configured with different JDK than build tool
// IDE uses JDK 21, Maven uses JDK 11
```

## Solutions

```java
// Fix 1: Cross-compile for the target JDK version
// javac --release 11 MyClass.java

// Fix 2: Configure Maven to target specific version
// <plugin>
//     <groupId>org.apache.maven.plugins</groupId>
//     <artifactId>maven-compiler-plugin</artifactId>
//     <configuration>
//         <source>11</source>
//         <target>11</target>
//     </configuration>
// </plugin>

// Fix 3: Verify class file version
// javap -v MyClass.class | grep "major version"

// Fix 4: Use matching JDK for build and runtime
// Build with same JDK version as deployment target
```

## Examples

```java
// Example: Code using JDK 21 features run on JDK 17
// JDK 21: String s = "hello".indent(4);  // preview feature
// Running on JDK 17: UnsupportedClassVersionError

// Check version in code
public class VersionChecker {
    public static void main(String[] args) {
        System.out.println("Java version: " + System.getProperty("java.version"));
    }
}
```

## Related Exceptions

- [ClassFormatError]({{< relref "/languages/java/classformaterror" >}}) — class file is malformed
- [NoClassDefFoundError](../noclassdeffounderror) — class file missing
- [LinkageError](../linkageerror) — parent class for linkage failures
