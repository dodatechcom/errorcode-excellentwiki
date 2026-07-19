---
title: "[Solution] IntelliJ IDEA Gradle sync failed"
description: "Fix IntelliJ IDEA Gradle sync failures. Resolve project import, dependency resolution, and Gradle wrapper issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "gradle", "build-system", "dependency-management"]
severity: "error"
---

# Gradle sync failed

## Error Message

```
Could not resolve all dependencies for configuration ':classpath'.
Gradle sync failed: Could not determine the dependencies of task ':compileJava'.
> Failed to notify project evaluation listener.
```

## Common Causes

- Gradle wrapper version incompatible with project configuration
- Network issues preventing dependency download
- Corrupted Gradle cache or wrapper distribution
- Incorrect JDK version configured for Gradle
- Proxy or firewall blocking Gradle repository access

## Solutions

### Solution 1: Invalidate Gradle Caches

Clear the Gradle cache and re-sync the project. Navigate to **File → Invalidate Caches → Invalidate and Restart**, then re-import the project.

```bash
# Manually clear Gradle caches:
rm -rf ~/.gradle/caches/
rm -rf .gradle/
rm -rf build/

# Re-generate Gradle wrapper:
gradle wrapper --gradle-version=8.5

# Then re-sync in IDE:
# File → Invalidate Caches and Restart
```

### Solution 2: Check Gradle Wrapper and JDK Configuration

Ensure the Gradle wrapper version and JDK are correctly configured for your project.

```bash
# Check current wrapper version:
cat gradle/wrapper/gradle-wrapper.properties

# Verify JDK installation:
java -version

# Set JAVA_HOME for Gradle:
export JAVA_HOME=/path/to/jdk-17

# Update wrapper to compatible version:
./gradlew wrapper --gradle-version=8.5
```

### Solution 3: Configure Proxy Settings for Gradle

If behind a corporate proxy, configure Gradle proxy settings in gradle.properties.

```properties
# gradle.properties (in project root or ~/.gradle/gradle.properties)
systemProp.http.proxyHost=proxy.company.com
systemProp.http.proxyPort=8080
systemProp.https.proxyHost=proxy.company.com
systemProp.https.proxyPort=8080
systemProp.http.nonProxyHosts=localhost|127.0.0.1
```

### Solution 4: Force Refresh Dependencies

Use the --refresh-dependencies flag to force Gradle to re-download all dependencies.

```bash
# From project root:
./gradlew build --refresh-dependencies

# Or in IDE:
# File → Settings → Build Tools → Gradle
# Check 'Always update snapshots'
# Then click 'Sync Gradle Project' (elephant icon)

# For offline mode issues, disable it:
# File → Settings → Build Tools → Gradle
# Uncheck 'Offline work'
```

## Prevention Tips

- Always use the Gradle wrapper rather than a system-installed Gradle
- Pin the Gradle wrapper version in gradle-wrapper.properties
- Configure the Gradle JDK in File → Settings → Build Tools → Gradle
- Use build scans (gradle build --scan) to diagnose complex dependency issues

## Related Errors

- [Maven Integration Error]({{< relref "/tools/intellij/maven-integration-error" >}})
- [Compilation Failed]({{< relref "/tools/intellij/compilation-error" >}})
- [Run Configuration Error]({{< relref "/tools/intellij/run-configuration-error" >}})
