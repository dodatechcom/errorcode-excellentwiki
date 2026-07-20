---
title: "[Solution] sqlx Named Query Error Fix"
description: "Fix sqlx named query errors. Handle named parameters, struct binding, and query execution."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# sqlx Named Query Error

The `jmoiron/sqlx` library fails on named queries when parameter names don't match struct field names, the struct tag is missing or wrong, or named parameters use incorrect syntax. sqlx extends `database/sql` with struct scanning and named parameters, which introduces new failure modes.

## Common Causes

```go
// Cause 1: Struct tag missing or wrong name
type User struct {
    ID   int    // sqlx expects `db:"id"` tag
    Name string // maps to column "name" without tag
}
// SELECT id, name FROM users WHERE id = :id
// sqlx cannot bind :id to User struct without `db:"id"` tag

// Cause 2: Named parameter syntax wrong
db.Queryx("SELECT * FROM users WHERE name = :name", sqlx.Named("name", "Alice"))
// If using Query instead of Queryx, named params not expanded

// Cause 3: Using QueryRowx with multiple results
row := db.QueryRowx("SELECT * FROM users")
// returns only first row, may miss expected data

// Cause 4: Named struct embedding issues
type Base struct {
    ID int `db:"id"`
}
type User struct {
    Base
    Name string `db:"name"`
}
// Named query with :id works, but :base.id does not

// Cause 5: NamedExec with pointer vs value
db.NamedExec("INSERT INTO users (name) VALUES (:name)", &user) // pointer works
db.NamedExec("INSERT INTO users (name) VALUES (:name)", user)  // value also works
// But: NamedExec("INSERT INTO users (name) VALUES (:name)", *user) — pointer dereferenced
```

## How to Fix

### Fix 1: Add proper db tags to all struct fields

```go
import (
    "fmt"
    "log"

    "github.com/jmoiron/sqlx"
    _ "github.com/go-sql-driver/mysql"
)

type User struct {
    ID    int    `db:"id"`
    Name  string `db:"name"`
    Email string `db:"email"`
    Age   int    `db:"age"`
}

func getUser(db *sqlx.DB, id int) (*User, error) {
    var u User
    err := db.Get(&u, "SELECT * FROM users WHERE id = ?", id)
    if err != nil {
        return nil, fmt.Errorf("get user: %w", err)
    }
    return &u, nil
}
```

### Fix 2: Use named parameters correctly

```go
type CreateUserInput struct {
    Name  string `db:"name" json:"name"`
    Email string `db:"email" json:"email"`
}

func createUser(db *sqlx.DB, input CreateUserInput) (int64, error) {
    query, args, err := sqlx.Named(
        "INSERT INTO users (name, email) VALUES (:name, :email)",
        input,
    )
    if err != nil {
        return 0, err
    }

    result, err := db.Exec(query, args...)
    if err != nil {
        return 0, err
    }
    return result.LastInsertId()
}
```

### Fix 3: Use StructScan for multiple rows

```go
func listUsers(db *sqlx.DB) ([]User, error) {
    var users []User
    err := db.Select(&users, "SELECT * FROM users WHERE age > ?", 18)
    if err != nil {
        return nil, err
    }
    return users, nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "github.com/jmoiron/sqlx"
    _ "github.com/go-sql-driver/mysql"
)

type User struct {
    ID    int    `db:"id"`
    Name  string `db:"name"`
    Email string `db:"email"`
}

func main() {
    db, err := sqlx.Open("mysql", "root:pass@tcp(127.0.0.1:3306)/testdb")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    users := []User{}
    err = db.Select(&users, "SELECT id, name, email FROM users WHERE age > ?", 18)
    if err != nil {
        log.Fatal(err)
    }

    for _, u := range users {
        fmt.Printf("ID: %d, Name: %s, Email: %s\n", u.ID, u.Name, u.Email)
    }
}
```

## Related Errors

- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — no rows found by query
- [go-mysql-error]({{< relref "/languages/go/go-mysql-error" >}}) — underlying MySQL driver error
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — struct tag mapping issues
