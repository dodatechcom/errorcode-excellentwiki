---
title: "[Solution] Jenkins Docker Agent Failed"
description: "Fix Jenkins Docker agent failures. Resolve Docker agent container creation and connectivity issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Docker Agent Failed

Docker agent failures occur when Jenkins cannot create or connect to a Docker container agent.

## How to Fix

```bash
docker info
docker ps
sudo usermod -aG docker jenkins
```

```groovy
pipeline {
    agent { docker { image 'maven:3.9-jdk-17'; args '-v $HOME/.m2:/root/.m2 --memory 2g' } }
    stages { stage('Build') { steps { sh 'mvn clean package -B' } } }
}
```
