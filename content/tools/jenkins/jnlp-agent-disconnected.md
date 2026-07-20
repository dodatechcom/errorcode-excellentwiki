---
title: "[Solution] Jenkins JNLP Agent Disconnected"
description: "Fix Jenkins JNLP agent disconnection errors. Resolve inbound agent connectivity and stability issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins JNLP Agent Disconnected

JNLP agents connect to Jenkins via an outbound connection. Disconnections occur when the connection drops.

## How to Fix

```bash
java -jar agent.jar -url http://jenkins:8080 -secret @secret -name my-agent -retry 5
```

### Use WebSocket Transport

```bash
# Manage Jenkins > Manage Nodes > Agent > Enable WebSocket
```
