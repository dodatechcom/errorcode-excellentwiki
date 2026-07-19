---
title: "[Solution] Go test coverage threshold — Testing Error Fix"
description: "Fix Go test coverage threshold enforcement."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# test coverage threshold

Enforce minimum test coverage in CI/CD pipelines.

## How to Fix

### Fix 1: Check coverage percentage

```bash
go test -coverprofile=coverage.out ./...
go tool cover -func=coverage.out | tail -1
# output: total: (statements) 85.2%
```

### Fix 2: Use coverage tool

```bash
gocover-cobertura < coverage.out > coverage.xml
```

## Related Errors

- [test-fail]({{< relref "/languages/go/test-fail" >}}) — test failed.
- [go-test-coverage]({{< relref "/languages/go/go-test-coverage" >}}) — coverage issues.
