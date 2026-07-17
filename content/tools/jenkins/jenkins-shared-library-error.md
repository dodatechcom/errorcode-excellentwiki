---
title: "Jenkins Shared Library Error"
description: "Jenkins pipeline fails to load or execute shared library code."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

# Jenkins Shared Library Error

A Jenkins shared library error occurs when the pipeline cannot load or execute code from a shared library. Shared libraries allow code reuse across multiple Jenkins pipelines.

## Common Causes

- Shared library not configured in Jenkins
- Library repository URL incorrect
- Library version mismatch
- Missing or incorrect library structure
- Groovy compilation errors in library code

## How to Fix

### Configure Shared Library

Go to **Manage Jenkins > Configure System > Global Pipeline Libraries**:
- Add library name, default version, and repository URL

### Use @Library Annotation

```groovy
@Library('my-shared-library') _

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                myCustomStep()
            }
        }
    }
}
```

### Verify Library Structure

```
my-shared-library/
├── vars/
│   ├── myCustomStep.groovy
│   └── myGlobalVar.groovy
├── src/
│   └── com/example/
│       └── MyClass.groovy
└── resources/
    └── templates/
```

### Fix Library Loading

```groovy
// Load specific version
@Library('my-shared-library@main') _

// Load multiple libraries
@Library(['lib1', 'lib2']) _
```

### Debug Library Issues

```groovy
stage('Debug') {
    steps {
        script {
            echo "Library loaded: ${myGlobalVar}"
        }
    }
}
```

### Check Library Repository Access

```bash
git ls-remote https://github.com/owner/my-shared-library.git
```

## Examples

```text
org.jenkinsci.plugins.workflow.cps.CpsCompilationException:
Could not resolve class for: myCustomStep
```

## Related Errors

- [Groovy Error]({{< relref "/tools/jenkins/jenkins-groovy-error" >}}) — Groovy syntax error
- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax error
- [Credential Error]({{< relref "/tools/jenkins/credential-error2" >}}) — credential issues
