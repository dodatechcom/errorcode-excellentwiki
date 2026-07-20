---
title: "[Solution] Jenkins Node Not Found"
description: "Fix Jenkins node not found errors. Resolve agent node registration and availability issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Node Not Found

Jenkins cannot find the specified node.

## How to Fix

```bash
# Jenkins > Manage Jenkins > Manage Nodes
java -jar agent.jar -url http://jenkins:8080 -secret @secret-file -name my-node
```
