---
title: "[Solution] Jenkins Plugin Missing Error"
description: "Fix Jenkins missing plugin errors. Resolve plugin installation and dependency issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Plugin Missing Error

Jenkins plugins provide additional functionality. When a required plugin is missing, pipeline steps become unavailable.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install required plugin
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin workflow-aggregator
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins | grep "workflow"
```
