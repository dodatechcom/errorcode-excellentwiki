---
title: "[Solution] ent Mutation Error Fix"
description: "Fix ent ORM mutation errors. Handle entity creation, graph traversal, and schema mutations."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ent Mutation Error

The `ent` ORM framework for Go fails during entity mutation operations when schema definitions are incomplete, required fields are missing, unique constraints are violated, or edge traversals point to non-existent records. ent uses code generation, so many errors are caught at compile time, but runtime mutation errors still occur.

## Common Causes

```go
// Cause 1: Required field not set
client.User.Create().
    SetName("Alice").
    // forgot SetEmail — required field
    Save(ctx)
// ent: field "email" is required

// Cause 2: Unique constraint violation
client.User.Create().
    SetEmail("alice@example.com").
    Save(ctx) // first insert OK
client.User.Create().
    SetEmail("alice@example.com").
    Save(ctx) // unique_violation: duplicate email

// Cause 3: Edge not loaded — N+1 or nil pointer
user, _ := client.User.Get(ctx, 1)
fmt.Println(user.Edges.Pets) // empty — not loaded with QueryPets()

// Cause 4: Transaction rollback on constraint violation
tx, _ := client.Tx(ctx)
tx.User.Create().SetEmail("a@b.com").Save(ctx)
tx.User.Create().SetEmail("a@b.com").Save(ctx) // duplicate, tx rolled back

// Cause 5: Mutation on soft-deleted entity
client.User.Update().Where(user.ID(1)).SetAge(30).Exec(ctx)
// entity already soft-deleted, no rows affected
```

## How to Fix

### Fix 1: Use mutation builder with all required fields

```go
import (
    "context"
    "fmt"
    "log"

    "your-project/ent"
    "your-project/ent/user"
)

func createUser(ctx context.Context, client *ent.Client) (*ent.User, error) {
    u, err := client.User.Create().
        SetName("Alice").
        SetEmail("alice@example.com").
        SetAge(30).
        Save(ctx)
    if err != nil {
        return nil, fmt.Errorf("create user: %w", err)
    }
    return u, nil
}
```

### Fix 2: Handle unique constraint violations gracefully

```go
func createOrUpdateUser(ctx context.Context, client *ent.Client, name, email string) (*ent.User, error) {
    u, err := client.User.Create().
        SetName(name).
        SetEmail(email).
        Save(ctx)
    if ent.IsConstraintError(err) {
        // Update existing user instead
        return client.User.Update().
            Where(user.EmailEQ(email)).
            SetName(name).
            Save(ctx)
    }
    return u, err
}
```

### Fix 3: Use eager loading for edges

```go
users, err := client.User.
    Query().
    WithPets(func(q *ent.PetQuery) {
        q.WithOwner() // nested eager loading
    }).
    All(ctx)

for _, u := range users {
    fmt.Printf("User: %s, Pets: %d\n", u.Name, len(u.Edges.Pets))
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"

    "your-project/ent"
)

func main() {
    client, err := ent.Open("sqlite3", "file:ent.db?mode=memory")
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    ctx := context.Background()

    // Create schema
    if err := client.Schema.Create(ctx); err != nil {
        log.Fatal(err)
    }

    // Create a user
    u, err := client.User.Create().
        SetName("Alice").
        SetEmail("alice@example.com").
        Save(ctx)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created user: %d - %s\n", u.ID, u.Name)

    // Query with condition
    users, err := client.User.Query().
        Where(user.NameContains("Ali")).
        All(ctx)
    if err != nil {
        log.Fatal(err)
    }
    for _, u := range users {
        fmt.Printf("Found: %s\n", u.Name)
    }
}
```

## Related Errors

- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — entity not found during query
- [go-pgerror]({{< relref "/languages/go/go-pgerror" >}}) — underlying PostgreSQL constraint violations
- [invalid-memory-address]({{< relref "/languages/go/invalid-memory-address" >}}) — nil pointer on unloaded edge
