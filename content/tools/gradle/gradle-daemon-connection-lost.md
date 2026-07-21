---
title: "Gradle Daemon Connection Lost"
description: "Gradle daemon process lost its connection during build execution, causing the build to fail with an unexpected disconnect error."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Gradle Daemon Connection Lost

The Gradle daemon is a long-lived background process that speeds up builds. A connection lost error means the client lost communication with the daemon, typically due to memory exhaustion or process termination.

## Common Causes

- The daemon process ran out of memory and was killed by the OS
- A system update or restart terminated the daemon process
- The daemon JVM crashed due to a native library issue
- The build consumed more memory than allocated to the daemon

## How to Fix

1. Stop all running daemons and restart:

```bash
./gradlew --stop
```

2. Increase daemon JVM memory:

```bash
# In gradle.properties
org.gradle.jvmargs=-Xmx4g -XX:+UseParallelGC
```

3. Check system logs for OOM killer activity:

```bash
dmesg | grep -i "oom\|killed"
```

4. Run the build without the daemon to isolate the issue:

```bash
./gradlew build --no-daemon
```

## Examples

```bash
# Error output
Daemon connection lost: The client has disconnected from the daemon.
  The build has been abandoned.
```

```properties
# gradle.properties -- daemon configuration
org.gradle.jvmargs=-Xmx4g -XX:+HeapDumpOnOutOfMemoryError
org.gradle.daemon=true
org.gradle.daemon.idletoutout=10800000
```

## Related Errors

- [Daemon Error]({{< relref "/tools/gradle/gradle-daemon-error" >}}) -- general daemon failures
- [Daemon Memory Exhausted]({{< relref "/tools/gradle/gradle-daemon-memory-exhausted" >}}) -- daemon OOM issues
