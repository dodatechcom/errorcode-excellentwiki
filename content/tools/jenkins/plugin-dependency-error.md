---
title: "[Solution] Jenkins Plugin Dependency Error"
description: "Fix Jenkins plugin dependency errors. Resolve missing or incompatible plugin dependencies."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Plugin Dependency Error

Plugin dependency errors occur when a plugin cannot find required dependencies.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install the plugin (auto-installs deps)
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins --output txt | grep "Missing"
```
