---
title: "[Solution] ActiveRecord::MigrationError Fix"
description: "Fix ActiveRecord migration errors when running or creating Rails migrations."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ActiveRecord::MigrationError Fix

An ActiveRecord::MigrationError occurs when a migration cannot be executed due to schema issues, conflicting migrations, or invalid migration code.

## What This Error Means

Migrations modify the database schema. Errors occur when migration files are invalid, versions conflict, or the migration tries to do something impossible (like adding a column that already exists).

## Common Causes

- Migration file has syntax errors
- Conflicting migration versions
- Adding column that already exists
- Migration references non-existent table
- Pending migrations blocking new ones

## How to Fix

### 1. Check migration status

```ruby
# CORRECT: See pending migrations
rails db:migrate:status

# Run pending migrations
rails db:migrate
```

### 2. Fix migration syntax

```ruby
# WRONG: Invalid migration
class AddUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :email, :string  # Wrong: no block
  end
end

# CORRECT: Proper migration structure
class AddUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :name, null: false
      t.string :email, null: false
      t.timestamps
    end
    add_index :users, :email, unique: true
  end
end
```

### 3. Handle existing columns

```ruby
# CORRECT: Check before adding
class AddEmailToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :email, :string unless column_exists?(:users, :email)
  end
end
```

### 4. Rollback and fix

```ruby
# CORRECT: Rollback last migration
rails db:rollback

# Fix the migration file, then re-run
rails db:migrate
```

## Related Errors

- [ActiveRecord::RecordNotFound](activerecord-error-v2) — record missing
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection-v2) — no connection
- [ActiveRecord::RecordInvalid](activerecord-validation-v2) — validation failed
