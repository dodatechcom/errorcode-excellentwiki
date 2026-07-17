---
title: "[Solution] ActiveRecord::RecordInvalid Error Fix"
description: "Fix ActiveRecord::RecordInvalid when model validations fail during save."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ActiveRecord::RecordInvalid Error Fix

An ActiveRecord::RecordInvalid error occurs when `save!` or `create!` is called and model validations fail.

## What This Error Means

`save!` and `create!` raise `ActiveRecord::RecordInvalid` when validations fail. The error message includes which fields failed validation. `save` (without bang) returns false instead.

## Common Causes

- Required fields missing
- Uniqueness constraint violated
- Format validation failed
- Custom validation logic rejected the record

## How to Fix

### 1. Check validations before saving

```ruby
# WRONG: Using save! without rescue
user = User.new(name: "", email: "")
user.save!  # ActiveRecord::RecordInvalid

# CORRECT: Use save (non-bang) and check result
if user.save
  puts "Saved!"
else
  puts user.errors.full_messages
end
```

### 2. Rescue and handle the error

```ruby
# CORRECT: Rescue RecordInvalid
begin
  user.save!
rescue ActiveRecord::RecordInvalid => e
  puts "Validation failed: #{e.record.errors.full_messages.join(', ')}"
end
```

### 3. Use create with validation

```ruby
# CORRECT: Use create (non-bang) for optional creation
user = User.create(name: "Alice", email: "alice@example.com")
if user.persisted?
  puts "Created: #{user.id}"
else
  puts "Failed: #{user.errors.full_messages}"
end
```

### 4. Validate before building

```ruby
# CORRECT: Check before creating
unless User.exists?(email: params[:email])
  user = User.create!(user_params)
end
```

## Related Errors

- [ActiveRecord::RecordNotFound](activerecord-error-v2) — record missing
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection-v2) — no connection
- [ActiveRecord::MigrationError](activerecord-migration-v2) — migration issues
