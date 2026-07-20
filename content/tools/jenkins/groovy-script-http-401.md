---
title: "[Solution] Jenkins Groovy Script HTTP 401 Error"
description: "Fix Jenkins Groovy script HTTP 401 unauthorized errors. Resolve script console authentication issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Groovy Script HTTP 401 Error

HTTP 401 errors occur when Groovy scripts sent via HTTP are not authenticated properly.

## How to Fix

```bash
curl -u admin:api-token -d "script=println 'Hello'" http://localhost:8080/scriptText
```

```bash
CRUMB=$(curl -s -u admin:api-token http://localhost:8080/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField']+':'+d['crumb'])")
curl -u admin:api-token -H "$CRUMB" -d "script=println Jenkins.instance.version" http://localhost:8080/scriptText
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ groovy = <<'EOF'
println Jenkins.instance.version
EOF
```
