---
title: "[Solution] Jenkins Plugin Failed to Load"
description: "Fix Jenkins plugin failed to load errors. Resolve plugin initialization and startup issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Plugin Failed to Load

Plugins fail to load during Jenkins startup when they encounter errors during initialization.

## How to Fix

```bash
# Manage Jenkins > System Log
# Or: $JENKINS_HOME/logs/
```

```bash
mkdir -p $JENKINS_HOME/plugins.disabled
mv $JENKINS_HOME/plugins/my-plugin.jpi $JENKINS_HOME/plugins.disabled/
```
