---
title: "Gradle Cache Error"
description: "Gradle build cache is corrupted, causing build failures or incorrect build results."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "cache", "corrupted", "build-cache", "clean"]
weight: 5
---

# Gradle Cache Error

A Gradle cache error occurs when the build cache or dependency cache becomes corrupted. This can cause builds to fail with unexpected errors or produce incorrect build outputs.

## Common Causes

- Interrupted build process corrupts cache files
- Disk space exhaustion during build
- Concurrent Gradle processes writing to cache
- Cache format changed between Gradle versions

## How to Fix

### Clean Gradle Cache

```bash
rm -rf ~/.gradle/caches/
```

### Clean Project Build Cache

```bash
./gradlew clean
rm -rf build/
```

### Use Offline Mode After Cleaning

```bash
./gradlew build --refresh-dependencies
```

### Delete Specific Module Cache

```bash
rm -rf ~/.gradle/caches/modules-2/files-2.1/com.example/library/
```

### Disable Build Cache Temporarily

```bash
./gradlew build --no-build-cache
```

### Check Disk Space

```bash
df -h ~/.gradle/
```

## Examples

```bash
./gradlew build
# FAILURE: Could not resolve com.example:library:1.0.0.
# > Could not GET '...'
# > Premature end of file

# Fix:
rm -rf ~/.gradle/caches/
./gradlew build --refresh-dependencies
```

## Related Errors

- [Dependency Error]({{< relref "/tools/gradle/gradle-dependency-error" >}}) — resolution failure
- [Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
