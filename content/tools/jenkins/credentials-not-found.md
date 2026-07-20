---
title: "[Solution] Jenkins Credentials Not Found"
description: "Fix Jenkins credentials not found errors. Resolve missing credential configuration and access issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Credentials Not Found

Jenkins credentials not found errors occur when the pipeline references a credential ID that does not exist.

## Common Causes

- Credential ID typo
- Credential was deleted
- Credential in different scope (folder vs global)

## How to Fix

```bash
# Manage Jenkins > Credentials > System > Global credentials
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-credentials system::system::jenkins
```
