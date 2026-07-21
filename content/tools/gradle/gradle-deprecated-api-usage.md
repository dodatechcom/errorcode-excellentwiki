---
title: "Deprecated Gradle API Usage"
description: "Gradle build uses deprecated APIs that will be removed in future versions, causing warnings or build failures in strict mode."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Deprecated Gradle API Usage

Gradle periodically deprecates old APIs as newer versions introduce replacements. A deprecated API usage error occurs when the build script calls methods or properties that are scheduled for removal.

## Common Causes

- Build scripts use plugin application syntax from older Gradle versions
- Task configuration uses the `<<` operator (removed in Gradle 5+)
- Deprecated `compile` or `runtime` dependency configurations are used
- The build uses `project.convention` instead of the newer extension API

## How to Fix

1. Replace deprecated dependency configurations:

```groovy
// Deprecated
dependencies {
    compile 'com.google.guava:guava:31.1-jre'
    testCompile 'junit:junit:4.13'
    runtime 'org.slf4j:slf4j-simple:1.7.36'
}

// Fixed -- use api or implementation
dependencies {
    api 'com.google.guava:guava:31.1-jre'
    testImplementation 'junit:junit:4.13'
    runtimeOnly 'org.slf4j:slf4j-simple:1.7.36'
}
```

2. Replace the `<<` task operator:

```groovy
// Deprecated (Gradle 4 and earlier)
task hello << { println 'Hello' }

// Fixed
task hello { doLast { println 'Hello' } }
```

3. Enable deprecation warnings to find all issues:

```bash
./gradlew build -Dorg.gradle.warning.mode=all
```

4. Update plugin application syntax:

```groovy
// Deprecated
apply plugin: 'java'

// Fixed
plugins {
    id 'java'
}
```

## Examples

```bash
# Warning output
w: Build script uses deprecated method: Project.convention
  This is scheduled for removal in Gradle 9.0
  Use project.extensions instead
```

```groovy
// Modern build.gradle.kts
plugins {
    java
    id('org.springframework.boot') version '3.2'
}

dependencies {
    implementation('org.springframework.boot:spring-boot-starter-web')
    testImplementation('org.springframework.boot:spring-boot-starter-test')
}
```

## Related Errors

- [Convention Deprecated]({{< relref "/tools/gradle/gradle-convention-deprecated" >}}) -- convention plugin deprecation
- [Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) -- Gradle version compatibility
