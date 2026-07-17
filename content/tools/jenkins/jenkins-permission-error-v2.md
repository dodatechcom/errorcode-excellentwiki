---
title: "Jenkins Permission Project Not Accessible"
description: "Jenkins project or resource is not accessible due to permission issues."
tools: ["jenkins"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jenkins", "permission", "access", "authorization", "role"]
weight: 5
---

# Jenkins Permission — Project Not Accessible

This error occurs when a Jenkins user or service account lacks the necessary permissions to access a project, view build results, or execute pipeline operations.

## Common Causes

- Role-Based Access Control (RBAC) misconfigured
- User not added to the correct group or role
- Project-level permissions not set
- Anonymous access restricted

## How to Fix

### Configure Project Permissions

Go to **Project > Configure > Authorization** and set appropriate permissions.

### Assign Role to User

```groovy
// In CasC or init script
import com.michelin.casdo.*
def roleMap = Jenkins.instance.getItem('my-project').properties
```

### Use Role-Based Authorization Strategy

```groovy
// Configure RBAC
RoleBasedAuthorizationStrategy strategy = new RoleBasedAuthorizationStrategy()
```

### Grant Read Permission

Go to **Manage Jenkins > Security > Authorization** and configure matrix-based or role-based authorization.

### Check User Permissions

```groovy
// Jenkins Script Console
println Jenkins.instance.authorizationStrategy.getClass().name
```

### Enable Project-Based Permissions

```yaml
# CasC configuration
jenkins:
  authorizationStrategy:
    projectMatrix:
      entries:
        - user: "dev-user"
          permissions: ["Job/Read", "Job/Build"]
```

## Examples

```text
用户 dev-user 没有权限查看 Job 'my-project'
  Permission: Overall/Read required
```

## Related Errors

- [Jenkins Credential Error]({{< relref "/tools/jenkins/jenkins-credential-error" >}}) — credential issues
- [Jenkins Build Failed]({{< relref "/tools/jenkins/jenkins-build-failed" >}}) — general build failure
- [Jenkins Agent Error]({{< relref "/tools/jenkins/jenkins-agent-error" >}}) — agent connection issues
