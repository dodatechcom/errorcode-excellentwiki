---
title: "[Solution] Docker Compose AWS Logs Error"
description: "Fix Docker Compose awslogs logging errors. Resolve CloudWatch log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose AWS Logs Error can prevent your application from working correctly.

## Common Causes

- AWS credentials not configured
- Log group not found

## How to Fix

### Use awslogs

```yaml
logging:
  driver: awslogs
  options:
    awslogs-group: my-group
    awslogs-region: us-east-1
    awslogs-stream-prefix: my-prefix
```

