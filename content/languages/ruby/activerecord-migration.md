---
title: "[Solution] Ruby ActiveRecord::MigrationError Fix"
description: "Fix ActiveRecord::MigrationError in Rails. Learn why migrations fail and how to resolve migration conflicts."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An `ActiveRecord::MigrationError` is raised when there's a problem with database migrations. This can happen due to pending migrations, conflicting migration versions, or migration file issues.

## Common Causes

- Pending migrations not yet run
- Migration file name conflicts
- Migration version mismatch
- Database schema out of sync

## How to Fix

```ruby
# WRONG: Ignoring pending migrations
# Running app without running pending migrations
User.all  # MigrationError: Migrations are pending

# CORRECT: Run pending migrations
rails db:migrate
```

```ruby
# WRONG: Migration version conflict
# Two migrations with same timestamp
20240101000001_create_users.rb
20240101000001_create_posts.rb  # Conflict!

# CORRECT: Use unique timestamps
20240101000001_create_users.rb
20240101000002_create_posts.rb
```

```ruby
# WRONG: Migration references non-existent table
class AddEmailToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :nonexistent_table, :email, :string
  end
end

# CORRECT: Ensure table exists first
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :name
      t.timestamps
    end
  end
end
```

## Examples

```ruby
# Example 1: Check pending migrations
ActiveRecord::Migration.check_all_pending!

# Example 2: Status of migrations
rails db:migrate:status

# Example 3: Rollback last migration
rails db:rollback STEP=1
```

## Related Errors

- [ActiveRecord::RecordNotFound](activerecord-error) — record not found
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
- [ActiveRecord::RecordInvalid](activerecord-validation) — validation failed
