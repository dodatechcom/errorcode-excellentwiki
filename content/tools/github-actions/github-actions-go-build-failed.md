---
title: "[Solution] GitHub Actions Go Build Failed"
description: "Fix GitHub Actions Go build failures in CI workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Go build failures occur during Go compilation in the workflow:

```
Error: ./main.go:10:2: cannot find package "github.com/example/pkg"
```

## Common Causes

- Go modules not properly initialized.
- go.sum file is out of date.
- Go version mismatch.

## How to Fix

**Set up Go properly:**

```yaml
steps:
  - uses: actions/setup-go@v5
    with:
      go-version: '1.21'
      cache: true
  - run: go mod download
  - run: go build ./...
```

## Examples

```yaml
steps:
  - uses: actions/setup-go@v5
    with:
      go-version: '1.21'
      cache: true
  - run: go vet ./...
  - run: go build -o bin/app ./cmd/app
```
