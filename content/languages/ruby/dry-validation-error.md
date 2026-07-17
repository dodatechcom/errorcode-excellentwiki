---
title: "[Solution] Ruby Dry::Validation Error Fix"
description: "Fix Dry::Validation errors in Ruby. Learn why validation contracts fail and how to define proper validation schemas."
languages: ["ruby"]
severities: ["error"]
error-types: ["validation-error"]
tags: ["dry-validation", "validation", "contract", "ruby"]
weight: 5
---

## What This Error Means

A Dry::Validation error occurs when a validation contract rejects input data. Dry::Validation uses a schema-based approach to validate data, and errors include detailed messages about what failed.

## Common Causes

- Required field missing
- Type mismatch (wrong type provided)
- Format validation failed (email, URL, etc.)
- Custom rule rejected the data

## How to Fix

```ruby
# WRONG: Missing required field
class UserContract < Dry::Validation::Contract
  params do
    required(:name).filled(:string)
  end
end

result = UserContract.new.call({})
result.success?  # false
result.errors.to_h  # {name: ["is missing"]}
```

```ruby
# WRONG: Wrong type provided
class AgeContract < Dry::Validation::Contract
  params do
    required(:age).filled(:integer)
  end
end

result = AgeContract.new.call(age: "not a number")
result.errors.to_h  # {age: ["must be an integer"]}

# CORRECT: Handle type coercion
class AgeContract < Dry::Validation::Contract
  params do
    required(:age).filled(:integer)
  end

  rule(:age) do
    key.failure(:invalid) unless value > 0
  end
end
```

```ruby
# WRONG: Custom rule always failing
class EmailContract < Dry::Validation::Contract
  params do
    required(:email).filled(:string)
  end

  rule(:email) do
    key.failure("invalid email") unless value.include?("@")
  end
end

# CORRECT: Use built-in format validation
class EmailContract < Dry::Validation::Contract
  params do
    required(:email).filled(:string, format?: /\A[\w+\-.]+@[a-z\d\-.]+\.[a-z]+\z/i)
  end
end
```

## Examples

```ruby
# Example 1: Basic validation
class UserContract < Dry::Validation::Contract
  params do
    required(:name).filled(:string, min_size?: 2)
    required(:email).filled(:string, format?: /@/)
    optional(:age).value(:integer, gt?: 0)
  end
end

# Example 2: Check result
result = UserContract.new.call(name: "A", email: "bad")
result.success?  # false
result.errors.to_h  # {name: ["size cannot be less than 2"], email: ["is invalid"]}

# Example 3: Custom validation
rule(:email) do
  key.failure(:unique) if User.exists?(email: value)
end
```

## Related Errors

- [ActiveRecord::RecordInvalid](activerecord-validation) — ActiveRecord validation failed
- [Dry::Types error] — type coercion failed
- [ROM repository error](rom-error) — ROM ORM error
