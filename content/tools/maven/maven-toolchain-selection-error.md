---
title: "Maven Toolchain Selection Error"
description: "Maven toolchain plugin cannot find a matching JDK toolchain for the requested version, causing compilation to fail."
tools: ["maven"]
error-types: ["tool-error"]
severities: ["error"]
---

# Maven Toolchain Selection Error

Maven toolchains allow builds to use specific JDK versions. A selection error occurs when no installed toolchain matches the version requested by the compiler plugin.

## Common Causes

- The requested JDK version is not installed on the machine
- The `toolchains.xml` file does not contain a matching toolchain entry
- The toolchain vendor or OS type does not match what is available
- The toolchain path points to a JRE instead of a full JDK

## How to Fix

1. Check available toolchains:

```bash
mvn toolchain:list
```

2. Configure a toolchain entry in `~/.m2/toolchains.xml`:

```xml
<toolchains>
  <toolchain>
    <type>jdk</type>
    <provides>
      <version>11</version>
      <vendor>oracle</vendor>
    </provides>
    <configuration>
      <jdkHome>/usr/lib/jvm/java-11-oracle</jdkHome>
    </configuration>
  </toolchain>
</toolchains>
```

3. Configure the compiler plugin to use a toolchain:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.11.0</version>
  <configuration>
    <toolchain>
      <version>11</version>
    </toolchain>
  </configuration>
</plugin>
```

4. Install the required JDK:

```bash
sudo apt-get install openjdk-11-jdk
```

## Examples

```bash
# Error output
[ERROR] Failed to execute goal compiler:compile
  No toolchain found with matching version: 11
  Available toolchains: [jdk-17]
```

```xml
<!-- Complete toolchains.xml example -->
<toolchains>
  <toolchain>
    <type>jdk</type>
    <provides>
      <version>11</version>
    </provides>
    <configuration>
      <jdkHome>/usr/lib/jvm/java-11-openjdk-amd64</jdkHome>
    </configuration>
  </toolchain>
</toolchains>
```

## Related Errors

- [JDK Toolchain Error]({{< relref "/tools/maven/maven-jdk-toolchain-error" >}}) -- toolchain configuration
- [Java Version Mismatch]({{< relref "/tools/maven/maven-java-version-mismatch" >}}) -- version mismatch issues
