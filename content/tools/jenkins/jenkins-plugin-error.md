---
title: "Jenkins Plugin Error"
description: "Jenkins plugin fails to install, load, or execute during build."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Plugin Error

A Jenkins plugin error occurs when a plugin fails to install, load, or execute. This can prevent pipeline steps from running or cause the Jenkins UI to malfunction.

## Common Causes

- Plugin version incompatible with Jenkins version
- Plugin dependencies missing
- Plugin configuration errors
- Corrupted plugin installation

## How to Fix

### Check Plugin Compatibility

Go to **Manage Jenkins > Plugins > Available** and verify compatibility.

### Update Plugin

```bash
# Via Jenkins CLI
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin plugin-name:latest
```

### Check Plugin Dependencies

```bash
# View plugin dependencies
cat /var/lib/jenkins/plugins/plugin-name/META-INF/MANIFEST.MF
```

### Reinstall Plugin

```bash
# Remove plugin directory
rm -rf /var/lib/jenkins/plugins/plugin-name*
# Restart Jenkins
systemctl restart jenkins
# Reinstall from UI
```

### Check Jenkins Logs

```bash
tail -f /var/log/jenkins/jenkins.log
# Look for plugin-related errors
```

### Fix Pipeline Plugin Usage

```groovy
// Ensure pipeline plugins are installed
@Library('my-shared-library') _

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
    }
}
```

## Examples

```text
SEVERE: Failed to install plugin: pipeline-model-definition
java.io.IOException: Dependencies missing for plugin pipeline-model-definition
```

## Related Errors

- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax error
- [Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — build failure
