---
title: "[Solution] Gradle Cache Corruption"
description: "Fix Gradle cache corruption errors. Resolve build cache and dependency resolution issues."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Cache Corruption

Cache corruption occurs when Gradle's local cache contains invalid, incomplete, or mismatched data. This can cause builds to fail with cryptic errors about mismatched checksums or missing artifacts.

## Common Causes

- A previous build was interrupted, leaving partial cache entries
- Disk space ran out during a download
- Manual deletion of cache files while Gradle was running
- Corrupted `.gradle` directory in the project or home folder

## How to Fix

### Clean the Project Build Cache

```bash
./gradlew clean
rm -rf build/
```

### Delete the Gradle Home Cache

```bash
rm -rf ~/.gradle/caches/
rm -rf ~/.gradle/wrapper/
```

### Use the --refresh-dependencies Flag

```bash
./gradlew build --refresh-dependencies
```

### Delete the Daemon Cache

```bash
./gradlew --stop
rm -rf ~/.gradle/daemon/
```

### Nuclear Option: Clear Everything

```bash
rm -rf ~/.gradle/
./gradlew build
```

## Examples

```bash
# Checksum mismatch after interrupted download
./gradlew build
# FAILURE: Could not resolve all dependencies.
# SHA-1 mismatch for: library-1.0.jar
# Fix: rm -rf ~/.gradle/caches/ && ./gradlew build

# Stale lock file
./gradlew build
# FAILURE: Could not lock configuration cache
# Fix: rm -rf .gradle/configuration-cache/
```

## Related Errors

- [Task Error]({{< relref "/tools/gradle/task-error" >}}) — task execution failure
- [Configuration Error]({{< relref "/tools/gradle/config-error4" >}}) — build script evaluation failure
