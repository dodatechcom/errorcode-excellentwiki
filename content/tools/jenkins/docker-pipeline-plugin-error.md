---
title: "[Solution] Jenkins Docker Pipeline Plugin Error"
description: "Fix Jenkins Docker Pipeline plugin errors. Resolve docker-workflow plugin configuration issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Docker Pipeline Plugin Error

The Docker Pipeline plugin allows using Docker agents in pipelines.

## How to Fix

```bash
# Manage Jenkins > Plugins > Available > Install "Docker Pipeline"
docker --version
sudo usermod -aG docker jenkins
```

```groovy
pipeline {
    agent { docker { image 'maven:3.9-jdk-17' } }
    stages {
        stage('Build') { steps { sh 'mvn clean package -B' } }
    }
}
```
