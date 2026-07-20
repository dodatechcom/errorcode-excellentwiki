---
title: "[Solution] Jenkins REST API 403 Forbidden"
description: "Fix Jenkins API 403 forbidden errors. Resolve API authentication and permission issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins REST API 403 Forbidden

API calls return 403 when the authenticated user lacks permission.

## How to Fix

```bash
curl -u admin:valid-api-token http://jenkins:8080/api/json
```

```bash
CRUMB=$(curl -s -u admin:token http://jenkins:8080/crumbIssuer/api/json)
curl -u admin:token -H "$(echo $CRUMB | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d["crumbRequestField"]+":"+d["crumb"])')"   -X POST http://jenkins:8080/job/my-job/build
```
