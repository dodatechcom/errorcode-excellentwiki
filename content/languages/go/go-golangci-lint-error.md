---
title: "[Solution] Go golangci-lint Error — How to Fix"
description: "Fix Go golangci-lint errors. Handle linter configuration, exclusions, performance, and CI integration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go golangci-lint Error

Fix Go golangci-lint errors. Handle linter configuration, exclusions, performance, and CI integration.

## Why It Happens

- golangci-lint runs too slowly on large codebases because too many linters are enabled
- Linter exclusions do not work as expected because of configuration syntax
- False positives from linters that do not understand project-specific patterns
- golangci-lint version mismatch causes different results locally and in CI

## Common Error Messages

```
golangci-lint: timeout exceeded
```
```
golangci-lint: unknown linter
```
```
golangci-lint: can't load package
```
```
level=error msg="Timeout exceeded"
```

## How to Fix It

### Solution 1: Configure golangci-lint

```yaml
# .golangci.yml
linters:
  enable:
    - errcheck
    - gosimple
    - govet
    - ineffassign
    - staticcheck
    - unused
  disable:
    - depguard
linters-settings:
  errcheck:
    check-blank: true
issues:
  exclude-rules:
    - path: _test.go
      linters: [errcheck]
```

### Solution 2: Exclude false positives

```yaml
issues:
  exclude-rules:
    - path: generated/
      linters: [staticcheck]
    - path: _test.go
      text: "SA1019"
```

### Solution 3: Run with timeout

```bash
golangci-lint run --timeout 5m ./...
# Or skip specific linters
# golangci-lint run --disable errcheck ./...
```

### Solution 4: Pin version in CI

```yaml
# .github/workflows/lint.yml
- uses: golangci/golangci-lint-action@v4
  with:
    version: v1.57.2
```

## Common Scenarios

- golangci-lint times out because the codebase is too large
- A new linter version introduces false positives
- Configuration file syntax differs between versions

## Prevent It

- Pin golangci-lint version in CI and locally
- Use issue exclusion rules to suppress known false positives
- Run golangci-lint only on changed files in pull requests
