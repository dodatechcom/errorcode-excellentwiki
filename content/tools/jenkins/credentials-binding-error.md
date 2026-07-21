---
title: "[Solution] Jenkins Credentials Binding Error"
description: "Fix Jenkins credentials binding errors when the withCredentials step cannot bind the specified credential to an environment variable."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Credentials Binding Error

Credentials binding errors occur when the `withCredentials` step cannot bind a credential to an environment variable because the credential is missing, expired, or incorrectly configured.

## Common Causes

- Credential ID does not match any stored credential
- Credential type does not match the binding method
- Credential was deleted or expired
- Pipeline runs on a different folder scope than where credential is stored
- User does not have permission to access the credential

## How to Fix

### Solution 1: Verify credential exists

Navigate to **Manage Jenkins > Credentials** and verify the credential ID matches:

```groovy
pipeline {
    stages {
        stage('Deploy') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'my-deploy-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $USER:$PASS'
                }
            }
        }
    }
}
```

### Solution 2: Use correct binding type

```groovy
// Username/password
withCredentials([usernamePassword(credentialsId: 'creds', usernameVariable: 'U', passwordVariable: 'P')])

// Secret text
withCredentials([string(credentialsId: 'token', variable: 'TOKEN')])

// File
withCredentials([file(credentialsId: 'keystore', variable: 'KEYSTORE')])

// SSH key
withCredentials([sshUserPrivateKey(credentialsId: 'ssh-key', keyFileVariable: 'KEY', usernameVariable: 'USER')])
```

### Solution 3: Check credential scope

Ensure the credential is in the same folder scope as the pipeline or in the global scope.

## Examples

```
ERROR: Credentials "missing-cred" not found
ERROR: java.lang.ClassCastException: class credentials binding
```

## Prevent It

- Store credentials in the correct folder scope
- Use consistent credential IDs across pipelines
- Test credential binding in a simple pipeline first
