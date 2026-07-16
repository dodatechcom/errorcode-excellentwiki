---
title: "[Solution] Ruby ArgumentError — Wrong Number of Arguments Fix"
description: "Fix Ruby ArgumentError: wrong number of arguments. Learn how to handle argument validation and default parameters in Ruby methods."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["argumenterror", "wrong-number-of-arguments", "method-arguments", "ruby"]
weight: 5
---

# ArgumentError — Wrong Number of Arguments

An `ArgumentError` is raised when a method receives a different number of arguments than it expects.

## Description

Ruby methods have strict argument requirements. When you call a method with too many or too few arguments, Ruby raises an `ArgumentError`. This error also occurs when arguments fail validation checks.

Common causes:

- **Wrong argument count** — passing more or fewer arguments than defined
- **Missing required arguments** — not providing mandatory parameters
- **Invalid argument values** — arguments that fail validation
- **Incorrect splat usage** — misunderstanding `*args` behavior

## Common Causes

```ruby
# Cause 1: Wrong number of arguments
def greet(name)
  "Hello, #{name}!"
end
greet("Alice", "Bob")  # ArgumentError: wrong number of arguments (given 2, expected 1)

# Cause 2: Missing required arguments
def divide(a, b)
  a / b
end
divide(10)  # ArgumentError: wrong number of arguments (given 0, expected 2)

# Cause 3: Invalid argument values
def set_age(age)
  raise ArgumentError, "Age must be positive" unless age > 0
end
set_age(-5)  # ArgumentError: Age must be positive

# Cause 4: Hash vs keyword arguments confusion
def configure(host: "localhost", port: 80)
  "#{host}:#{port}"
end
configure(host: "example.com", port: 443)  # OK
configure({host: "example.com", port: 443})  # ArgumentError
```

## How to Fix

### Fix 1: Use default parameters

```ruby
# Wrong
def greet(name)
  "Hello, #{name}!"
end

# Correct
def greet(name = "World")
  "Hello, #{name}!"
end
greet  # "Hello, World!"
greet("Alice")  # "Hello, Alice!"
```

### Fix 2: Use optional arguments with splat

```ruby
# Wrong
def sum(a, b)
  a + b
end

# Correct
def sum(*args)
  args.reduce(0, :+)
end
sum(1, 2, 3)  # 6
```

### Fix 3: Validate arguments explicitly

```ruby
# Wrong
def set_age(age)
  # No validation
end

# Correct
def set_age(age)
  raise ArgumentError, "Age must be a positive integer" unless age.is_a?(Integer) && age > 0
end
```

### Fix 4: Use keyword arguments

```ruby
# Wrong
def configure(options)
  # Hash-based
end

# Correct
def configure(host: "localhost", port: 80)
  "#{host}:#{port}"
end
```

## Examples

```ruby
# Example 1: Variable argument count
def flexible(*args)
  "Received #{args.length} arguments: #{args.join(', ')}"
end
flexible("a")  # "Received 1 arguments: a"
flexible("a", "b")  # "Received 2 arguments: a, b"

# Example 2: Required and optional
def create_user(name, email, role: "viewer")
  "#{name} (#{email}) - #{role}"
end
create_user("Alice", "alice@example.com")  # "Alice (alice@example.com) - viewer"
```

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}}) — undefined method for object
- [TypeError]({{< relref "/languages/ruby/typeerror-ruby" >}}) — wrong object type for an operation
- [KeyError]({{< relref "/languages/ruby/keyerror-ruby" >}}) — key not found in hash
