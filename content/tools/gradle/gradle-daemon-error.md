---
title: "Gradle Daemon Error"
description: "Gradle daemon process fails to start or crashes during build execution."
tools: ["gradle"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Gradle Daemon Error

The Gradle daemon is a long-running background process that speeds up builds by caching build state. A daemon error means the daemon failed to start, became unresponsive, or crashed during execution.

## Common Causes

- Daemon process ran out of memory
- Corrupted daemon registry or cache
- Port conflict with another Gradle daemon
- JVM compatibility issues with the daemon

## How to Fix

### Stop All Daemons

```bash
./gradlew --stop
```

### Run Without Daemon

```bash
./gradlew build --no-daemon
```

### Delete Daemon Registry

```bash
rm -rf ~/.gradle/daemon/
```

### Check Daemon Logs

```bash
ls ~/.gradle/daemon/
cat ~/.gradle/daemon/*/daemon-*.out.log
```

### Configure Daemon Memory

```properties
# gradle.properties
org.gradle.daemon=true
org.gradle.jvmargs=-Xmx2g -XX:MaxMetaspaceSize=256m
```

### Check for Port Conflicts

```bash
lsof -i :6043
# Default Gradle daemon port is 6043
```

## Examples

```bash
./gradlew build
# Daemon could not be started, or connection timed out

# Solution:
./gradlew --stop
rm -rf ~/.gradle/daemon/
./gradlew build
```

## Related Errors

- [Out of Memory]({{< relref "/tools/gradle/out-of-memory" >}}) — daemon OOM crash
- [Cache Error]({{< relref "/tools/gradle/cache-error3" >}}) — corrupted daemon cache
