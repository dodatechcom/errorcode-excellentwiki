---
title: "[Solution] Jenkins Parameterized Build Error"
description: "Fix Jenkins parameterized build errors. Resolve parameter definition and value issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Parameterized Build Error

Parameterized builds allow passing values to jobs at build time.

## How to Fix

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: '1.0.0', description: 'App version')
        choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: 'Target env')
        booleanParam(name: 'SKIP_TESTS', defaultValue: false)
    }
    stages {
        stage('Build') {
            steps {
                echo "Building ${params.VERSION} for ${params.ENV}"
                sh "make VERSION=${params.VERSION} ENV=${params.ENV}"
            }
        }
    }
}
```
