---
title: "[Solution] Jenkins Credential Not Found"
description: "Fix Jenkins credential not found errors. Resolve credential ID and scope configuration issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "credentials", "not-found", "secret", "scope"]
weight: 5
---

# Jenkins Credential Not Found

A credential not found error occurs when a pipeline step references a credential ID that does not exist in Jenkins' credential store, or the credential scope does not match.

## Common Causes

- The credential ID is misspelled in the Jenkinsfile
- The credential was deleted or not yet created
- The credential is in a different folder scope than the pipeline
- The credential type does not match what the step expects

## How to Fix

### Verify Credential Exists

```
Jenkins > Manage Jenkins > Credentials > System > Global credentials
```

### Reference Credentials Correctly

```groovy
// Username/Password
withCredentials([usernamePassword(
    credentialsId: 'my-credentials',
    usernameVariable: 'USER',
    passwordVariable: 'PASS'
)]) {
    sh 'echo $USER $PASS'
}

// SSH Key
withCredentials([sshUserPrivateKey(
    credentialsId: 'ssh-key',
    keyFileVariable: 'SSH_KEY',
    usernameVariable: 'USER'
)]) {
    sh 'ssh -i $SSH_KEY $USER@server'
}

// Secret Text
withCredentials([string(
    credentialsId: 'api-token',
    variable: 'TOKEN'
)]) {
    sh 'curl -H "Authorization: $TOKEN" https://api.example.com'
}
```

### Check Folder Scope

```
# Credentials in folder "my-folder" are only accessible from
# pipelines in that folder, or use the "Global" scope
```

### List Available Credentials via API

```bash
curl -u admin:token "http://jenkins/api/json?tree=credentials[id,type]"
```

## Examples

```groovy
// Wrong credential ID
withCredentials([string(credentialsId: 'API_TOKEN', variable: 'TOKEN')]) {
// ERROR: Credentials 'API_TOKEN' not found
// Fix: check the exact ID — it's case sensitive
}

// Credential in wrong scope
// Deploy pipeline in /job/prod/ can't see credential in /job/staging/
// Fix: move credential to Global scope or create it in the correct folder
```

## Related Errors

- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax issue
- [Plugin Error]({{< relref "/tools/jenkins/plugin-error3" >}}) — missing plugin
