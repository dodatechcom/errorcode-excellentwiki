---
title: "[Solution] Rails Migration Error — How to Fix"
description: "Fix Rails database migration errors. Resolve migration file conflicts, schema drift, and rollback failures in Rails."
frameworks: ["rails"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails migration error occurs when a database migration cannot be applied, rolled back, or conflicts with the current schema state. These errors block deployments and can corrupt your database if not handled carefully.

## Why It Happens

Migration errors happen due to conflicting migration versions, missing columns or tables, incorrect SQL syntax, or schema_migrations table mismatches. They are common when multiple developers create migrations simultaneously or when manual database changes bypass Rails.

## Common Error Messages

```
ActiveRecord::MigrationError: Table already exists
```

```
ActiveRecord::IrreversibleMigration: This migration is not reversible
```

```
PG::UndefinedTable: ERROR: relation "users" does not exist
```

```
ActiveRecord::ConcurrentMigrationError: Another migration is running
```

## How to Fix It

### 1. Check Migration Status

Run `rails db:migrate:status` to see which migrations are pending, applied, or conflicting.

```bash
rails db:migrate:status
```

### 2. Fix Conflicting Migrations

Rename or reorder migration files to resolve timestamp conflicts.

```bash
# Rename with later timestamp
mv db/migrate/20240101_create_users.rb db/migrate/20240102_create_users.rb
rails db:migrate
```

### 3. Rollback and Re-run

Roll back the failed migration, fix the issue, and re-run.

```bash
rails db:rollback STEP=3
# Fix the migration file
rails db:migrate
```

### 4. Reset Database in Development

When the development database is corrupted, reset it entirely (never in production).

```bash
rails db:drop db:create db:schema:load db:seed
```

## Common Scenarios

**Scenario 1: Migration fails after merge.**
Two developers created migrations with the same timestamp prefix. Rename the later file with a higher timestamp and re-run `rails db:migrate`.

**Scenario 2: IrreversibleMigration on rollback.**
Add a reversible `down` block: `def down; drop_table :users; end`.

**Scenario 3: Schema drift between environments.**
Compare `rails db:schema:dump` output across environments and reconcile differences.

## Prevent It

1. **Use timestamp-based naming.**
Always use `rails generate migration CreateUsers` to get unique timestamps. Never manually create files.

2. **Test migrations on a clean DB.**
Run `rails db:drop db:create db:migrate` in CI to verify all migrations apply cleanly.

3. **Never edit a committed migration.**
Create a new migration instead. Editing committed migrations causes schema drift.

