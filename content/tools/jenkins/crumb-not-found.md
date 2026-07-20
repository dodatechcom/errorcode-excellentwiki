---
title: "[Solution] Jenkins Crumb Issuer Not Found"
description: "Fix Jenkins crumb issuer not found errors. Resolve CSRF token generation issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Crumb Issuer Not Found

The crumb issuer provides CSRF tokens for API calls.

## How to Fix

```bash
# Manage Jenkins > Configure Security > CSRF Protection > Enable
curl -u admin:token http://jenkins:8080/crumbIssuer/api/json
```

```bash
CRUMB_FIELD=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField'])")
CRUMB_VALUE=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumb'])")
curl -u admin:token -H "${CRUMB_FIELD}:${CRUMB_VALUE}" -X POST http://jenkins:8080/job/my-job/build
```
