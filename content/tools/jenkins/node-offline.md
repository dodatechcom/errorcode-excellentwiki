---
title: "[Solution] Jenkins Node Offline Error"
description: "Fix Jenkins node offline errors. Resolve agent connectivity and availability issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Node Offline Error

A node goes offline when Jenkins cannot communicate with the agent.

## Common Causes

- Agent machine is down
- JNLP agent lost connection
- SSH connection timed out
- Agent JVM crashed

## How to Fix

```bash
# Jenkins > Manage Jenkins > Manage Nodes > Click node > "Reconnect"
```

```bash
java -jar agent.jar -url http://jenkins:8080 -secret @secret-file -name my-agent -retry 3
```
