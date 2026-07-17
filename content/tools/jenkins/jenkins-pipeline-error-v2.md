---
title: "Jenkins Pipeline DSL Error"
description: "Jenkins pipeline DSL syntax error in Jenkinsfile."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "pipeline", "dsl", "jenkinsfile", "syntax"]
weight: 5
---

# Jenkins Pipeline — DSL Error

This error occurs when a Jenkins pipeline DSL syntax is invalid. The Jenkinsfile contains syntax errors or uses incorrect step names that prevent the pipeline from parsing.

## Common Causes

- Incorrect Groovy syntax in Jenkinsfile
- Undefined pipeline step (missing plugin)
- Missing required DSL parameters
- Unbalanced braces or parentheses
- Incorrect stage/step nesting

## How to Fix

### Validate Jenkinsfile Syntax

```groovy
// Check for balanced braces
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello"'
            }
        }
    }
}
```

### Use Declarative Pipeline

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
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

### Fix Scripted Pipeline Syntax

```groovy
node {
    stage('Checkout') {
        checkout scm
    }
    stage('Build') {
        sh 'make build'
    }
}
```

### Check for Missing Plugins

```groovy
// Ensure required plugins are installed
// pipeline-aggregator, git, workflow-basic-steps
```

### Use Jenkins Pipeline Linter

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"jenkinsfile": "..."}' \
  http://localhost:8080/pipeline-model-converter/validate
```

## Examples

```text
WorkflowScript: 15: Unexpected token '}' @ line 15, column 1.
   1 error(s) in pipeline script.
```

## Related Errors

- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Groovy Error]({{< relref "/tools/jenkins/jenkins-groovy-error" >}}) — Groovy script error
- [Jenkins Shared Library Error]({{< relref "/tools/jenkins/jenkins-shared-library-error" >}}) — shared library load error
