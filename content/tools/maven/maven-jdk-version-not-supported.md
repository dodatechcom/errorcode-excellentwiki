---
title: "Maven JDK Version Not Supported"
description: "Maven build fails because the required JDK version is not available or the configured toolchain does not match the installed JDK."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven JDK Version Not Supported

Maven requires a JDK to compile and run. This error occurs when the project specifies a JDK version that is not installed or the Maven compiler plugin is configured for an unsupported version.

## Common Causes

- The `maven.compiler.source` or `maven.compiler.target` properties specify a version newer than the installed JDK
- The JDK toolchain is configured but no matching JDK is available
- The Maven wrapper script uses a different JDK than expected
- The `JAVA_HOME` environment variable points to an incompatible JDK

## How to Fix

1. Check the installed JDK version:

```bash
java -version
echo $JAVA_HOME
```

2. Set the correct JDK in `pom.xml` properties:

```xml
<properties>
  <maven.compiler.source>11</maven.compiler.source>
  <maven.compiler.target>11</maven.compiler.target>
</properties>
```

3. Configure the Maven compiler plugin explicitly:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <configuration>
    <source>11</source>
    <target>11</target>
  </configuration>
</plugin>
```

4. Set the JDK toolchain in the build:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <release>11</release>
  </configuration>
</plugin>
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.11.0
  (default-compile): Unsupported source version 17
```

```xml
<!-- Correct JDK version configuration -->
<properties>
  <maven.compiler.source>17</maven.compiler.source>
  <maven.compiler.target>17</maven.compiler.target>
</properties>
```

## Related Errors

- [Java Version Mismatch]({{< relref "/tools/maven/maven-java-version-mismatch" >}}) -- version mismatch issues
- [JDK Toolchain Error]({{< relref "/tools/maven/maven-jdk-toolchain-error" >}}) -- toolchain configuration
