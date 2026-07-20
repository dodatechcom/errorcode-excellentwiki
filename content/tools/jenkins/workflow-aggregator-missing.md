---
title: "[Solution] Jenkins Workflow Aggregator Plugin Missing"
description: "Fix Jenkins workflow-aggregator plugin missing error. Resolve pipeline plugin installation issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Workflow Aggregator Plugin Missing

The `workflow-aggregator` plugin is the core plugin for Jenkins Pipeline.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Pipeline: Aggregator"
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin workflow-aggregator workflow-step-api workflow-cps
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```
