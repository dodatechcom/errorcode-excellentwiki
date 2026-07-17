---
title: "[Solution] Ruby ROM Repository Error Fix"
description: "Fix ROM (Ruby Object Mapper) repository errors. Learn why ROM operations fail and how to handle repository errors properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["database-error"]
weight: 5
---

## What This Error Means

A ROM repository error occurs when the Ruby Object Mapper encounters issues with data persistence. ROM uses a repository pattern for data access, and errors can arise from connection, mapping, or query issues.

## Common Causes

- Database connection issues
- Missing or incorrect schema definition
- Type coercion failures
- Relation not configured properly

## How to Fix

```ruby
# WRONG: Missing schema definition
module Repositories
  class Users < ROM::Repository[:users]
    # No commands defined
  end
end

# CORRECT: Define schema and commands
module Repositories
  class Users < ROM::Repository[:users]
    commands :create, update: :by_pk, delete: :by_pk

    def all
      users.to_a
    end
  end
end
```

```ruby
# WRONG: Wrong type coercion
class Users < ROM::Relation[:sql]
  schema(infer: true) do
    attribute :age, Types::Integer  # May fail with string input
  end
end

# CORRECT: Handle type coercion
class Users < ROM::Relation[:sql]
  schema(infer: true) do
    attribute :age, Types::Coercible::Integer
  end
end
```

```ruby
# WRONG: Not handling missing records
repo = Repositories::Users.new(rom)
user = repo.find(999)  # Returns nil, may cause NoMethodError

# CORRECT: Check for nil
user = repo.find(999)
raise "User not found" unless user
```

## Examples

```ruby
# Example 1: ROM setup
ROM.container(:sql, 'sqlite::memory') do |config|
  config.default.create_table(:users) do
    column :id, Integer, primary_key: true
    column :name, String
  end
end

# Example 2: Using repository
repo = Repositories::Users.new(rom)
user = repo.create(name: "Alice")
repo.update(user.id, name: "Bob")

# Example 3: Transactions
rom.transaction do |t|
  t.run { repo.create(name: "Alice") }
  t.run { repo.create(name: "Bob") }
end
```

## Related Errors

- [Sequel database error](sequel-error) — Sequel ORM error
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
- [ActiveRecord::RecordInvalid](activerecord-validation) — validation failed
