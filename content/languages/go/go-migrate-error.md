---
title: "[Solution] golang-migrate Migration Error Fix"
description: "Fix golang-migrate migration errors. Handle schema changes, version conflicts, and rollback failures."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# golang-migrate Migration Error

The `golang-migrate` library fails when migration files have syntax errors, the database connection drops mid-migration, a migration is applied twice, or the migration version does not match the expected state. Migrations must be idempotent and reversible.

## Common Causes

```go
// Cause 1: Migration SQL syntax error
// 000001_create_users.up.sql
// CREATE TABLE users (id INT PRIMARY KEY,);  -- trailing comma

// Cause 2: Database connection drops mid-migration
m, err := migrate.NewWithDatabaseInstance(
    "file://migrations",
    "postgres",
    dbInstance,
)
err = m.Up() // connection lost — migration partially applied

// Cause 3: Migration applied twice
// Running migrate.Up() twice — table already exists

// Cause 4: Down migration not implemented
// 000001_create_users.down.sql is empty
// migrate.Down() does nothing

// Cause 5: Migration version conflict
// Database at version 3, migration file has version 5
// skipping versions 4 — may miss schema changes
```

## How to Fix

### Fix 1: Use proper migration file structure

```sql
-- 000001_create_users.up.sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 000001_create_users.down.sql
DROP TABLE IF EXISTS users;
```

### Fix 2: Handle migration errors with proper connection

```go
import (
    "github.com/golang-migrate/migrate/v4"
    _ "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/file"
)

func runMigration(dbURL string) error {
    m, err := migrate.New("file://migrations", dbURL)
    if err != nil {
        return fmt.Errorf("create migrate instance: %w", err)
    }
    defer m.Close()

    if err := m.Up(); err != nil && err != migrate.ErrNoChange {
        return fmt.Errorf("migrate up: %w", err)
    }

    version, dirty, _ := m.Version()
    fmt.Printf("Migration version: %d, dirty: %v\n", version, dirty)
    return nil
}
```

### Fix 3: Use programmatic migration for complex changes

```go
func migrateUp(db *sql.DB) error {
    // Check current version
    var version int
    db.QueryRow("SELECT version FROM schema_migrations ORDER BY version DESC LIMIT 1").Scan(&version)

    if version >= 3 {
        return nil // already up to date
    }

    // Apply migration
    _, err := db.Exec(`
        ALTER TABLE users ADD COLUMN IF NOT EXISTS phone VARCHAR(20);
    `)
    return err
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "github.com/golang-migrate/migrate/v4"
    _ "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/file"
)

func main() {
    m, err := migrate.New(
        "file://migrations",
        "postgres://user:pass@localhost:5432/mydb?sslmode=disable",
    )
    if err != nil {
        log.Fatal(err)
    }
    defer m.Close()

    if err := m.Up(); err != nil && err != migrate.ErrNoChange {
        log.Fatal(err)
    }

    fmt.Println("Migration completed successfully")
}
```

## Related Errors

- [go-pgerror]({{< relref "/languages/go/go-pgerror" >}}) — PostgreSQL errors during migration
- [go-mysql-error]({{< relref "/languages/go/go-mysql-error" >}}) — MySQL errors during migration
- [sql-no-rows]({{< relref "/languages/go/sql-no-rows-2" >}}) — no schema_migrations table
