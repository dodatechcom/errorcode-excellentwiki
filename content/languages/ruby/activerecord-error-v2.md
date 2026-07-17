---
title: "[Solution] ActiveRecord::RecordNotFound Error Fix"
description: "Fix ActiveRecord::RecordNotFound in Rails when record lookups fail."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["activerecord", "record-not-found", "rails", "ruby"]
weight: 5
---

# ActiveRecord::RecordNotFound Error Fix

An ActiveRecord::RecordNotFound error occurs when ActiveRecord cannot find a record by its ID using `find`, `find!`, or `find_by!`.

## What This Error Means

`find` and `find!` raise `ActiveRecord::RecordNotFound` when no matching record exists. This is different from `find_by` which returns nil.

## Common Causes

- Record was deleted or never existed
- Wrong ID passed to `find`
- Race condition between check and access
- Using `find` instead of `find_by` for optional lookups

## How to Fix

### 1. Use find_by for optional lookups

```ruby
# WRONG: find raises if missing
user = User.find(params[:id])  # ActiveRecord::RecordNotFound

# CORRECT: find_by returns nil
user = User.find_by(id: params[:id])
render json: { error: "Not found" }, status: :not_found unless user
```

### 2. Handle missing records in controllers

```ruby
# WRONG: No error handling
def show
  @user = User.find(params[:id])
end

# CORRECT: Handle gracefully
def show
  @user = User.find_by(id: params[:id])
  if @user
    render json: @user
  else
    render json: { error: "User not found" }, status: :not_found
  end
end
```

### 3. Use find with validation

```ruby
# CORRECT: Validate before find
id = params[:id].to_i
if id.positive?
  user = User.find_by(id: id)
end
```

### 4. Use find_by for composite lookups

```ruby
# CORRECT: find_by with multiple conditions
user = User.find_by(email: "alice@example.com", active: true)
```

## Related Errors

- [ActiveRecord::RecordInvalid](activerecord-validation-v2) — validation failed
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection-v2) — no connection
- [ActiveRecord::MigrationError](activerecord-migration-v2) — migration issues
