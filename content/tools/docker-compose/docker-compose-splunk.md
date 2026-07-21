---
title: "[Solution] Docker Compose Splunk Logging Error"
description: "Fix Docker Compose splunk logging errors. Resolve Splunk log driver issues."
tools: ["docker-compose"]
error-types: ["tool-error"]
severities: ["error"]
---

Docker Compose Splunk Logging Error can prevent your application from working correctly.

## Common Causes

- Splunk server unreachable
- Token invalid

## How to Fix

### Use Splunk

```yaml
logging:
  driver: splunk
  options:
    splunk-token: "my-token"
    splunk-url: "https://splunk.example.com:8088"
```

