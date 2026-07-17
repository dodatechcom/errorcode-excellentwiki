---
title: "[Solution] Ruby ActiveRecord::RecordInvalid Fix"
description: "Fix ActiveRecord::RecordInvalid in Rails. Learn why model validations fail and how to handle validation errors properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An `ActiveRecord::RecordInvalid` is raised when you call `save!` or `create!` on an ActiveRecord model and the record fails validation. The exception includes the validation errors.

## Common Causes

- Required fields are blank
- Uniqueness constraint violated
- Format validation failed
- Custom validation logic rejected the data

## How to Fix

```ruby
# WRONG: Using save! without rescue
user = User.new(name: "")
user.save!  # ActiveRecord::RecordInvalid: Validation failed: Name can't be blank

# CORRECT: Use save and check errors
user = User.new(name: "")
if user.save
  puts "Saved!"
else
  puts user.errors.full_messages
end
```

```ruby
# WRONG: create! without checking
user = User.create!(name: "")  # Raises if invalid

# CORRECT: Use create and check
user = User.create(name: "")
if user.persisted?
  puts user.id
else
  puts user.errors.full_messages
end
```

```ruby
# WRONG: Ignoring validation errors
def update_user(params)
  @user.update!(params)  # Raises on failure
end

# CORRECT: Handle gracefully
def update_user(params)
  if @user.update(params)
    { success: true }
  else
    { success: false, errors: @user.errors.full_messages }
  end
end
```

## Examples

```ruby
# Example 1: Check validation errors
user = User.new
user.valid?  # false
user.errors.full_messages  # ["Name can't be blank", "Email can't be blank"]

# Example 2: Custom validation
class User < ApplicationRecord
  validate :adult_age

  def adult_age
    errors.add(:age, "must be 18 or older") if age && age < 18
  end
end

# Example 3: Skip validation
user.save!(validate: false)  # Skips validations (dangerous)
```

## Related Errors

- [ActiveRecord::RecordNotFound](activerecord-error) — record not found
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no DB connection
- [ActiveRecord::MigrationError](activerecord-migration) — migration issues
