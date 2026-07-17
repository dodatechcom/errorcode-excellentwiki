---
title: "Jenkins Credential Error"
description: "Jenkins cannot find or access configured credentials."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Jenkins Credential Error

A Jenkins credential error occurs when the pipeline cannot access the credentials needed for operations like Git cloning, SSH deployment, or API authentication.

## Common Causes

- Credential not configured in Jenkins
- Credential ID mismatch in pipeline
- Credential expired or revoked
- Credential scope (global vs. folder) not matching

## How to Fix

### Configure Credentials

Go to **Manage Jenkins > Credentials > System > Global credentials**:
- Click **Add Credentials**
- Choose the appropriate type (Username/Password, SSH Key, etc.)

### Reference Credential in Pipeline

```groovy
// Username/Password
withCredentials([usernamePassword(
    credentialsId: 'my-credentials',
    usernameVariable: 'USERNAME',
    passwordVariable: 'PASSWORD'
)]) {
    sh 'echo $USERNAME $PASSWORD'
}

// SSH Key
withCredentials([sshUserPrivateKey(
    credentialsId: 'ssh-key',
    keyFileVariable: 'SSH_KEY',
    usernameVariable: 'USER'
)]) {
    sh 'ssh -i $SSH_KEY $USER@server command'
}
```

### Check Credential Scope

Ensure the credential is accessible from the folder where the job runs.

### Verify Credential ID

```groovy
// Must match exactly the ID configured in Jenkins
credentialsId: 'my-credentials'  // Case-sensitive
```

### Check Jenkins Logs

```bash
tail -f /var/log/jenkins/jenkins.log | grep -i credential
```

## Examples

```text
com.cloudbees.plugins.credentials.common.UnresolvableCredentialsException:
Credentials 'my-credentials' not found among {usernamePassword=my-pass}
```

## Related Errors

- [Permission Error]({{< relref "/tools/jenkins/jenkins-permission-error" >}}) — permission issues
- [Pipeline Error]({{< relref "/tools/jenkins/pipeline-error" >}}) — pipeline syntax error
