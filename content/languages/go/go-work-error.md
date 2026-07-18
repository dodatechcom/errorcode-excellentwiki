---
title: "[Solution] Go workspace Error — How to Fix"
description: "Fix Go workspace errors. Handle go.work configuration, multi-module development, and workspace switching."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go workspace Error

Fix Go workspace errors. Handle go.work configuration, multi-module development, and workspace switching.

## Why It Happens

- go.work file is not configured correctly causing module resolution failures
- Workspace mode conflicts with individual module versions
- IDE does not recognize workspace configuration
- go.work.sum grows too large over time

## Common Error Messages

```
go.work: unknown directive
```
```
go: workspace module not found
```
```
go.work: no such module
```
```
go: use of go.work is disabled
```

## How to Fix It

### Solution 1: Configure go workspace

```go
// go.work init ./module1 ./module2
// go.work use ./local-pkg
// go.work edit -dropuse ./deprecated-pkg
// go.work sync
```

### Solution 2: Manage workspace dependencies

```go
// go.work uses local module paths
go work use ./api ./core ./shared
// Go 1.22+: go.work.sum tracks workspace deps
```

### Solution 3: Switch between workspace and non-workspace mode

```go
// Workspace mode is enabled when go.work exists
// Disable: export GOWORK=off
// Or: go build -mod=mod
```

### Solution 4: Use workspace for multi-module projects

```go
// go.work
// go 1.22
// use (
//     ./api
//     ./core
//     ./shared
// )
```

## Common Scenarios

- go.work file causes module resolution to pick the wrong version
- IDE does not support go workspace and gives incorrect diagnostics
- go.work.sum is huge and slowing down builds

## Prevent It

- Use GOWORK=off to disable workspace mode temporarily
- Keep go.work file in .gitignore if each developer has different local modules
- Run go.work sync to update go.work.sum
