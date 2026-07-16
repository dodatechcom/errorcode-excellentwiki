---
title: "[Solution] Ruby NoMethodError — Undefined Method Fix"
description: "Fix Ruby NoMethodError: undefined method. Check method existence, receiver type, and include required modules."
languages: ["ruby"]
severities: ["error"]
error_types: ["no-method"]
tags: ["nomethoderror", "method", "undefined", "receiver"]
weight: 50
---

# NoMethodError — Undefined Method Fix

A `NoMethodError` is raised when you call a method that doesn't exist on an object. The error message tells you the method name, the receiver, and suggests similar methods.

## Description

`NoMethodError` is one of the most common Ruby errors. It means the object you're calling a method on doesn't have that method available in its current context.

Common scenarios:

- **Method doesn't exist** — calling a method that isn't defined.
- **Wrong receiver** — calling an Array method on a String.
- **Missing include** — method defined in a module that isn't included.
- **Private method called publicly** — method exists but isn't accessible.
- **Nil receiver** — calling a method on nil (very common).

## Common Causes

```ruby
# Cause 1: Method doesn't exist
"hello".push("world")  # NoMethodError: undefined method 'push' for "hello":String

# Cause 2: Nil receiver
user = nil
user.name  # NoMethodError: undefined method 'name' for nil:NilClass

# Cause 3: Private method called publicly
class Secret
  private
  def hidden; "secret"; end
end
Secret.new.hidden  # NoMethodError: private method 'hidden' called

# Cause 4: Missing module include
module Greeter
  def greet
    "Hello!"
  end
end
# Object.new.greet  # NoMethodError — module not included
```

## Solutions

### Fix 1: Check if the method exists

```ruby
# Wrong
"hello".push("world")  # NoMethodError

# Correct — use appropriate String method
"hello" << "world"  # "helloworld"
"hello".concat(" world")  # "hello world"
```

### Fix 2: Handle nil with safe navigation

```ruby
# Wrong
user = nil
user.name  # NoMethodError

# Correct
user&.name  # nil (safe navigation operator)

# Or provide a default
user&.name || "Anonymous"
```

### Fix 3: Include the module

```ruby
module Greeter
  def greet
    "Hello!"
  end
end

class Person
  include Greeter  # Include the module
end

Person.new.greet  # "Hello!"
```

### Fix 4: Call private methods with send

```ruby
class Secret
  private
  def hidden; "secret"; end
end

# If you must call a private method
Secret.new.send(:hidden)  # "secret"
```

## Related Errors

- [NameError](name-error) — undefined variable or constant.
- [TypeError](type-error) — wrong object type for an operation.
- [ArgumentError](argument-error) — wrong number of arguments.
