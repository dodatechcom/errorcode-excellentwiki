---
title: "Jenkins Permission Error"
description: "Jenkins operation fails due to insufficient permissions or authorization issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "permission", "authorization", "user", "role"]
weight: 5
---

# Jenkins Permission Error

A Jenkins permission error occurs when a user or process lacks the necessary permissions to perform an operation. Jenkins uses Role-Based Access Control (RBAC) and project-level permissions.

## Common Causes

- User lacks required Jenkins permissions
- Role-Based Access Control (RBAC) not configured
- Project-level permissions restrict access
- API token lacks required scopes

## How to Fix

### Configure Global Permissions

Go to **Manage Jenkins > Security > Authorization**:
- Set to "Role-Based Authorization Strategy" or "Matrix-based security"

### Grant User Permissions

```groovy
// In Jenkinsfile
@NonCPS
def checkPermission() {
    if (!currentUser().hasPermission('Job/Build')) {
        error('You do not have permission to build this job')
    }
}
```

### Configure Project Permissions

Go to **Job > Configure > Authorization**:
- Add user or group with appropriate permissions

### Fix API Token Permissions

```bash
# Generate new API token with required scopes
# User > Configure > API Token
```

### Check Admin Permissions

```bash
# Add admin user via CLI
java -jar jenkins-cli.jar -s http://localhost:8080/ \
  -auth admin:token \
  add-user admin password "Full Name"
```

## Examples

```text
hudson.security.AccessDeniedException2: admin is missing the Job/Build permission
```

## Related Errors

- [Credential Error]({{< relref "/tools/jenkins/credential-error2" >}}) — credential issues
- [Agent Error]({{< relref "/tools/jenkins/agent-error" >}}) — agent connection issues
