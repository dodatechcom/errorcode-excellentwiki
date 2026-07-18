---
title: "[Solution] GitLab CI Service Error"
description: "Fix GitLab CI service errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Service Error

Service errors occur when Docker service containers fail to start or connect.

## Why This Happens

- Image not accessible
- Port not exposed
- Health check failing
- Alias not resolving

## Common Error Messages

- `service_not_starting`
- `service_connection_error`
- `service_image_error`
- `service_health_error`

## How to Fix It

### Solution 1: Define services correctly

Use name, alias, and variables:

```yaml
services:
  - name: postgres:14
    alias: db
    variables:
      POSTGRES_DB: test_db
      POSTGRES_PASSWORD: secret
```

### Solution 2: Use aliases for connections

Connect to services using their alias:

```yaml
script:
  - psql -h db -U postgres -d test_db
```

### Solution 3: Add health checks

Ensure services are ready before jobs start.


## Common Scenarios

- **Cannot connect:** Check alias and port.
- **Service not starting:** Verify the image exists and is accessible.

## Prevent It

- Use aliases
- Add health checks
- Define variables
