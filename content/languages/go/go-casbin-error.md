---
title: "[Solution] Casbin Authorization Denied Fix"
description: "Fix Casbin authorization denied errors. Handle policy evaluation, model configuration, and role management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Casbin Authorization Denied

The Casbin authorization library fails when the RBAC/ABAC model configuration is wrong, policy rules are not loaded, the matcher function produces unexpected results, or the adapter cannot connect to the policy storage backend. Casbin uses PERM (Policy, Effect, Request, Matchers) model language.

## Common Causes

```go
// Cause 1: Model configuration wrong
// model.conf missing [matchers] section
// or [policy_effect] uses wrong effect

// Cause 2: Policy not loaded
e, _ := casbin.NewEnforcer("model.conf", "policy.csv")
// policy.csv is empty or not loaded
ok, _ := e.Enforce("alice", "data1", "read")
// false — no policy rules defined

// Cause 3: Role hierarchy not configured
// alice has role "admin" but model does not define [role_definition]
// users cannot be assigned to roles

// Cause 4: Adapter connection failure
a, _ := gormadapter.NewAdapterByDB(db)
e, _ := casbin.NewEnforcer("model.conf", a)
// adapter cannot read policy table

// Cause 5: Request does not match policy format
// Policy: p, alice, data1, read
// Request: alice, data1 (missing "read" action)
```

## How to Fix

### Fix 1: Define proper RBAC model

```ini
# model.conf
[request_definition]
r = sub, obj, act

[policy_definition]
p = sub, obj, act

[role_definition]
g = _, _

[policy_effect]
e = some(where (p.eft == allow))

[matchers]
m = g(r.sub, p.sub) && r.obj == p.obj && r.act == p.act
```

```go
import (
    "log"

    "github.com/casbin/casbin/v2"
    "github.com/casbin/casbin/v2/model"
)

func newEnforcer() (*casbin.Enforcer, error) {
    e, err := casbin.NewEnforcer("model.conf", "policy.csv")
    if err != nil {
        return nil, err
    }

    // Add policies programmatically
    e.AddPolicy("alice", "data1", "read")
    e.AddPolicy("bob", "data2", "write")

    // Add role assignments
    e.AddGroupingPolicy("alice", "admin")

    return e, nil
}
```

### Fix 2: Use GORM adapter for persistent policy storage

```go
import (
    "gorm.io/gorm"

    "github.com/casbin/casbin/v2"
    "github.com/casbin/gorm-adapter/v3"
)

func setupCasbin(db *gorm.DB) (*casbin.Enforcer, error) {
    adapter, err := gormadapter.NewAdapterByDB(db)
    if err != nil {
        return nil, err
    }

    e, err := casbin.NewEnforcer("model.conf", adapter)
    if err != nil {
        return nil, err
    }

    // Load policies from database
    e.LoadPolicy()

    return e, nil
}
```

### Fix 3: Check enforcement with debug logging

```go
func checkAccess(e *casbin.Enforcer, sub, obj, act string) (bool, error) {
    ok, err := e.Enforce(sub, obj, act)
    if err != nil {
        return false, fmt.Errorf("enforce error: %w", err)
    }
    if !ok {
        log.Printf("ACCESS DENIED: %s -> %s on %s", sub, act, obj)
    }
    return ok, nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "github.com/casbin/casbin/v2"
)

func main() {
    e, err := casbin.NewEnforcer("model.conf", "policy.csv")
    if err != nil {
        log.Fatal(err)
    }

    // Add policies
    e.AddPolicy("alice", "data1", "read")
    e.AddPolicy("bob", "data2", "write")
    e.AddGroupingPolicy("alice", "admin")

    // Check access
    tests := []struct{ sub, obj, act string }{
        {"alice", "data1", "read"},
        {"bob", "data2", "write"},
        {"bob", "data1", "read"},
    }

    for _, t := range tests {
        ok, _ := e.Enforce(t.sub, t.obj, t.act)
        fmt.Printf("%s %s %s: %v\n", t.sub, t.act, t.obj, ok)
    }
}
```

## Related Errors

- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault policy enforcement similar to Casbin
- [go-oauth-error]({{< relref "/languages/go/go-oauth-error" >}}) — OAuth token scopes for authorization
- [grpc-unauthenticated]({{< relref "/languages/go/grpc-unauthenticated" >}}) — gRPC authorization failures
