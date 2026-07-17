---
title: "Jenkins Shared Library Load Error"
description: "Jenkins pipeline fails to load a shared library."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Shared Library — Load Error

This error occurs when a Jenkins pipeline fails to load a shared library. The library may not be configured globally, the path may be incorrect, or the branch may not exist.

## Common Causes

- Shared library not configured in Jenkins
- Library path or branch name is incorrect
- Library repository not accessible
- Function or class not found in library
- Version mismatch

## How to Fix

### Configure Shared Library

Go to **Manage Jenkins > Configure System > Global Pipeline Libraries**

```groovy
// Add library configuration
Name: my-shared-lib
Default version: main
Include @Library in classpath: checked
```

### Import Library in Jenkinsfile

```groovy
@Library('my-shared-lib') _

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    myCustomStep()
                }
            }
        }
    }
}
```

### Use Specific Version

```groovy
@Library('my-shared-lib@v1.2') _
```

### Use Library in Scripted Pipeline

```groovy
@Library('my-shared-lib') import com.example.Utils

node {
    Utils.cleanWorkspace()
}
```

### Debug Library Loading

```groovy
// Check if library is loaded
println this.class.classLoader.classPath
```

## Examples

```text
org.jenkinsci.plugins.workflow.cps.CpsCompilationErrorsException:
  startup failed:
  No such property: myCustomStep for class: WorkflowScript
```

## Related Errors

- [Jenkins Pipeline Error]({{< relref "/tools/jenkins/jenkins-pipeline-error" >}}) — pipeline syntax error
- [Jenkins Groovy Error]({{< relref "/tools/jenkins/jenkins-groovy-error" >}}) — Groovy script error
- [Jenkins Plugin Error]({{< relref "/tools/jenkins/jenkins-plugin-error" >}}) — plugin issues
