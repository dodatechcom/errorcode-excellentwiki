---
title: "Jenkins Credential Not Found or Expired"
description: "Jenkins credential is missing, expired, or not accessible in the pipeline."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Credential — Not Found or Expired

This error occurs when a Jenkins credential referenced in a pipeline is missing, expired, or not accessible in the current scope. Builds that require authentication fail.

## Common Causes

- Credential ID misspelled
- Credential not stored in Jenkins
- Credential expired or revoked
- Credential not available in the credential scope
- Secret text or file credential corrupted

## How to Fix

### Verify Credential ID

```groovy
// Check the credential ID in Jenkins UI
// Manage Jenkins > Manage Credentials
withCredentials([string(credentialsId: 'my-api-key', variable: 'API_KEY')]) {
    sh 'echo $API_KEY'
}
```

### Add Credential

Go to **Manage Jenkins > Manage Credentials > Jenkins > Global credentials > Add Credentials**

### Use Credential in Pipeline

```groovy
// Username/password credential
withCredentials([usernamePassword(
    credentialsId: 'my-cred',
    usernameVariable: 'USER',
    passwordVariable: 'PASS'
)]) {
    sh 'curl -u $USER:$PASS https://api.example.com'
}
```

### Use SSH Key Credential

```groovy
withCredentials([sshUserPrivateKey(
    credentialsId: 'deploy-key',
    keyFileVariable: 'SSH_KEY',
    usernameVariable: 'SSH_USER'
)]) {
    sh 'ssh -i $SSH_KEY $SSH_USER@server.example.com'
}
```

### Debug Credential Access

```groovy
// Jenkins Script Console
println com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
    com.cloudbees.plugins.credentials.common.StandardCredentials.class,
    Jenkins.instance, null, null
).collect { it.id }
```

## Examples

```text
java.lang.IllegalArgumentException:
  Could not find credentials with id 'my-api-key' in store
```

## Related Errors

- [Jenkins Permission Error]({{< relref "/tools/jenkins/jenkins-permission-error" >}}) — permission issues
- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Pipeline Error]({{< relref "/tools/jenkins/jenkins-pipeline-error" >}}) — pipeline syntax error
