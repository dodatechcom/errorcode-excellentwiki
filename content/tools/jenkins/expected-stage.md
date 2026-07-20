---
title: "[Solution] Expected 'stage' Block in Jenkinsfile"
description: "Fix 'expected stage' parsing errors in Jenkins declarative pipelines. Resolve Jenkinsfile structure issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Expected 'stage' Block in Jenkinsfile

The `expected 'stage'` error means Jenkins declarative pipeline parser encountered an element where it expected a `stage` block inside the `stages` section.

## Common Causes

- Placing non-stage content directly inside `stages { }` without wrapping in a `stage { }`
- Using scripted pipeline syntax inside a declarative pipeline
- Incorrect nesting levels in the Jenkinsfile
- Extra or missing braces causing misaligned blocks

## How to Fix

### Wrap All Blocks in Stage

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make'
            }
        }
    }
}
```

### Use the Pipeline Linter

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ declarative-linter < Jenkinsfile
```

## Examples

```groovy
pipeline {
    agent any
    stages {
        stage('Parallel') {
            parallel {
                stage('A') { steps { sh 'echo A' } }
                stage('B') { steps { sh 'echo B' } }
            }
        }
    }
}
```
