---
title: "[Solution] DockerHub Tag Not Found"
description: "Fix DockerHub tag not found errors. Resolve image tag lookup issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Tag Not Found can prevent your application from working correctly.

## Common Causes

- Tag does not exist
- Typo in tag name
- Tag was removed

## How to Fix

### List Tags

```bash
curl -s "https://hub.docker.com/v2/repositories/library/nginx/tags/?page_size=10" | jq '.results[].name'
```

