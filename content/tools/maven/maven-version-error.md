---
title: "Maven Version Mismatch Error"
description: "Maven build fails due to version incompatibility between Maven, plugins, or Java."
tools: ["maven"]
error-types: ["build-error"]
severities: ["error"]
tags: ["maven", "version", "compatibility", "java", "plugin"]
weight: 5
---

# Maven Version Mismatch Error

A Maven version mismatch error occurs when the Maven version, Java version, or plugin versions are incompatible. Maven has strict compatibility requirements between these components.

## Common Causes

- Java version does not match Maven requirements
- Maven plugin requires a newer Maven version
- Source/target Java version in compiler plugin is too high for installed JDK
- Plugin version conflicts between modules

## How to Fix

### Check Maven and Java Versions

```bash
mvn -version
java -version
```

### Configure Java Version in pom.xml

```xml
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
</properties>
```

### Set JAVA_HOME

```bash
export JAVA_HOME=/usr/lib/jvm/java-17
mvn clean install
```

### Update Maven

```bash
# Using Maven wrapper
mvn wrapper:wrapper -Dmaven=3.9.5
```

### Check Plugin Requirements

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

### Use Maven Wrapper for Consistent Version

```bash
mvn wrapper:wrapper
./mvnw clean install
```

## Examples

```bash
mvn clean install
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.11.0:compile
[ERROR] Unsupported target version: 21 for source 21
[ERROR] Java 21 requires maven-compiler-plugin 3.12.0 or higher
```

## Related Errors

- [Build Failed]({{< relref "/tools/maven/maven-build-error" >}}) — general build failure
- [Plugin Error]({{< relref "/tools/maven/maven-plugin-error" >}}) — plugin execution failure
