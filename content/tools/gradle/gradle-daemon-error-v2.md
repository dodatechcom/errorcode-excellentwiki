---
title: "Gradle Daemon Connection Lost"
description: "Gradle daemon process disconnects or becomes unresponsive during build."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Daemon Connection Lost

This error occurs when the Gradle daemon process crashes, becomes unresponsive, or loses its connection to the build client. The daemon is a long-lived background process that speeds up builds, but it can fail due to memory or compatibility issues.

## Common Causes

- Daemon JVM crashed due to out of memory
- Daemon became unresponsive due to long GC pauses
- Version mismatch between client and daemon
- Daemon killed by operating system (OOM killer)
- Stale daemon process from previous build

## How to Fix

### Stop All Daemons

```bash
./gradlew --stop
```

### Disable Daemon for Current Build

```bash
./gradlew build --no-daemon
```

### Configure Daemon Idle Timeout

```properties
# gradle.properties
org.gradle.daemon.idletimeout=3600000
```

### Set Daemon JVM Arguments

```properties
# gradle.properties
org.gradle.jvmargs=-Xmx4g -XX:MaxMetaspaceSize=512m -XX:+HeapDumpOnOutOfMemoryError
```

### Disable Daemon Globally

```properties
# gradle.properties
org.gradle.daemon=false
```

### Use Daemon Health Check

```bash
./gradlew --status
```

## Examples

```text
* What went wrong:
  Gradle daemon disconnected.
  This may be caused by one of the contributing factors described at
  https://docs.gradle.org/8.0/userguide/troubleshooting.html

DaemonJvmParameters: -Xmx2g
```

## Related Errors

- [Gradle Out of Memory]({{< relref "/tools/gradle/gradle-out-of-memory" >}}) — daemon OOM crash
- [Gradle Version Error]({{< relref "/tools/gradle/gradle-version-error" >}}) — version compatibility issues
- [Gradle Build Failed]({{< relref "/tools/gradle/gradle-build-failed" >}}) — general build failure
