---
title: "[Solution] Eclipse Debug error"
description: "Debug error"
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "eclipse"
tags: ["eclipse", "ide", "debug", "breakpoint", "jvm", "jdwp"]
severity: "error"
---

# Debug error

## Error Message

```
Failed to connect to remote VM. Connection refused. Could not open debug connection: JDWP transport library could not be loaded.
```

## Common Causes

- The target JVM was not started with the JDWP agent for remote debugging.
- A firewall or network configuration is blocking the debug port (default 5005).
- The debug port is already in use by another debugging session.

## Solutions

### Solution 1: Enable Remote Debugging on the JVM

Start the target Java application with JDWP debugging enabled. For local debugging, Eclipse automatically adds the necessary JVM arguments. For remote debugging, configure the run configuration or command line with the JDWP transport arguments.

```java
# Enable remote debugging on JVM
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005 \
  -jar application.jar

# For older Java versions (< 9)
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005 \
  -jar application.jar
```

### Solution 2: Configure Remote Debug in Eclipse

Go to **Run > Debug Configurations > Remote Java Application** and create a new configuration. Set the host and port to match the target JVM. Click **Debug** to establish the connection. Ensure the source code in Eclipse matches the version running on the remote JVM.

```bash
# Check if debug port is in use
netstat -tlnp | grep 5005

# Test connectivity to remote debug port
telnet remote-host 5005
```

## Prevention Tips

- Use **Run > Debug (F11)** instead of Run to automatically attach the debugger.
- Set conditional breakpoints by right-clicking a breakpoint and entering a Java expression.
- Use the **Debug** view to inspect thread states and call stacks during debugging.

## Related Errors

- [run-configuration-error]({{< relref "/tools/eclipse/run-configuration-error" >}})
- [console-error]({{< relref "/tools/eclipse/console-error" >}})
- [test-error]({{< relref "/tools/eclipse/test-error" >}})
