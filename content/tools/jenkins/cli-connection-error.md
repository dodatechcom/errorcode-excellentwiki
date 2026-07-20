---
title: "[Solution] Jenkins CLI Connection Error"
description: "Fix Jenkins CLI connection errors. Resolve Jenkins Command Line Interface connectivity issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins CLI Connection Error

Jenkins CLI connection errors occur when the CLI cannot connect to the Jenkins server.

## How to Fix

```bash
curl -s http://localhost:8080/api/json | python3 -m json.tool
java -jar jenkins-cli.jar -s http://localhost:8080/ help
java -jar jenkins-cli.jar -s ssh://admin@localhost:22/ help
```

```bash
# Manage Jenkins > Configure Security > SSH Server > Enable > Set port
```
