---
title: "Maven Source Target Incompatible"
description: "Maven compiler plugin fails because the source and target Java versions are incompatible or mismatched with the installed JDK."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Source Target Incompatible

Maven compiler plugin requires compatible source and target settings. An error occurs when the specified source level is higher than the target or when the JDK does not support the configured levels.

## Common Causes

- `maven.compiler.source` is set to a version newer than the installed JDK
- Source and target versions are from incompatible Java generations
- The `release` flag conflicts with explicit source/target settings
- A Kotlin plugin sets a different target JVM version than the Java compiler

## How to Fix

1. Use the `release` flag instead of separate source/target:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <configuration>
    <release>11</release>
  </configuration>
</plugin>
```

2. Match source and target versions:

```xml
<properties>
  <maven.compiler.source>11</maven.compiler.source>
  <maven.compiler.target>11</maven.compiler.target>
</properties>
```

3. Verify the JDK supports the requested version:

```bash
javac -version
javac --source 11 --target 11 /dev/null 2>&1 || echo "JDK does not support source/target 11"
```

4. Remove conflicting compiler options:

```xml
<configuration>
  <!-- Do not mix release with source/target -->
  <release>17</release>
  <!-- Remove: <source>11</source> and <target>11</target> -->
</configuration>
```

## Examples

```bash
# Error output
[ERROR] Source option 17 is not supported. Use 11 or later.
```

```xml
<!-- Correct configuration for cross-compilation -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <configuration>
    <release>11</release>
    <compilerArgs>
      <arg>-Xlint:all</arg>
    </compilerArgs>
  </configuration>
</plugin>
```

## Related Errors

- [Compiler Error]({{< relref "/tools/maven/maven-compiler-error" >}}) -- general compilation failures
- [Java Version Mismatch]({{< relref "/tools/maven/maven-java-version-mismatch" >}}) -- Java version issues
