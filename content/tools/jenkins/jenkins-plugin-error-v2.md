---
title: "Jenkins Plugin Compatibility Error"
description: "Jenkins plugin has compatibility issues with the Jenkins version."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "plugin", "compatibility", "version", "update"]
weight: 5
---

# Jenkins Plugin — Compatibility Error

This error occurs when a Jenkins plugin is incompatible with the installed Jenkins version or has conflicting dependencies with other plugins.

## Common Causes

- Plugin version not compatible with Jenkins core
- Plugin dependencies not satisfied
- Plugin requires newer Jenkins version
- Conflicting plugin versions installed

## How to Fix

### Check Plugin Compatibility

Go to **Manage Jenkins > Plugins > Available plugins** and check compatibility.

### Update Jenkins Core

```bash
sudo apt-get update
sudo apt-get install jenkins
```

### Update Plugin

Go to **Manage Jenkins > Plugins > Updates** and install available updates.

### Check Plugin Dependencies

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-plugins
```

### Install Specific Plugin Version

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ \
  install-plugin workflow-aggregator:2.26
```

### Pin Plugin Version

```groovy
// In init.groovy.d or CasC
def plugins = ['workflow-aggregator', 'git', 'pipeline-stage-view']
plugins.each { plugin ->
    if (!instance.pluginManager.getPlugin(plugin)) {
        instance.pluginManager.installPlugin(plugin)
    }
}
```

## Examples

```text
Failed to install plugin: workflow-aggregator@2.26
  This plugin requires Jenkins 2.387.1 or later
```

## Related Errors

- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Pipeline Error]({{< relref "/tools/jenkins/jenkins-pipeline-error" >}}) — pipeline syntax error
- [Jenkins Master Error]({{< relref "/tools/jenkins/jenkins-master-error" >}}) — controller issues
