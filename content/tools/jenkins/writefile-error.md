---
title: "[Solution] Jenkins Pipeline writeFile Error"
description: "Fix writeFile step errors in Jenkins pipeline. Resolve file writing failures in Jenkinsfile."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Pipeline writeFile Error

The `writeFile` step writes a String to a file in the agent's workspace. Errors occur when the directory does not exist or permissions are insufficient.

## Common Causes

- Target directory does not exist
- Jenkins agent user lacks write permissions
- File encoding mismatch
- Disk space is full

## How to Fix

```groovy
sh 'mkdir -p output/config'
writeFile file: 'output/config/app.yml', text: 'key: value'
```

```groovy
writeFile file: 'output/report.csv', text: csvContent, encoding: 'UTF-8'
```
