---
title: "[Solution] Jenkins Plugin Error"
description: "Fix Jenkins plugin errors. Resolve plugin installation, compatibility, and dependency issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "plugin", "installation", "compatibility", "dependency"]
weight: 5
---

# Jenkins Plugin Error

A plugin error occurs when a Jenkins plugin fails to install, load, or execute. The plugin may be incompatible with the current Jenkins version or have missing dependencies.

## Common Causes

- The plugin version is incompatible with the current Jenkins version
- Required plugin dependencies are missing
- The plugin failed to download from the update center
- A plugin update introduced breaking changes

## How to Fix

### Check Jenkins and Plugin Versions

```bash
# Jenkins version
java -jar jenkins-cli.jar version

# List installed plugins
java -jar jenkins-cli.jar list-plugins
```

### Install Plugin via CLI

```bash
java -jar jenkins-cli.jar install-plugin plugin-name:version
java -jar jenkins-cli.jar safe-restart
```

### Fix Plugin Dependencies

```
Jenkins > Manage Jenkins > Manage Plugins > Advanced
> Check for updates and install missing dependencies
```

### Pin Plugin Version in Docker

```dockerfile
FROM jenkins/jenkins:lts
RUN jenkins-plugin-cli --plugins workflow-aggregator git credentials-binding
```

### Reinstall Corrupted Plugin

```bash
rm -p $JENKINS_HOME/plugins/<plugin-name>*
# Restart Jenkins to trigger re-download
```

## Examples

```bash
# Plugin incompatible with Jenkins
# ERROR: This plugin requires Jenkins 2.400+ but you have 2.380
# Fix: update Jenkins or install an older plugin version

# Missing dependency
# ERROR:atrix-auth requires configuration-as-code
# Fix: install configuration-as-code plugin first
```

## Related Errors

- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax issue
- [Node Offline]({{< relref "/tools/jenkins/node-offline" >}}) — agent is not connected
