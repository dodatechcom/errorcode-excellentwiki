---
title: "[Solution] Go SQL No Rows in Result Set Fix"
description: "Fix Go sql: no rows in result set error. Handle empty results with sql.ErrNoRows, use QueryRow properly, and check for missing data."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# SQL: No Rows in Result Set — Fix

A `sql: no rows in result set` error occurs when `QueryRow.Scan()` is called but the SQL query returned zero rows.

## Description

Go's `database/sql` package returns `sql.ErrNoRows` when `Row.Scan()` is called on a query that returned no rows. This is common with `QueryRow()` when looking up a specific record that doesn't exist.

Common scenarios:

- **Record not found** — `SELECT * FROM users WHERE id = 999` returns no rows.
- **Wrong query conditions** — WHERE clause filters out all results.
- **Table is empty** — querying an empty table.
- **Race condition** — record was deleted between check and query.

## Common Causes

```go
// Cause 1: QueryRow with non-existent record
var name string
err := db.QueryRow("SELECT name FROM users WHERE id = ?", 999).Scan(&name)
// sql: no rows in result set

// Cause 2: Wrong WHERE clause
var count int
err := db.QueryRow("SELECT COUNT(*) FROM orders WHERE status = ?", "pending").Scan(&count)
// May return no rows if query is wrong

// Cause 3: Not checking for sql.ErrNoRows specifically
row := db.QueryRow("SELECT * FROM products WHERE sku = ?", "NONEXISTENT")
err := row.Scan(&id, &name)
if err != nil {
    log.Fatal(err) // Treats ErrNoRows as fatal error
}
```

## How to Fix

### Fix 1: Check for sql.ErrNoRows specifically

```go
// Wrong — treats all errors the same
err := db.QueryRow("SELECT name FROM users WHERE id = ?", id).Scan(&name)
if err != nil {
    log.Fatal(err)
}

// Correct — handle ErrNoRows separately
err := db.QueryRow("SELECT name FROM users WHERE id = ?", id).Scan(&name)
if err == sql.ErrNoRows {
    fmt.Println("user not found")
    return nil
} else if err != nil {
    return fmt.Errorf("query user: %w", err)
}
```

### Fix 2: Return a clear "not found" error

```go
func GetUser(ctx context.Context, db *sql.DB, id int) (*User, error) {
    var user User
    err := db.QueryRowContext(ctx,
        "SELECT id, name, email FROM users WHERE id = ?", id,
    ).Scan(&user.ID, &user.Name, &user.Email)

    if err == sql.ErrNoRows {
        return nil, fmt.Errorf("user %d: %w", id, ErrNotFound)
    }
    if err != nil {
        return nil, fmt.Errorf("query user %d: %w", id, err)
    }
    return &user, nil
}
```

### Fix 3: Use EXISTS check before querying

```go
// Wrong — two queries without atomicity
exists := db.QueryRow("SELECT 1 FROM users WHERE id = ?", id)
var found bool
err := exists.Scan(&found)

// Correct — single query with COALESCE
var name string
err := db.QueryRow("SELECT COALESCE(name, '') FROM users WHERE id = ?", id).Scan(&name)
if err == sql.ErrNoRows {
    name = "Guest"
}
```

### Fix 4: Use Query() instead of QueryRow() for optional results

```go
// Wrong — panics if no rows
var name string
err := db.QueryRow("SELECT name FROM users WHERE id = ?", id).Scan(&name)

// Correct — handle empty result set
rows, err := db.Query("SELECT name FROM users WHERE id = ?", id)
if err != nil {
    return "", err
}
defer rows.Close()

if !rows.Next() {
    return "", fmt.Errorf("user %d not found", id)
}

var name string
if err := rows.Scan(&name); err != nil {
    return "", err
}
```

### Fix 5: Create a helper function for common lookups

```go
var ErrNotFound = errors.New("record not found")

func scanOne[T any](row *sql.Row, scanFunc func(*T) []any) (*T, error) {
    var result T
    err := row.Scan(scanFunc(&result)...)
    if err == sql.ErrNoRows {
        return nil, ErrNotFound
    }
    if err != nil {
        return nil, err
    }
    return &result, nil
}

// Usage
user, err := scanOne(db.QueryRow("SELECT id, name FROM users WHERE id = ?", id),
    func(u *User) []any { return []any{&u.ID, &u.Name} },
)
```

## Examples

```go
// This triggers: sql: no rows in result set
package main

import (
    "database/sql"
    "fmt"
    _ "github.com/mattn/go-sqlite3"
)

func main() {
    db, _ := sql.Open("sqlite3", ":memory:")
    db.Exec("CREATE TABLE users (id INT, name TEXT)")

    var name string
    err := db.QueryRow("SELECT name FROM users WHERE id = ?", 1).Scan(&name)
    if err != nil {
        fmt.Println(err) // sql: no rows in result set
    }
}
```

## Related Errors

- [sql-no-rows]({{< relref "/languages/go/sql-no-rows" >}}) — no rows returned from query.
- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — resource not found (file system).
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — invalid JSON input.
