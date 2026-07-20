---
title: "[Solution] Missing 'agent any' in Jenkins Pipeline"
description: "Fix missing agent declaration in Jenkins declarative pipeline. Resolve pipeline without agent directive."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Missing 'agent any' in Jenkins Pipeline

A declarative pipeline requires an `agent` directive either at the top level or per-stage. Without it, Jenkins does not know where to execute the pipeline.

## Common Causes

- Omitted the `agent` directive entirely from the `pipeline` block
- Forgot to add `agent` to individual stages
- Mixed scripted and declarative syntax

## How to Fix

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps { sh 'make build' }
        }
    }
}
```

### Use Per-Stage Agent

```groovy
pipeline {
    stages {
        stage('Build') {
            agent { label 'linux' }
            steps { sh 'make build' }
        }
    }
}
```
