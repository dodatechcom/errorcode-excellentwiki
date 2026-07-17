---
title: "[Solution] Ruby ArgumentError — Wrong Number of Arguments Fix"
description: "Fix Ruby ArgumentError: wrong number of arguments. Learn why argument count mismatches occur and how to handle optional parameters."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["argumenterror", "arguments", "wrong-number", "ruby"]
weight: 5
---

## What This Error Means

An `ArgumentError` is raised when a method receives an incorrect number of arguments or an argument of an inappropriate type. The error message tells you how many arguments were given versus expected.

## Common Causes

- Passing too many or too few arguments to a method
- Missing required keyword arguments
- Passing wrong type of argument
- Calling super with wrong argument count

## How to Fix

```ruby
# WRONG: Wrong number of arguments
def greet(name, greeting)
  "#{greeting}, #{name}!"
end
greet("Alice")  # ArgumentError: wrong number of arguments (given 1, expected 2)

# CORRECT: Provide all required arguments
greet("Alice", "Hello")  # "Hello, Alice!"
```

```ruby
# WRONG: Missing keyword argument
def create_user(name:, age:)
  { name: name, age: age }
end
create_user(name: "Alice")  # ArgumentError: missing keyword: age

# CORRECT: Provide all keyword arguments or set defaults
def create_user(name:, age: 0)
  { name: name, age: age }
end
create_user(name: "Alice")  # {:name=>"Alice", :age=>0}
```

```ruby
# WRONG: Passing wrong argument type
def add(a, b)
  a + b
end
add("1", 2)  # TypeError, not ArgumentError

# CORRECT: Validate argument types
def add(a, b)
  raise ArgumentError unless a.is_a?(Numeric) && b.is_a?(Numeric)
  a + b
end
```

```ruby
# WRONG: Splat argument mismatch
def process(*args); end
process()       # OK
process(1, 2, 3)  # OK
```

## Examples

```ruby
# Example 1: Wrong count
def sum(a, b, c); a + b + c; end
sum(1, 2)  # ArgumentError: wrong number of arguments (given 2, expected 3)

# Example 2: Too many arguments
"hello".include?  # ArgumentError: wrong number of arguments (given 0, expected 1)

# Example 3: Optional parameters
def log(message, level = :info); end
log("Hello")        # OK
log("Hello", :warn) # OK
```

## Related Errors

- [NoMethodError](nomethoderror-ruby) — undefined method
- [TypeError](typeerror-ruby) — wrong type for operation
- [KeyError](keyerror-ruby) — key not found in hash
