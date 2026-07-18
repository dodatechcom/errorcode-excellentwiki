---
title: "[Solution] Go mod Error — How to Fix"
description: "Fix Go mod errors. Handle module initialization, dependency management, version resolution, and workspace configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go mod Error

Fix Go mod errors. Handle module initialization, dependency management, version resolution, and workspace configuration.

## Why It Happens

- go mod tidy produces different results than what is in go.sum
- Dependency version resolution fails because of incompatible transitive dependencies
- Module replacement breaks because the replaced module is not available
- go.sum contains entries for modules that are no longer needed

## Common Error Messages

```
go: module not found
```
```
go: version constraints not satisfiable
```
```
go: sum mismatch
```
```
go: github.com/...@...: reading github.com/...: 404
```

## How to Fix It

### Solution 1: Initialize and manage modules

```go
// go mod init github.com/myorg/myproject
// go mod tidy
// go get github.com/pkg/errors@v0.9.1
// go mod edit -replace github.com/old/pkg=github.com/fork/pkg@v1.0.0
// go mod vendor
```

### Solution 2: Fix version conflicts

```go
// go get specific transitive dependency
go get github.com/pkg/specific-dep@v1.2.3
// Check why a dependency is needed
go mod why github.com/pkg/dep
// Graph dependency tree
go mod graph
```

### Solution 3: Use replace for local development

```go
// go mod edit -replace ./local-pkg
// go mod edit -replace github.com/pkg=./local-pkg
// go mod edit -dropreplace github.com/pkg
```

### Solution 4: Clean up modules

```go
// go mod tidy - fixes go.sum
// go mod vendor - vendor all dependencies
// go mod verify - verify dependencies are correct
// go mod download - download all dependencies
```

## Common Scenarios

- go mod tidy changes go.sum every time it runs
- A transitive dependency pulls in an incompatible version
- go get cannot find a specific version of a module

## Prevent It

- Run go mod tidy and commit the changes
- Use go mod graph to understand dependency chains
- Use replace directives for local development of dependencies
