---
title: "[Solution] Ruby NoMethodError — Undefined Method Fix"
description: "Fix Ruby NoMethodError: undefined method. Learn why the method doesn't exist on the receiver and how to resolve it."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A `NoMethodError` is raised when you call a method that doesn't exist on an object. The error message tells you the method name, the receiver, and the receiver's class.

## Common Causes

- Calling a method that isn't defined on the object
- Calling a method on `nil` (very common)
- Private method called publicly
- Wrong receiver type for the method

## How to Fix

```ruby
# WRONG: Calling method that doesn't exist
"hello".push("world")  # NoMethodError: undefined method 'push' for "hello":String

# CORRECT: Use appropriate String method
"hello" << "world"  # "helloworld"
```

```ruby
# WRONG: Calling method on nil
user = nil
user.name  # NoMethodError: undefined method 'name' for nil:NilClass

# CORRECT: Use safe navigation operator
user&.name  # nil

# Or provide a default
user&.name || "Anonymous"
```

```ruby
# WRONG: Private method called publicly
class Secret
  private
  def hidden; "secret"; end
end
Secret.new.hidden  # NoMethodError: private method 'hidden' called

# CORRECT: Use send if you must call a private method
Secret.new.send(:hidden)  # "secret"
```

## Examples

```ruby
# Example 1: Nil receiver
data = nil
data.fetch(:key)  # NoMethodError

# Example 2: Wrong object type
arr = [1, 2, 3]
arr.push(4)  # NoMethodError: undefined method 'push' for [1, 2, 3]:Array

# Example 3: Missing module include
module Greeter
  def greet; "Hello!"; end
end
# Object.new.greet  # NoMethodError — module not included
```

## Related Errors

- [NameError](name-error) — undefined variable or constant
- [TypeError](typeerror-ruby) — wrong object type for an operation
- [ArgumentError](argumenterror-ruby) — wrong number of arguments
