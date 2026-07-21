---
title: "Incompatible Target JVM Error"
description: "Gradle compilation fails because the target JVM version does not match the source bytecode version or toolchain availability."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Incompatible Target JVM Error

Gradle compiles Java or Kotlin code targeting a specific JVM version. This error occurs when the target JVM version is higher than the source version or no compatible toolchain is available.

## Common Causes

- The `sourceCompatibility` or `targetCompatibility` is set to a version newer than the JDK in use
- The Java toolchain configuration specifies a JDK version that is not installed
- The compiled bytecode uses features not available in the target JVM
- Cross-compilation is attempted without a toolchain resolver plugin

## How to Fix

1. Check the currently active JDK version:

```bash
java -version
javac -version
```

2. Configure source and target compatibility:

```groovy
java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}
```

3. Use a Java toolchain for cross-compilation:

```groovy
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(11)
    }
}
```

4. Install the required JDK and configure Gradle to find it:

```bash
# Install JDK 11
sudo apt-get install openjdk-11-jdk

# Verify
/usr/lib/jvm/java-11-openjdk-amd64/bin/java -version
```

## Examples

```bash
# Error output
> Incompatible JVM detected. Source level 17 requires JDK 17 or higher.
  Current JDK: 11.0.20
```

```groovy
// Toolchain-based compilation
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(17)
    }
}

tasks.withType(JavaCompile) {
    options.compilerArgs += ['-Xlint:all']
}
```

## Related Errors

- [Java Compilation Failed]({{< relref "/tools/gradle/gradle-java-compilation-failed" >}}) -- general Java compile failures
- [Java Home Not Set]({{< relref "/tools/gradle/java-version" >}}) -- JAVA_HOME configuration issues
