---
title: "[Solution] Docker Hub Rate Limit Error"
description: "Fix Docker Hub rate limit errors. Learn why this happens and how to resolve it quickly."
tools: ["dockerhub"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Docker Hub Rate Limit Error

Docker Hub rate limit errors occur when pull or push requests exceed the allowed limits.

## Why This Happens

- Pull limit exceeded
- Push limit exceeded
- Anonymous limit
- Authenticated limit

## Common Error Messages

- `rate_pull_error`
- `rate_push_error`
- `rate_anonymous_error`
- `rate_authenticated_error`

## How to Fix It

### Solution 1: Check rate limits

View your rate limit status:

```bash
curl -s -I https://registry-1.docker.io/v2/ | grep -i ratelimit
```

### Solution 2: Authenticate to increase limits

Log in to Docker Hub:

```bash
docker login
```

### Solution 3: Use registry mirrors

Set up a local registry mirror:

```json
{"registry-mirrors": ["https://mirror.example.com"]}
```


## Common Scenarios

- **Anonymous limit exceeded:** Authenticate to increase limits.
- **Authenticated limit exceeded:** Use registry mirrors.

## Prevent It

- Authenticate pulls
- Use registry mirrors
- Cache images locally
