---
title: "Jenkins Pipeline Error"
description: "Jenkins pipeline has syntax errors or fails during pipeline execution."
tools: ["jenkins"]
error-types: ["build-error"]
severities: ["error"]
tags: ["jenkins", "pipeline", "declarative", "scripted", "jenkinsfile"]
weight: 5
---

# Jenkins Pipeline Error

A Jenkins pipeline error occurs when the Jenkinsfile has syntax errors or the pipeline fails during execution. This can happen in both declarative and scripted pipeline syntax.

## Common Causes

- Jenkinsfile syntax errors
- Missing pipeline plugin
- Invalid Groovy syntax in scripted sections
- Stage or step configuration errors

## How to Fix

### Validate Jenkinsfile Syntax

```bash
# Use Jenkins CLI to validate
java -jar jenkins-cli.jar -s http://localhost:8080/ \
  declarative-linter < Jenkinsfile
```

### Check Declarative Pipeline Syntax

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make build'
            }
        }
        stage('Test') {
            steps {
                sh 'make test'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
```

### Fix Scripted Pipeline Issues

```groovy
node {
    stage('Build') {
        try {
            sh 'make build'
        } catch (Exception e) {
            echo "Build failed: ${e.message}"
            currentBuild.result = 'FAILURE'
        }
    }
}
```

### Check for Missing Plugins

```bash
# Ensure Pipeline plugin is installed
# Manage Jenkins > Plugins > Pipeline
```

### Debug Pipeline Execution

```groovy
stage('Debug') {
    steps {
        script {
            echo "Build URL: ${env.BUILD_URL}"
            echo "Node: ${env.NODE_NAME}"
        }
    }
}
```

## Examples

```text
WorkflowScript: 5: Expected a stage @ line 5, column 5.
   stage('Build') {
   ^

WorkflowScript: 8: Unknown stage section 'steps' @ line 8, column 9.
```

## Related Errors

- [Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — build failure
- [Plugin Error]({{< relref "/tools/jenkins/jenkins-plugin-error" >}}) — plugin issues
- [Groovy Error]({{< relref "/tools/jenkins/jenkins-groovy-error" >}}) — Groovy script error
