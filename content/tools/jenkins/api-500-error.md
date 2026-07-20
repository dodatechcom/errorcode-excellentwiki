---
title: "[Solution] Jenkins REST API 500 Internal Server Error"
description: "Fix Jenkins API 500 internal server errors. Resolve server-side API processing failures."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins REST API 500 Internal Server Error

API calls return 500 when Jenkins encounters an internal server error.

## How to Fix

```bash
# Manage Jenkins > System Log
# Or: $JENKINS_HOME/logs/
```

```bash
curl -u admin:token -H "Content-Type: application/json"   -d '{"parameter": [{"name":"VERSION","value":"1.0"}]}'   http://jenkins:8080/job/my-job/buildWithParameters
```
