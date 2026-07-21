---
title: "[Solution] Deprecated Function Migration: instance_variable_get/set to attr accessors"
description: "Migrate from deprecated instance_variable_get/set to attr_accessor in Ruby."
deprecated_function: "obj.instance_variable_get(:@name)"
replacement_function: "obj.name"
languages: ["ruby"]
deprecated_since: "Ruby 1.9+"
---

# [Solution] Deprecated Function Migration: instance_variable_get/set to attr accessors

The `obj.instance_variable_get(:@name)` has been deprecated in favor of `obj.name`.

## Migration Guide

Use attr_accessor, attr_reader, or attr_writer instead of direct instance variable access.

## Before (Deprecated)

```ruby
class User
    def initialize(name)
        @name = name
    end
end

user = User.new("Alice")
user.instance_variable_get(:@name)
user.instance_variable_set(:@name, "Bob")
```

## After (Modern)

```ruby
class User
    attr_accessor :name

    def initialize(name)
        @name = name
    end
end

user = User.new("Alice")
user.name      # getter
user.name = "Bob"  # setter
```

## Key Differences

- attr_accessor creates getter and setter
- attr_reader creates getter only
- attr_writer creates setter only
- Much cleaner than instance_variable_get/set
