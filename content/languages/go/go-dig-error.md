---
title: "[Solution] Go Dig Error — How to Fix"
description: "Fix Go Dig errors. Handle container construction, dependency resolution, invoke failures, and optional dependencies."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Dig Error

Fix Go Dig errors. Handle container construction, dependency resolution, invoke failures, and optional dependencies.

## Why It Happens

- Dig cannot resolve a type because no constructor provides it
- Multiple constructors provide the same type causing conflicts
- Invoke function signature does not match the provided dependencies
- Optional dependencies are not handled causing unnecessary failures

## Common Error Messages

```
missing dependency for type
```
```
multiple instances for type
```
```
could not resolve dependency
```
```
invoke failed
```

## How to Fix It

### Solution 1: Provide constructors properly

```go
c := dig.New()
c.Provide(NewConfig)
c.Provide(NewDatabase)
c.Provide(NewUserRepo)
c.Invoke(func(repo *UserRepo) {
    users := repo.FindAll()
})
```

### Solution 2: Handle optional dependencies

```go
type OptionalDep struct{}
c.Provide(func() *OptionalDep { return nil })
type Service struct {
    Dep *OptionalDep `optional:"true"`
}
```

### Solution 3: Use named values for multiple instances

```go
c.Provide(func() *sql.DB { return db1 }, dig.Name("primary"))
c.Provide(func() *sql.DB { return db2 }, dig.Name("secondary"))
```

### Solution 4: Scope dependencies correctly

```go
c.Scope("request", func(s *dig.Scope) {
    s.Provide(NewRequestContext)
    s.Invoke(HandleRequest)
})
```

## Common Scenarios

- Dig fails because a new type was added without a constructor
- Multiple constructors conflict because they provide the same interface
- Invoke function signature does not match available dependencies

## Prevent It

- Run dig validation in tests to catch missing providers early
- Use named values when multiple instances of the same type are needed
- Scope request-scoped dependencies to avoid leaking state between requests
