---
title: "[Solution] Source/Target Release Mismatch — Maven Compiler Fix"
description: "Fix source release and target release version mismatches in Maven compiler plugin. Configure Java source and target versions correctly."
languages: ["java"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Source/Target Release Mismatch — Maven Compiler Fix

A compiler version mismatch error occurs when the Maven compiler plugin's `source` and `target` settings do not align with the JDK version used to compile, or when cross-compilation targets are incompatible.

## What This Error Means

Common messages:

- `source release X requires target release Y`
- `invalid source release: 21`
- `unsupported class file major version 65`
- `error: Source option 17 is not supported`

## Common Causes

```xml
<!-- Cause 1: source/target version higher than installed JDK -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <source>21</source>  <!-- JDK 17 installed, can't compile 21 -->
        <target>21</target>
    </configuration>
</plugin>

<!-- Cause 2: Maven compiler plugin version too old -->
<plugin>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.1</version> <!-- May not support Java 21 -->
</plugin>

<!-- Cause 3: JAVA_HOME pointing to wrong JDK -->
# JAVA_HOME=/usr/lib/jvm/java-11-openjdk but code needs Java 17
```

## How to Fix

### Fix 1: Align compiler settings with installed JDK

Ensure the maven-compiler-plugin source and target versions match the JDK available in your build environment.

```java
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
    <configuration>
        <source>17</source>
        <target>17</target>
        <!-- Or use release flag for safety -->
        <release>17</release>
    </configuration>
</plugin>

# Check installed JDK version
java -version
javac -version
echo $JAVA_HOME
```

### Fix 2: Use the release flag instead of source/target

The `release` flag in Java 9+ ensures source, target, and boot classpath are all consistent for a given Java version.

```java
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
    <configuration>
        <release>17</release>
    </configuration>
</plugin>

# This replaces both <source> and <target>
# and also verifies API compatibility with Java 17
```

### Fix 3: Configure toolchain for cross-compilation

Use the Maven toolchains plugin to compile against a specific JDK version regardless of the system default.

```java
<!-- toolchains.xml in ~/.m2/ -->
<toolchains>
    <toolchain>
        <type>jdk</type>
        <provides>
            <version>17</version>
            <vendor>temurin</vendor>
        </provides>
        <configuration>
            <jdkHome>/usr/lib/jvm/temurin-17</jdkHome>
        </configuration>
    </toolchain>
</toolchains>

<!-- pom.xml -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-toolchains-plugin</artifactId>
    <version>3.1.0</version>
    <executions>
        <execution>
            <goals><goal>toolchain</goal></goals>
        </execution>
    </executions>
    <configuration>
        <toolchains>
            <jdk>
                <version>17</version>
                <vendor>temurin</vendor>
            </jdk>
        </toolchains>
    </configuration>
</plugin>
```

## Related Errors

- {{< relref "maven-plugin-error" >}} — Plugin Execution Error
- {{< relref "maven-surefire" >}} — Surefire Test Failure
