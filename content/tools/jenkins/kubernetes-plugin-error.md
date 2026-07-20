---
title: "[Solution] Jenkins Kubernetes Plugin Error"
description: "Fix Jenkins Kubernetes plugin errors. Resolve Kubernetes agent provisioning and pod template issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Kubernetes Plugin Error

The Kubernetes plugin allows Jenkins to dynamically provision agents as pods.

## How to Fix

```bash
# Manage Jenkins > Manage Clouds > Add cloud > Kubernetes
# Kubernetes URL: https://kubernetes.default.svc
```

```groovy
pipeline {
    agent {
        kubernetes {
            yaml '''
                apiVersion: v1
                kind: Pod
                spec:
                  containers:
                  - name: maven
                    image: maven:3.9-jdk-17
                    command: ['sleep']
                    args: ['infinity']
            '''
        }
    }
    stages {
        stage('Build') {
            steps {
                container('maven') { sh 'mvn clean package -B' }
            }
        }
    }
}
```
