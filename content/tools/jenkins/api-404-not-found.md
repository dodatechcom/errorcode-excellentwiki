---
title: "[Solution] Jenkins REST API 404 Not Found"
description: "Fix Jenkins API 404 not found errors. Resolve API endpoint and job URL issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins REST API 404 Not Found

API calls return 404 when the requested resource does not exist.

## How to Fix

```bash
# Job: http://jenkins:8080/job/my-job/api/json
# Folder: http://jenkins:8080/job/my-folder/job/my-job/api/json
curl -u admin:token http://jenkins:8080/api/json?tree=jobs[name,url]
```
