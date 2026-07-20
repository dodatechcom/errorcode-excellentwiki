---
title: "[Solution] Jenkins Plugin Not Updated Warning"
description: "Fix Jenkins plugin update warnings and security vulnerabilities. Resolve outdated plugin issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Plugin Not Updated Warning

Outdated plugins may contain security vulnerabilities or bugs.

## How to Fix

```bash
# Manage Jenkins > Plugins > Updates
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin plugin-name:latest
java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart
```

Monitor: https://www.jenkins.io/security/advisories/
