---
title: "[Solution] Git Fetch Failed in Jenkins Pipeline"
description: "Fix git fetch failed errors in Jenkins pipeline. Resolve Git SCM fetch failures and authentication issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Git Fetch Failed in Jenkins Pipeline

A `git fetch failed` error occurs when Jenkins cannot retrieve the latest changes from the remote Git repository.

## Common Causes

- Invalid or expired credentials for the Git remote
- Repository URL is incorrect or moved
- SSH key not added to the agent
- Network firewall blocking outbound connections
- SSL certificate validation failure

## How to Fix

```groovy
checkout([
    $class: 'GitSCM',
    branches: [[name: 'main']],
    userRemoteConfigs: [[
        url: 'https://github.com/org/repo.git',
        credentialsId: 'github-ssh-key'
    ]]
])
```

```bash
mkdir -p ~/.ssh
ssh-keyscan github.com >> ~/.ssh/known_hosts
```

```groovy
withCredentials([sshUserPrivateKey(credentialsId: 'github-ssh-key', keyFileVariable: 'SSH_KEY')]) {
    sh 'GIT_SSH_COMMAND="ssh -i $SSH_KEY" git fetch origin main'
}
```
