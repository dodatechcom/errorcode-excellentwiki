---
title: "[Solution] Ruby NoMethodError — Undefined Method Fix"
description: "Fix Ruby NoMethodError: undefined method. Learn why Ruby raises this error and how to resolve it with method checks and safe navigation."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nomethoderror", "undefined-method", "method", "ruby"]
weight: 5
---

# NoMethodError — Undefined Method

A `NoMethodError` is raised when you call a method that doesn't exist on an object.

## Description

`NoMethodError` is one of the most common Ruby errors. It occurs when you invoke a method that isn't defined on the receiver, or when you try to call a method on `nil`.

Common causes:

- **Method doesn't exist** — calling a method that isn't defined on the object
- **Nil receiver** — calling a method on `nil` (very common)
- **Wrong receiver type** — calling an Array method on a String
- **Missing module include** — method is defined in a module that isn't included

## Common Causes

```ruby
# Cause 1: Method doesn't exist
"hello".push("world")  # NoMethodError: undefined method 'push' for "hello":String

# Cause 2: Nil receiver
user = nil
user.name  # NoMethodError: undefined method 'name' for nil:NilClass

# Cause 3: Wrong receiver type
[1, 2, 3].hello  # NoMethodError: undefined method 'hello' for [1, 2, 3]:Array

# Cause 4: Private method called publicly
class Secret
  private
  def hidden; "secret"; end
end
Secret.new.hidden  # NoMethodError: private method 'hidden' called
```

## How to Fix

### Fix 1: Use safe navigation operator

```ruby
# Wrong
user = nil
user.name  # NoMethodError

# Correct
user&.name  # nil
user&.name || "Anonymous"
```

### Fix 2: Verify method existence

```ruby
# Check if method exists before calling
if obj.respond_to?(:my_method)
  obj.my_method
end
```

### Fix 3: Use appropriate methods for the type

```ruby
# Wrong
"hello".push("world")  # NoMethodError

# Correct
"hello" << "world"  # "helloworld"
```

### Fix 4: Include required modules

```ruby
module Greeter
  def greet; "Hello!"; end
end

class Person
  include Greeter
end

Person.new.greet  # "Hello!"
```

## Examples

```ruby
# Example 1: Common nil case
data = { name: "Alice" }
result = data[:missing_key]  # nil
result.upcase  # NoMethodError: undefined method 'upcase' for nil:NilClass
result&.upcase  # nil

# Example 2: Array vs String confusion
"hello".length  # 5
[1, 2, 3].length  # 3
"hello".count  # 1
```

## Related Errors

- [NameError]({{< relref "/languages/ruby/name-error" >}}) — undefined variable or constant
- [TypeError]({{< relref "/languages/ruby/type-error" >}}) — wrong object type for an operation
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}}) — wrong number of arguments
