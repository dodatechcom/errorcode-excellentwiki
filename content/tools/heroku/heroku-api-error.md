---
title: "[Solution] Heroku API Returned Error — Fix Heroku API Issues"
description: "Fix Heroku API errors. Resolve API authentication, rate limiting, and request errors in Heroku platform API."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
weight: 8
---

A Heroku API returned error occurs when the Heroku Platform API rejects a request due to invalid credentials, missing permissions, or malformed requests. API errors are common when automating Heroku operations.

## What This Error Means

```json
{
  "id": "forbidden",
  "message": "Forbidden"
}
```

Or:

```json
{
  "id": "unauthorized",
  "message": "No API credentials provided"
}
```

The API request was rejected for authentication, authorization, or validation reasons.

## Why It Happens

- API key is invalid or expired
- The account does not have access to the resource
- The request body is malformed
- Rate limit has been exceeded
- The resource does not exist
- Insufficient permissions for the operation

## How to Fix It

### Authenticate API Requests

```bash
# Using Heroku CLI (auto-authenticates)
heroku apps

# Using API directly
curl -X GET "https://api.heroku.com/apps" \
  -H "Authorization: Bearer $(heroku auth:token)" \
  -H "Accept: application/vnd.heroku+json; version=3"
```

### Generate API Key

```bash
# In Heroku Dashboard:
# Account Settings > API Key > Reveal

# Or use Heroku CLI
heroku auth:token
```

### Check API Permissions

```bash
# List account info
curl -X GET "https://api.heroku.com/account" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3"

# List apps
curl -X GET "https://api.heroku.com/apps" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3"
```

### Handle Rate Limits

```bash
# Check rate limit headers
curl -I "https://api.heroku.com/apps" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3"

# Look for:
# Rate-Remaining: 4999
# Rate-Reset: 1699900000
```

### Fix Request Body

```bash
# Correct API request
curl -X POST "https://api.heroku.com/apps" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3" \
  -H "Content-Type: application/json" \
  --data '{
    "name": "my-new-app",
    "region": "us"
  }'
```

### Use Heroku CLI as Reference

```bash
# Heroku CLI logs show API calls
heroku --debug apps

# Check what headers are sent
heroku --verbose apps
```

## Common Mistakes

- Using the wrong API version header
- Not including the Accept header
- Using account credentials instead of API key
- Not handling 429 rate limit responses
- Not checking API documentation for required fields

## Related Pages

- [Heroku Rate Limit Error]({{< relref "/tools/heroku/heroku-rate-limit" >}}) — Rate limit exceeded on API
- [Heroku Runtimes Error]({{< relref "/tools/heroku/heroku-runtimes-error" >}}) — No such app
