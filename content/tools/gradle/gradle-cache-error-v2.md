---
title: "Gradle Corrupted Cache Entry"
description: "Gradle build cache contains corrupted entries causing build failures."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["gradle", "cache", "corruption", "build-cache", "clean"]
weight: 5
---

# Gradle Corrupted Cache Entry

This error occurs when Gradle's build cache or dependency cache contains corrupted entries. Stale or incomplete cache files can cause unexpected build failures, incorrect outputs, or strange class loading issues.

## Common Causes

- Interrupted build left partial cache files
- Disk corruption or filesystem issues
- Multiple Gradle processes writing to the cache simultaneously
- Incompatible Gradle version wrote to shared cache

## How to Fix

### Delete Build Cache

```bash
rm -rf .gradle/caches/build-cache-*
./gradlew clean build
```

### Delete All Gradle Caches

```bash
rm -rf ~/.gradle/caches/
./gradlew build
```

### Clean Specific Cache Directory

```bash
rm -rf ~/.gradle/caches/transforms-3/
rm -rf ~/.gradle/caches/modules-2/files-2.1/
```

### Rebuild Dependencies Only

```bash
./gradlew build --refresh-dependencies
```

### Disable Build Cache Temporarily

```bash
./gradlew build --no-build-cache
```

### Configure Cache Policy

```groovy
// settings.gradle
buildCache {
    local {
        enabled = true
        removeUnusedEntriesAfterDays = 7
    }
}
```

## Examples

```text
Could not resolve com.example:library:1.0.0.
  > Could not parse POM
    > Content is not allowed in prolog.

BUILD FAILED in 2s
```

## Related Errors

- [Gradle Dependency Error]({{< relref "/tools/gradle/gradle-dependency-error" >}}) — dependency resolution failure
- [Gradle Wrapper Error]({{< relref "/tools/gradle/gradle-wrapper-error" >}}) — wrapper download issues
- [Gradle Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
