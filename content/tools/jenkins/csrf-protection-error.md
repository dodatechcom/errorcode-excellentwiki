---
title: "[Solution] Jenkins CSRF Protection Error"
description: "Fix Jenkins CSRF protection errors. Resolve cross-site request forgery token issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins CSRF Protection Error

CSRF protection requires a valid crumb token for POST requests.

## How to Fix

```bash
CRUMB=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField']+':'+d['crumb'])")
curl -u admin:token -H "$CRUMB" -X POST http://jenkins:8080/job/my-job/build
```
