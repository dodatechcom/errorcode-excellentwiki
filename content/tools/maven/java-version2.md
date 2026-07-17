---
title: "[Solution] Maven Invalid Java Version"
description: "Fix Maven invalid Java version errors. Resolve JDK compatibility and compiler configuration issues."
tools: ["maven"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Maven Invalid Java Version

Maven fails when the configured Java source/target version is not supported by the current JDK, or when the JDK itself is incompatible with the Maven version being used.

## Common Causes

- `source` or `target` in the compiler plugin is set to a version the JDK cannot compile
- JAVA_HOME points to an older JDK than what the code requires
- The maven-compiler-plugin version does not support the specified Java version
- Maven version is too old for the JDK being used

## How to Fix

### Check Current Java Version

```bash
java -version
mvn --version
```

### Set Source and Target in pom.xml

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

### Use Maven Toolchains for Multiple JDKs

```xml
<!-- ~/.m2/toolchains.xml -->
<toolchains>
    <toolchain>
        <type>jdk</type>
        <provides>
            <version>17</version>
        </provides>
        <configuration>
            <jdkHome>/usr/lib/jvm/java-17-openjdk</jdkHome>
        </configuration>
    </toolchain>
</toolchains>
```

### Set JAVA_HOME

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
mvn package
```

## Examples

```bash
# source=17 but JDK 11 is running
mvn package
# [ERROR] Unsupported source version: 17
# Fix: install JDK 17 or set JAVA_HOME to JDK 17

# Invalid release version
mvn package
# [ERROR] invalid target release: 21
# Fix: update maven-compiler-plugin to 3.11+ and use JDK 21
```

## Related Errors

- [Plugin Error]({{< relref "/tools/maven/plugin-error2" >}}) — plugin execution failure
- [Build Failed]({{< relref "/tools/maven/build-failed" >}}) — general build failure
