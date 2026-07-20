---
title: "[Solution] No Credentials Found for SCM in Jenkins"
description: "Fix 'no credentials found' errors for SCM checkout in Jenkins. Resolve missing credential configuration."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# No Credentials Found for SCM in Jenkins

Jenkins requires credentials to access private repositories. When the specified credential ID does not exist, the checkout fails.

## Common Causes

- Credential ID typo in Jenkinsfile
- Credential was deleted
- Credential is in a different scope (folder vs global)

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
# Add credentials with the correct ID
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-credentials system::system::jenkins
```
