---
title: "[Solution] Go SQL No Rows in Result Set Fix"
description: "Fix Go sql no rows in result set error. Check for sql.ErrNoRows before treating it as a fatal error, and use QueryRow correctly."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["sql", "database", "rows", "query", "empty", "runtime"]
weight: 5
---

# SQL No Rows in Result Set Fix

The `sql: no rows in result set` error occurs when `QueryRow.Scan` is called but the query returned no rows.

## Description

In Go's `database/sql` package, `db.QueryRow` returns a `*sql.Row` that lazily executes the query. Calling `Scan` on it triggers the query and attempts to read the first row. If the query returns no rows, `Scan` returns `sql.ErrNoRows`. This is not a bug — it's a normal "not found" condition that must be handled.

Common scenarios:

- **Record doesn't exist** — querying by ID that has no matching row.
- **Optional record lookup** — checking if a record exists before creating.
- **Aggregation on empty table** — `SELECT COUNT(*)` on empty table still returns 1 row, but `SELECT *` returns none.
- **WHERE clause too restrictive** — filter condition eliminates all rows.

## Common Causes

```go
// Cause 1: Not checking for sql.ErrNoRows
func getUser(id int) User {
    var u User
    err := db.QueryRow("SELECT name FROM users WHERE id = ?", id).Scan(&u.Name)
    if err != nil {
        log.Fatal(err) // Fatal on "no rows" — should be handled
    }
    return u
}

// Cause 2: Wrong query returns empty result
func main() {
    var count int
    err := db.QueryRow("SELECT id FROM users WHERE id = ?", 999).Scan(&count)
    // No user with id=999, err is sql.ErrNoRows
}

// Cause 3: Query returns different columns than expected
func main() {
    var name string
    err := db.QueryRow("SELECT non_existent_column FROM users").Scan(&name)
    // This is a different error, not ErrNoRows
}

// Cause 4: Using QueryRow for aggregate without rows
func main() {
    var total int
    err := db.QueryRow("SELECT SUM(amount) FROM orders WHERE user_id = ?", -1).Scan(&total)
    // If no orders match, SUM returns NULL, Scan may return sql.ErrNoRows
}
```

## How to Fix

### Fix 1: Check specifically for sql.ErrNoRows

```go
func getUser(id int) (*User, error) {
    var u User
    err := db.QueryRow("SELECT name FROM users WHERE id = ?", id).Scan(&u.Name)
    if err != nil {
        if err == sql.ErrNoRows {
            return nil, nil // not found, not an error
        }
        return nil, err
    }
    return &u, nil
}
```

### Fix 2: Use EXISTS for existence checks

```go
func userExists(id int) (bool, error) {
    var exists bool
    err := db.QueryRow("SELECT EXISTS(SELECT 1 FROM users WHERE id = ?)", id).Scan(&exists)
    return exists, err
}
```

### Fix 3: Handle NULL results from aggregates

```go
func getTotalOrders(userID int) (int, error) {
    var total sql.NullInt64
    err := db.QueryRow("SELECT SUM(amount) FROM orders WHERE user_id = ?", userID).Scan(&total)
    if err != nil {
        return 0, err
    }
    if !total.Valid {
        return 0, nil // no orders — treat as zero
    }
    return int(total.Int64), nil
}
```

### Fix 4: Use COALESCE to avoid empty results

```go
// SQL handles NULL/missing rows
var total int
err := db.QueryRow("SELECT COALESCE(SUM(amount), 0) FROM orders WHERE user_id = ?", userID).Scan(&total)
```

## Examples

```go
// This triggers: sql: no rows in result set
package main

import (
    "database/sql"
    "fmt"
    "log"

    _ "github.com/go-sqlite3"
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

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — resource doesn't exist (file equivalent).
- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of data stream.
- [nil-pointer]({{< relref "/languages/go/nil-pointer" >}}) — dereferencing nil after failed lookup.
