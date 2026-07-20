---
title: "[Solution] ent Constraint Violation Error Fix"
description: "Fix ent ORM constraint violation errors. Handle unique constraints, foreign key violations, and check constraints."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ent Constraint Violation Error

The `ent` framework returns constraint violations when unique, not-null, or foreign key constraints are violated during create or update operations. ent surfaces these as typed errors that can be checked with `ent.IsConstraintError()`.

## Common Causes

```go
// Cause 1: Unique field violation
client.User.Create().
    SetEmail("dup@example.com").
    Save(ctx) // second insert with same email

// Cause 2: Required field not set
client.User.Create().
    SetName("Alice").
    Save(ctx) // missing required email field

// Cause 3: Foreign key points to non-existent record
client.Pet.Create().
    SetName("Rex").
    SetOwnerID(99999). // user 99999 does not exist
    Save(ctx)

// Cause 4: Check constraint violation
// Database check: age >= 0 AND age <= 150
client.User.Create().
    SetAge(-5).
    Save(ctx) // check_violation

// Cause 5: Transaction conflict on concurrent upsert
tx1, _ := client.Tx(ctx)
tx2, _ := client.Tx(ctx)
tx1.Counter.Update().AddValue(1).Save(ctx)
tx2.Counter.Update().AddValue(1).Save(ctx) // serialization failure
```

## How to Fix

### Fix 1: Handle constraint errors with upsert pattern

```go
import (
    "context"
    "errors"

    "your-project/ent"
    "your-project/ent/user"
)

func createOrUpdateUser(ctx context.Context, client *ent.Client, name, email string) (*ent.User, error) {
    u, err := client.User.Create().
        SetName(name).
        SetEmail(email).
        Save(ctx)

    if ent.IsConstraintError(err) {
        // Update existing
        return client.User.Update().
            Where(user.EmailEQ(email)).
            SetName(name).
            Save(ctx)
    }

    if err != nil {
        return nil, err
    }
    return u, nil
}
```

### Fix 2: Use SaveOrUpdate for atomic upsert

```go
u, err := client.User.Create().
    SetName("Alice").
    SetEmail("alice@example.com").
    OnConflict(
        user.ConflictColumns(user.FieldEmail),
    ).
    UpdateNewValues().
    Save(ctx)
```

### Fix 3: Validate before mutation

```go
func validateUser(name, email string) error {
    if name == "" {
        return fmt.Errorf("name is required")
    }
    if !strings.Contains(email, "@") {
        return fmt.Errorf("invalid email")
    }
    return nil
}

func createUser(ctx context.Context, client *ent.Client, name, email string) (*ent.User, error) {
    if err := validateUser(name, email); err != nil {
        return nil, err
    }
    return client.User.Create().SetName(name).SetEmail(email).Save(ctx)
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
    client.Schema.Create(ctx)

    // First create succeeds
    u1, err := client.User.Create().
        SetName("Alice").
        SetEmail("alice@example.com").
        Save(ctx)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created: %d - %s\n", u1.ID, u1.Name)

    // Duplicate email — handle gracefully
    u2, err := client.User.Create().
        SetName("Alice2").
        SetEmail("alice@example.com").
        Save(ctx)
    if ent.IsConstraintError(err) {
        fmt.Println("Email already exists, updating...")
        u2, _ = client.User.Update().
            Where(user.EmailEQ("alice@example.com")).
            SetName("Alice2").
            Save(ctx)
    }
    fmt.Printf("Result: %d - %s\n", u2.ID, u2.Name)
}
```

## Related Errors

- [go-pgerror]({{< relref "/languages/go/go-pgerror" >}}) — PostgreSQL-specific constraint violation codes
- [go-mysql-error]({{< relref "/languages/go/go-mysql-error" >}}) — MySQL duplicate entry errors
- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — no matching row found
