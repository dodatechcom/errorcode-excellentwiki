---
title: "[Solution] Heroku API Rate Limit Exceeded — How to Fix"
description: "Fix Heroku API rate limit errors by implementing request throttling, using conditional requests, optimizing API call patterns, and upgrading to higher rate limit tiers."
tools: ["heroku"]
error-types: ["rate-limit-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku API rate limit error occurs when your application or CLI client exceeds the number of allowed API requests within a given time window. Heroku enforces rate limits to ensure platform stability.

## What This Error Means

Heroku's Platform API and CLI both enforce rate limits. The API allows a certain number of requests per hour per account or per IP address. When you exceed this limit, the API returns a 429 Too Many Requests response. The error includes headers indicating the rate limit window, remaining requests, and when the limit resets.

Rate limits apply to both authenticated requests (using API tokens) and unauthenticated requests. The limits differ based on your authentication method and Heroku plan.

## Why It Happens

- Automated scripts or CI/CD pipelines make too many API calls in a short period
- Polling loops in monitoring tools check Heroku API too frequently
- A deployed application with many dynos makes excessive API calls on startup
- Heroku CLI commands are run in a tight loop (e.g., shell scripts)
- Multiple applications or users share the same API token
- A bug in application code causes an infinite loop of API calls
- Heroku Review Apps are created or destroyed too rapidly
- Log tailing or streaming services reconnect too frequently

## Common Error Messages

```
 ▸    HTTP 429 - Too Many Requests - Rate limit exceeded
# or
 ▸    Rate limit exceeded. Try again in X seconds.
# or
 ▸    API rate limit exceeded for account@example.com
# or
429 Too Many Requests (Retry-After: 3600)
```

## How to Fix It

### 1. Check Rate Limit Status

```bash
# Check your current rate limit usage
heroku limits

# Or using the API directly
curl -I -H "Authorization: Bearer $(heroku auth:token)" \
    https://api.heroku.com/apps

# Look for headers:
# RateLimit-Remaining: 4000
# RateLimit-Reset: 1623456789
# Retry-After: 3600
```

### 2. Implement Request Throttling

```python
import time
import requests

class HerokuThrottledClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.last_request_time = 0
        self.min_interval = 0.1  # Max 10 requests per second
    
    def _throttle(self):
        now = time.time()
        elapsed = now - self.last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request_time = time.time()
    
    def request(self, method, path):
        self._throttle()
        url = f"https://api.heroku.com{path}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/vnd.heroku+json; version=3"
        }
        return requests.request(method, url, headers=headers)
```

### 3. Use Conditional Requests with ETags

```python
import requests

class HerokuConditionalClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.etag_cache = {}
    
    def get_with_cache(self, path):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/vnd.heroku+json; version=3"
        }
        
        # Send ETag from previous response
        if path in self.etag_cache:
            headers["If-None-Match"] = self.etag_cache[path]
        
        response = requests.get(
            f"https://api.heroku.com{path}",
            headers=headers
        )
        
        if response.status_code == 304:
            # Not modified — use cached data
            return self.cached_data[path]
        
        # Cache the ETag and response
        if 'etag' in response.headers:
            self.etag_cache[path] = response.headers['etag']
            self.cached_data[path] = response.json()
        
        return response.json()
```

### 4. Optimize API Call Patterns

```python
# Bad: Making individual API calls for each app
for app_name in app_names:
    response = requests.get(f"https://api.heroku.com/apps/{app_name}", headers=headers)
    app_data = response.json()

# Good: Batch operations when possible
# List all apps in one call
response = requests.get("https://api.heroku.com/apps", headers=headers)
all_apps = response.json()

# Filter locally
target_apps = [app for app in all_apps if app['name'] in app_names]
```

### 5. Reduce CLI Call Frequency

```bash
# Bad: polling in a tight loop
while true; do
    heroku logs -n 10 -a my-app  # This counts as multiple API calls
    sleep 0.1
done

# Good: use --tail for streaming logs
heroku logs --tail -a my-app
```

### 6. Use Webhooks Instead of Polling

```bash
# Set up Heroku webhooks for events instead of polling
heroku webhooks:add \
    -i api:release \
    -i api:build \
    --url https://my-webhook.example.com/heroku-events \
    -a my-app \
    --secret my-webhook-secret

# List webhooks
heroku webhooks -a my-app
```

### 7. Handle Rate Limit Errors Gracefully

```python
import time
import requests

def api_call_with_retry(url, headers, max_retries=5):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            print(f"Rate limited. Waiting {retry_after} seconds...")
            time.sleep(retry_after)
            continue
        
        response.raise_for_status()
        return response
    
    raise Exception(f"Failed after {max_retries} retries due to rate limiting")
```

### 8. Use Multiple API Tokens for High-Volume Automation

```bash
# Create separate API tokens for different services
# Each token has its own rate limit

# Service 1: CI/CD
heroku authorizations:create -d "CI/CD Pipeline"

# Service 2: Monitoring
heroku authorizations:create -d "Monitoring Dashboard"

# Service 3: Backup
heroku authorizations:create -d "Automated Backup"

# List all authorizations
heroku authorizations
```

## Common Scenarios

### CI/CD Pipeline Hitting Rate Limits

A GitHub Actions workflow deploys to Heroku and then runs 50 individual `heroku run` commands for database seed data. Each command creates a one-off dyno and counts as an API call. The pipeline hits the rate limit midway through. Batch the seed commands into a single script and use one `heroku run` call.

### Monitoring Dashboard Polling Too Frequently

A custom monitoring dashboard polls the Heroku API every 5 seconds for dyno status, releases, and metrics. This generates 720 requests per hour per metric. The dashboard hits the 4500 request/hour rate limit within hours. Switch to Heroku webhooks for event-driven updates and increase the polling interval to 60 seconds.

### Shared API Token Across Services

A team shares one API token across five CI/CD pipelines, three monitoring services, and two deployment scripts. The combined request volume exceeds the rate limit. Create separate tokens for each service and distribute the load.

## Prevent It

- Use Heroku webhooks to receive event-driven updates instead of polling
- Implement exponential backoff with jitter in automated scripts
- Cache API responses with ETag support for read-heavy operations
- Use separate API tokens for different automated services
- Track rate limit headers (`RateLimit-Remaining`, `RateLimit-Reset`) in all API calls
- Set up alerts when remaining rate limit drops below 20%
- Use Heroku Platform API with pagination to reduce request count
- Batch operations into single API calls when possible

## Related Pages

- [Heroku App Not Found](/tools/heroku/heroku-app-not-found)
- [Heroku CLI Configuration Error](/tools/heroku/heroku-rc-error)
- [Heroku Config Error](/tools/heroku/heroku-config-error)
