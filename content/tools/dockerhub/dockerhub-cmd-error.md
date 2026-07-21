---
title: "[Solution] DockerHub CMD Error"
description: "Fix DockerHub CMD instruction errors. Resolve default command issues."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
---

DockerHub CMD Error can prevent your application from working correctly.

## Common Causes

- CMD syntax error
- Command not found
- Multiple CMD used

## How to Fix

### Correct CMD

```dockerfile
CMD ["node", "server.js"]
```

