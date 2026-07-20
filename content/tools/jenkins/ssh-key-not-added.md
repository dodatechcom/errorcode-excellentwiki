---
title: "[Solution] Jenkins SSH Key Not Added Error"
description: "Fix Jenkins SSH key not added errors. Resolve SSH credential configuration and access issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins SSH Key Not Added Error

SSH key errors occur when Jenkins tries to use an SSH key that is not properly configured.

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Kind: SSH Username with private key
```

```groovy
withCredentials([sshUserPrivateKey(credentialsId: 'deploy-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
    sh 'ssh -i $SSH_KEY -o StrictHostKeyChecking=no $SSH_USER@server.example.com "ls"'
}
```
