---
title: "[Solution] Ruby ActiveRecord::SerializationError Fix"
description: "Fix ActiveRecord::SerializationError: unsupported type in Rails. Learn why model serialization fails and how to handle unsupported data types."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "ruby"
tags: ["activerecord, serialization, json, rails"]
severity: "error"
---

# ActiveRecord::SerializationError

## Error Message

```
ActiveRecord::SerializationError: unsupported type: Symbol
```

## Common Causes

- Attempting to serialize a type that JSON does not support (Symbol, Range, etc.)
- Passing non-serializable objects to render json with ActiveRecord models
- Including unsupported attributes in as_json or to_json calls
- Custom attributes returning non-JSON-compatible types

## Solutions

### Solution 1: Override as_json to Filter Unsupported Types

Define as_json or a custom serializer method to only include JSON-compatible data types.

```ruby
class User < ApplicationRecord
  # WRONG: Symbol is not JSON-serializable
  def serializable_hash(options = {})
    super.merge(role: :admin)  # SerializationError
  end

  # CORRECT: Convert Symbol to String
  def as_json(options = {})
    super(options).merge("role" => role.to_s)
  end
end

# Usage
User.first.to_json  # => '{"id":1,"role":"admin",...}'
```

### Solution 2: Use ActiveModel::Serializers or jbuilder

Use a serializer gem to explicitly control which attributes and types are included in the JSON output.

```ruby
# Using jbuilder (built into Rails)
# app/views/users/show.json.jbuilder
json.id @user.id
json.name @user.name
json.role @user.role.to_s
json.created_at @user.created_at.iso8601

# Using ActiveModel::Serializers
class UserSerializer < ActiveModel::Serializer
  attributes :id, :name, :role

  def role
    object.role.to_s
  end
end
```

### Solution 3: Sanitize Data Before Serialization

Convert or reject problematic types before calling to_json to prevent the error from occurring.

```ruby
# WRONG: Passing raw model with Symbol attributes
render json: @user

# CORRECT: Sanitize before rendering
def safe_json(model, options = {})
  model.as_json(options).tap do |hash|
    hash.each do |key, value|
      case value
      when Symbol
        hash[key] = value.to_s
      when Range
        hash[key] = value.to_a
      when Time, DateTime
        hash[key] = value.iso8601
      end
    end
  end
end

render json: safe_json(@user)
```

### Solution 4: Handle Date and Time Serialization Properly

Date, Time, and DateTime objects need explicit conversion to strings for JSON serialization.

```ruby
# WRONG: Custom accessor returning Time
class Event < ApplicationRecord
  def occurrence
    starts_at  # Time object — may fail
  end
end

# CORRECT: Return ISO8601 string
class Event < ApplicationRecord
  def occurrence
    starts_at&.iso8601
  end
end

# Or configure globally in an initializer
# config/initializers/json_serialization.rb
ActiveSupport::JSON::Encoding.time_precision = 0
```

## Prevention Tips

- Always convert Symbols, Ranges, and custom objects to strings before JSON serialization
- Use serializers (jbuilder, active_model_serializers) for explicit control
- Test serialization in your test suite with assert_nothing_raised
- Be aware of nil handling — nil is valid JSON but may cause issues if not expected

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [ActiveRecord::RecordInvalid]({{< relref "/languages/ruby/activerecord-validation" >}})
