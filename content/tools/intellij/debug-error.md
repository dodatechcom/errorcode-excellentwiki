---
title: "[Solution] IntelliJ IDEA Debug session error"
description: "Fix IntelliJ IDEA debug session failures. Resolve JDWP connection errors, breakpoint issues, and debugger configuration problems."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "intellij"
tags: ["intellij", "ide", "debugging", "jdwp", "breakpoints", "jvm"]
severity: "error"
---

# Debug session error

## Error Message

```
Debug session error
Failed to connect to debugger: Connection refused
Unable to open debugger port: localhost:53539
JDWP Transport dt_socket failed to initialize
Transport error: Timeout connecting to debugger
Error: Debugger failed to attach to process
```

## Common Causes

- JDWP port is already in use by another debug session
- Firewall blocking the debugger transport port
- Application exited before debugger could attach
- JVM debug flags are not configured correctly
- Remote debug host/port mismatch in configuration

## Solutions

### Solution 1: Configure JVM Debug Agent

Ensure the JVM is started with the correct debug agent flags for remote debugging.

```bash
# For remote debugging, start your application with:
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 \
     -jar your-application.jar

# For suspend=y, the app will wait for debugger to attach
# For suspend=n, the app starts immediately

# Or use the older syntax:
java -Xdebug -Xrunjdwp:transport=dt_socket,server=y,address=*:5005 \
     -jar your-application.jar
```

### Solution 2: Kill Stale Debug Processes

Terminate any leftover debug processes that may be holding the debug port.

```bash
# Find processes using the debug port:
lsof -i :5005
# or
netstat -tlnp | grep 5005

# Kill the specific process:
kill -9 <PID>

# Or kill all Java debug processes:
jps -l | grep "YourApp"
kill -9 <PID>

# Check for zombie debug sessions:
ps aux | grep jdwp
```

### Solution 3: Configure Remote Debug in IDE

Create or update the remote debug configuration in IntelliJ IDEA.

```
Run → Edit Configurations → '+' → Remote JVM Debug
# Host: localhost (or remote server IP)
# Port: 5005 (must match the JVM debug port)
# Use module classpath: Select your application module

# Advanced options:
#   Transport: Default (dt_socket)
#   Auto-detect shared memory transport: Checked

# For Docker debugging:
# Host: localhost
# Port: Map from container (e.g., 5005)
# Ensure container exposes debug port
```

### Solution 4: Fix Breakpoint Configuration

Verify and fix breakpoint settings that may be preventing the debugger from stopping.

```
# View → Tool Windows → Breakpoints
# Review all breakpoints:
#   - Ensure condition expressions are valid Java
#   - Check 'Enabled' checkbox
#   - Verify 'Suspend' is set appropriately

# For method breakpoints:
#   Use 'Ctrl+Shift+F8' (View Breakpoints)
#   Verify method signature matches exactly

# For exception breakpoints:
#   Add specific exception class
#   Check 'Caught exception' and 'Uncaught exception'

# Clear all breakpoints:
# Run → Stop (Ctrl+F2) → then Ctrl+Shift+F8 → Remove All
```

## Prevention Tips

- Use conditional breakpoints to avoid stopping on every iteration in loops
- Enable 'Mute Breakpoints' to temporarily disable all breakpoints without removing them
- Use Evaluate Expression (Alt+F8) to inspect and modify variables during debugging
- Configure 'HotSwap' settings in Settings → Build → Compiler for live code changes

## Related Errors

- [Run Configuration Error]({{< relref "/tools/intellij/run-configuration-error" >}})
- [Terminal Error]({{< relref "/tools/intellij/terminal-error" >}})
- [Test Error]({{< relref "/tools/intellij/test-error" >}})
