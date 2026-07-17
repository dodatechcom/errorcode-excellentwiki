---
title: "[Solution] Ruby ActiveRecord::RecordNotFound Fix"
description: "Fix ActiveRecord::RecordNotFound in Rails. Learn why record lookups fail and how to handle missing records gracefully."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

An `ActiveRecord::RecordNotFound` is raised when ActiveRecord cannot find a record by its ID. This commonly happens with `find`, `find!`, and `find_by!` methods when no matching record exists.

## Common Causes

- Record was deleted or never existed
- Wrong ID passed to `find`
- Using `find!` instead of `find_by`
- Race condition between check and access

## How to Fix

```ruby
# WRONG: Using find! without rescue
user = User.find!(params[:id])  # ActiveRecord::RecordNotFound if missing

# CORRECT: Use find_by for optional lookup
user = User.find_by(id: params[:id])
render json: { error: "Not found" }, status: :not_found unless user
```

```ruby
# WRONG: Not handling missing record in controller
def show
  @user = User.find(params[:id])  # 404 if missing
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

```ruby
# WRONG: Using find with invalid ID format
User.find("abc")  # ActiveRecord::RecordNotFound

# CORRECT: Validate ID format
id = params[:id].to_i
user = User.find_by(id: id)
```

## Examples

```ruby
# Example 1: find vs find_by
User.find(999)         # ActiveRecord::RecordNotFound
User.find_by(id: 999)  # nil

# Example 2: find! raises, find does not
User.find!(999)        # ActiveRecord::RecordNotFound
User.find(999)         # ActiveRecord::RecordNotFound (find also raises)

# Example 3: find_by with conditions
User.find_by(email: "nonexistent@example.com")  # nil
```

## Related Errors

- [ActiveRecord::RecordInvalid](activerecord-validation) — validation failed
- [ActiveRecord::ConnectionNotEstablished](activerecord-connection) — no database connection
- [ActiveRecord::MigrationError](activerecord-migration) — migration issues
