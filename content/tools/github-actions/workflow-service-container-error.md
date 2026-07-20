---
title: "[Solution] Workflow Service Container Error"
description: "Fix GitHub Actions service container configuration errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Service container errors occur when the `services` configuration is invalid:

```
Error: .github/workflows/ci.yml: services.postgres.image is required
```

## Common Causes

- Missing `image` key for a service.
- Invalid port mapping format.
- Service name conflicts with built-in names.

## How to Fix

**Define services properly:**

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - run: pg_isready -h localhost -p 5432
```

## Examples

```yaml
# Wrong - missing image
services:
  redis:
    ports:
      - 6379:6379

# Correct
services:
  redis:
    image: redis:7
    ports:
      - 6379:6379
```
