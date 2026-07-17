---
title: "Gradle Could Not Resolve Dependency"
description: "Gradle fails to resolve a dependency due to version conflict or missing artifact."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "dependency", "resolution", "version", "conflict"]
weight: 5
---

# Gradle Could Not Resolve Dependency

This error occurs when Gradle cannot resolve a dependency from any configured repository, or when there is a version conflict between transitive dependencies. The build stops because required libraries are unavailable.

## Common Causes

- Artifact does not exist in configured repositories
- Version conflict between transitive dependencies
- Repository URL is incorrect or requires authentication
- Network issues preventing repository access
- SNAPSHOT dependency no longer available

## How to Fix

### Debug Dependency Resolution

```bash
./gradlew dependencies --configuration compileClasspath
```

### Force a Specific Version

```groovy
configurations.all {
    resolutionStrategy {
        force 'com.google.guava:guava:31.1-jre'
    }
}
```

### Exclude Conflicting Transitive Dependency

```groovy
dependencies {
    implementation('com.example:library:1.0.0') {
        exclude group: 'commons-logging', module: 'commons-logging'
    }
}
```

### Add Missing Repository

```groovy
repositories {
    mavenCentral()
    maven { url 'https://repo.example.com/releases' }
}
```

### Resolve Version Conflicts

```groovy
configurations.all {
    resolutionStrategy {
        failOnVersionConflict()
    }
}
```

### Check for Latest Version

```bash
./gradlew dependencyUpdates -Drevision=release
```

## Examples

```text
Could not resolve com.example:library:2.0.0.
  > Could not find com.example:library:2.0.0 in
    [https://repo.maven.apache.org/maven2/].

Could not resolve com.google.guava:guava:31.1-jre.
  > Cannot choose between [guava:30.1-jre, guava:31.1-jre]
```

## Related Errors

- [Gradle Plugin Error]({{< relref "/tools/gradle/gradle-plugin-error" >}}) — plugin not found
- [Gradle Cache Error]({{< relref "/tools/gradle/gradle-cache-error" >}}) — corrupted cache entries
- [Gradle Wrapper Error]({{< relref "/tools/gradle/gradle-wrapper-error" >}}) — wrapper download failure
