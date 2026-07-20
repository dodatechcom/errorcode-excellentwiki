---
title: "[Solution] Jenkins Agent Disconnected During Build"
description: "Fix Jenkins agent disconnection during builds. Resolve agent connectivity drops and build failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Agent Disconnected During Build

Agent disconnection occurs when the agent loses connection to Jenkins master.

## Common Causes

- Network instability
- Agent JVM crashed
- Master restarted during builds

## How to Fix

```bash
java -jar agent.jar -url http://jenkins:8080 -secret @secret-file -name my-agent -failAfter 300 -retry 5
```

### Use WebSocket Transport

```bash
# Manage Jenkins > Manage Nodes > Agent > Inbound agents > WebSocket
```
