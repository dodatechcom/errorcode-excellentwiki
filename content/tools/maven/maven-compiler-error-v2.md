---
title: "Maven Compiler Source Target Version Error"
description: "Maven compiler plugin fails due to source or target version mismatch."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Compiler — Source/Target Version Error

This error occurs when the Maven compiler plugin has mismatched source and target versions, or when the configured Java version is incompatible with the compiler settings.

## Common Causes

- Source version newer than the installed JDK
- Target version not supported by the compiler
- Source and target versions are incompatible
- JDK version mismatch between Maven and project

## How to Fix

### Configure Compiler Plugin Versions

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.11.0</version>
    <configuration>
        <source>17</source>
        <target>17</target>
    </configuration>
</plugin>
```

### Use Release Flag Instead of Source/Target

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
        <release>17</release>
    </configuration>
</plugin>
```

### Check Installed Java Version

```bash
java -version
javac -version
```

### Set JAVA_HOME

```bash
export JAVA_HOME=/usr/lib/jvm/java-17
mvn clean install
```

### Configure Properties in POM

```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
    <maven.compiler.release>17</maven.compiler.release>
</properties>
```

### Fix Cross-Compilation Issues

```bash
# Use a toolchain for cross-compilation
mvn clean install -Djava.home=/usr/lib/jvm/java-11
```

## Examples

```text
[ERROR] /home/user/src/main/java/App.java:
  error: source release 17 requires target release 17

[ERROR] unsupported source version 21 in -source option
```

## Related Errors

- [Maven Build Error]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Maven Compiler Error]({{< relref "/tools/maven/maven-compiler-error" >}}) — compiler configuration error
- [Maven Out of Memory]({{< relref "/tools/maven/maven-out-of-memory" >}}) — heap space during compilation
