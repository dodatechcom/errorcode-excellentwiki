---
title: "[Solution] DockerHub Storage Over Limit Error"
description: "Fix DockerHub storage over limit errors. Resolve storage quota exceeded issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub Storage Over Limit Error can prevent your application from working correctly.

## Common Causes

- Cannot push new images
- Storage quota exceeded

## How to Fix

### Reduce Storage

```bash
# Delete specific tag
curl -X DELETE "https://hub.docker.com/v2/repositories/username/repo/tags/tag/"
```

