---
title: "[Solution] Docker Build Failed in Jenkins Pipeline"
description: "Fix Docker build failures in Jenkins pipeline. Resolve Dockerfile errors and image build issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Docker Build Failed in Jenkins Pipeline

Docker build failures occur when `docker build` cannot create the image from the Dockerfile.

## Common Causes

- Dockerfile syntax errors
- Base image not found
- Docker daemon not running
- Out of disk space

## How to Fix

```groovy
pipeline {
    agent { label 'docker' }
    stages {
        stage('Build Image') {
            steps { sh 'docker build -t myapp:${BUILD_NUMBER} .' }
        }
    }
}
```

```bash
docker system prune -f
```
