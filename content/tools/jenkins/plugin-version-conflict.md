---
title: "[Solution] Jenkins Plugin Version Conflict"
description: "Fix Jenkins plugin version conflict errors. Resolve incompatible plugin version and dependency issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Plugin Version Conflict

Plugin version conflicts occur when installed plugins have incompatible version requirements.

## How to Fix

```bash
# Manage Jenkins > Plugins > Updates > Update all plugins
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins --output txt
```
