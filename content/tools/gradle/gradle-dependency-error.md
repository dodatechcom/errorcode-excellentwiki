---
title: "Could Not Resolve Dependency — Gradle"
description: "Gradle cannot resolve a required dependency from any configured repository."
tools: ["gradle"]
error-types: ["build-error"]
severities: ["error"]
tags: ["gradle", "dependency", "resolve", "repository", "artifact"]
weight: 5
---

# Could Not Resolve Dependency — Gradle

This error means Gradle looked in all configured repositories (Maven Central, local cache, custom repos) but could not find the artifact specified in your build script. The dependency coordinates or repository configuration are incorrect.

## Common Causes

- The dependency is misspelled in `build.gradle`
- The artifact does not exist in the configured repositories
- A custom repository URL is incorrect or requires authentication
- Network issues prevent repository access

## How to Fix

### Verify Dependency Coordinates

```groovy
dependencies {
    implementation 'com.example:library:1.0.0'  // check groupId, artifactId, version
}
```

Search [Maven Central](https://search.maven.org) for the correct coordinates.

### Add Missing Repository

```groovy
repositories {
    mavenCentral()
    maven { url 'https://repo.example.com/releases' }
}
```

### Configure Repository Authentication

```groovy
repositories {
    maven {
        url 'https://repo.example.com/releases'
        credentials {
            username = findProperty('repoUser') ?: ''
            password = findProperty('repoPassword') ?: ''
        }
    }
}
```

### Check Network Connectivity

```bash
curl -I https://repo.maven.apache.org/maven2/
```

### Clear Gradle Cache and Retry

```bash
rm -rf ~/.gradle/caches/modules-2/files-2.1/com.example
./gradlew build --refresh-dependencies
```

## Examples

```bash
./gradlew build
# FAILURE: Could not resolve com.example:library:1.0.0.
# Required by:
#     project :app
# > Could not find any matches for com.example:library:1.0.0
```

## Related Errors

- [Cache Error]({{< relref "/tools/gradle/cache-error3" >}}) — corrupted cache causing resolution issues
- [Build Failed]({{< relref "/tools/gradle/build-failed" >}}) — general build failure
