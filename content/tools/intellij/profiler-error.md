---
title: "[Solution] IntelliJ IDEA Profiler error"
description: "Fix IntelliJ IDEA profiler failures. Resolve CPU profiling, memory allocation analysis, and profiler attachment errors."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "profiler", "performance-analysis", "cpu-profiling", "memory-profiling"]
severity: "error"
---

# Profiler error

## Error Message

```
Profiler error
Profiler failed to attach to process: access denied
CPU profiling failed: JVMTI agent initialization error
Memory allocation profiling: unsupported JDK version
Profiler timeout: data collection exceeded maximum duration
Unable to start profiling: required JDK not configured
```

## Common Causes

- Profiler agent cannot attach due to JVM security restrictions
- JDK version does not support the profiling features required
- Target application is running with a different JDK than the profiler
- Insufficient permissions to profile the target process
- Memory profiling requires specific JVM flags that are not enabled

## Solutions

### Solution 1: Configure JDK for Profiling

Ensure the correct JDK is configured for profiling. The profiler requires a compatible JDK installation.

```
# Check JDK version for profiling:
# Help → About → JRE version

# For profiling, use a JDK (not JRE):
# File → Project Structure → SDKs
#   Add JDK path (not JRE path)

# For memory profiling, add JVM flags:
# Run → Edit Configurations → VM options:
-XX:+UnlockDiagnosticVMOptions
-XX:+DebugNonSafepoints

# For CPU profiling with sampling:
# The profiler uses JVMTI, which requires JDK
# Ensure -XX:+UseJvmti is not disabled
```

### Solution 2: Attach Profiler to Running Application

Attach the profiler to an already running application for on-demand profiling.

```
# Start application with profiling support:
# Run → Profile 'Application' (not Run)

# Or attach to running process:
# 1. Run → Profile → 'Attach to Process'
# 2. Select the target JVM process
# 3. Choose profiling mode:
#    - CPU Sampling (low overhead)
#    - CPU Tracing (high detail, high overhead)
#    - Allocations (memory allocation tracking)

# Start profiling from IDE:
# View → Tool Windows → Profiler
# Click 'Start CPU Profiling' or 'Start Allocation Profiling'
```

### Solution 3: Fix Profiler Permission Issues

Resolve permission issues when the profiler cannot attach to the target process.

```bash
# On Linux, allow profiling non-root processes:
# Check ptrace settings:
cat /proc/sys/kernel/yama/ptrace_scope
# If 1, profiling is restricted

# Temporarily allow profiling:
sudo sysctl kernel.yama.ptrace_scope=0

# Or run the IDE as root (not recommended for daily use):
sudo ./idea.sh

# For profiling your own application, add JVM args:
java -Dcom.sun.management.jmxremote \
     -Dcom.sun.management.jmxremote.port=9090 \
     -jar your-app.jar

# Then use JMX connection in profiler
```

### Solution 4: View and Analyze Profiler Results

Navigate and interpret profiler results to identify performance bottlenecks.

```
# After profiling, results appear in:
# View → Tool Windows → Profiler

# CPU Profiling:
#   - Flame Graph view: shows call stack hot spots
#   - Tree view: hierarchical method call times
#   - Table view: sortable method metrics

# Memory Allocation:
#   - Allocation Hotspots: methods allocating most memory
#   - Allocation Call Tree: allocation call paths

# Export profiler results:
#   Right-click results → 'Export Snapshot'
#   Save as .json for team sharing

# Compare profiling sessions:
#   Profiler → Compare Snapshots → Select two sessions
```

## Prevention Tips

- Use CPU Sampling mode first for low-overhead profiling, switch to Tracing for details
- Profile on a staging environment that mirrors production for accurate results
- Save profiling snapshots for historical comparison after code changes
- Use Flame Graph view to quickly identify the hottest code paths

## Related Errors

- [Memory/Heap Error]({{< relref "/tools/intellij/memory-heap-error" >}})
- [Debug Error]({{< relref "/tools/intellij/debug-error" >}})
- [Run Configuration Error]({{< relref "/tools/intellij/run-configuration-error" >}})
