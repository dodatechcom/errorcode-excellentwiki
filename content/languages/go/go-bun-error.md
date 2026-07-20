---
title: "[Solution] bun Query Builder Error Fix"
description: "Fix bun query builder errors. Handle query construction, model binding, and migration issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# bun Query Builder Error

The `bun` ORM fails during query execution when the model is not registered, column names are wrong, the query builder produces invalid SQL, or migration does not match the schema. bun uses struct tags for mapping and produces PostgreSQL-specific SQL by default.

## Common Causes

```go
// Cause 1: Model not registered
db := bun.NewDB(sqlDB, pgdialect.New())
// forgot: db.RegisterModel((*User)(nil))
err := db.NewSelect().Model(&users).Scan(ctx)
// relation "users" does not exist

// Cause 2: Column name mismatch
type User struct {
    ID   int
    Name string `bun:"column:username"` // DB has "name" not "username"
}

// Cause 3: Using raw SQL with bun placeholders
db.Query("SELECT * FROM users WHERE id = ?", 1) // uses ?
// PostgreSQL expects $1

// Cause 4: Missing table creation
db.NewCreateTable().Model((*User)(nil)).Exec(ctx)
// table "users" already exists

// Cause 5: N+1 query without relation loading
users, _ := db.NewSelect().Model(&users).Scan(ctx)
for _, u := range users {
    posts, _ := db.NewSelect().Model(&posts).
        Where("user_id = ?", u.ID).Scan(ctx) // N+1!
}
```

## How to Fix

### Fix 1: Register models and create tables

```go
import (
    "context"
    "database/sql"

    "github.com/uptrace/bun"
    "github.com/uptrace/bun/dialect/pgdialect"
    _ "github.com/lib/pq"
)

type User struct {
    ID    int    `bun:"id,pk,autoincrement"`
    Name  string `bun:"name,notnull"`
    Email string `bun:"email,unique"`
}

func main() {
    sqlDB, _ := sql.Open("postgres", "postgres://localhost/mydb?sslmode=disable")
    db := bun.NewDB(sqlDB, pgdialect.New())

    ctx := context.Background()

    // Create table
    _, err := db.NewCreateTable().Model((*User)(nil)).Exec(ctx)
    if err != nil {
        log.Fatal(err)
    }

    // Insert
    user := &User{Name: "Alice", Email: "alice@example.com"}
    _, err = db.NewInsert().Model(user).Exec(ctx)
    if err != nil {
        log.Fatal(err)
    }
}
```

### Fix 2: Use bun's query builder correctly

```go
// Select with conditions
var users []User
err := db.NewSelect().
    Model(&users).
    Where("name LIKE ?", "%Ali%").
    OrderExpr("id ASC").
    Limit(10).
    Scan(ctx)

// Update
_, err = db.NewUpdate().
    Model((*User)(nil)).
    Set("name = ?", "Bob").
    Where("id = ?", 1).
    Exec(ctx)
```

### Fix 3: Eager-load relations to avoid N+1

```go
var users []User
err := db.NewSelect().
    Model(&users).
    Relation("Posts").
    Relation("Profile").
    Scan(ctx)

for _, u := range users {
    fmt.Printf("User: %s, Posts: %d\n", u.Name, len(u.Posts))
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/uptrace/bun"
    "github.com/uptrace/bun/dialect/pgdialect"
    _ "github.com/lib/pq"
)

type User struct {
    ID    int    `bun:"id,pk,autoincrement"`
    Name  string `bun:"name,notnull"`
    Email string `bun:"email,unique"`
}

func main() {
    sqlDB, _ := sql.Open("postgres", "postgres://localhost/mydb?sslmode=disable")
    db := bun.NewDB(sqlDB, pgdialect.New())
    ctx := context.Background()

    db.NewCreateTable().Model((*User)(nil)).Exec(ctx)

    user := &User{Name: "Alice", Email: "alice@example.com"}
    db.NewInsert().Model(user).Exec(ctx)

    var users []User
    db.NewSelect().Model(&users).Scan(ctx)
    for _, u := range users {
        fmt.Printf("ID: %d, Name: %s\n", u.ID, u.Name)
    }
}
```

## Related Errors

- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — no rows returned
- [go-pgerror]({{< relref "/languages/go/go-pgerror" >}}) — PostgreSQL error codes
- [go-migrate-error]({{< relref "/languages/go/go-migrate-error" >}}) — migration failures
