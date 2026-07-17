---
title: "[Solution] Ruby ArgumentError — Wrong Number of Arguments Fix"
description: "Fix Ruby ArgumentError: wrong number of arguments. Correct method signatures and handle optional parameters properly."
languages: ["ruby"]
severities: ["error"]
error_types: ["argument"]
weight: 10
---

# ArgumentError — Wrong Number of Arguments Fix

An `ArgumentError` is raised when a method receives a number of arguments that doesn't match its expected signature.

## Description

Ruby methods have strict argument requirements. An `ArgumentError` occurs when you pass too many or too few arguments to a method. The error message includes the expected range and the actual count received.

Common scenarios:

- **Wrong argument count** — method expects 2 args but receives 1 or 3.
- **Missing required arguments** — required positional argument not provided.
- **Extra arguments** — passing arguments beyond what the method accepts.
- **Wrong argument type** — related but separate; `TypeError` covers type mismatches.

## Common Causes

```ruby
# Cause 1: Missing required argument
def greet(name, greeting)
  puts "#{greeting}, #{name}!"
end
greet("Alice")  # ArgumentError: wrong number of arguments (given 1, expected 2)

# Cause 2: Too many arguments
def add(a, b)
  a + b
end
add(1, 2, 3)  # ArgumentError: wrong number of arguments (given 3, expected 2)

# Cause 3: Incorrect use of splat operator
def sum(*numbers)
  numbers.reduce(:+)
end
sum()  # ArgumentError when reduce is called on empty array

# Cause 4: Calling parent method with wrong arity
class Parent
  def initialize(name, age)
    @name = name
    @age = age
  end
end

class Child < Parent
  def initialize(name)
    super  # ArgumentError: wrong number of arguments (given 0, expected 2)
  end
end
```

## Solutions

### Fix 1: Use default parameter values

```ruby
# Wrong
def greet(name, greeting)
  puts "#{greeting}, #{name}!"
end

# Correct — default value makes greeting optional
def greet(name, greeting = "Hello")
  puts "#{greeting}, #{name}!"
end

greet("Alice")            # "Hello, Alice!"
greet("Alice", "Hi")      # "Hi, Alice!"
```

### Fix 2: Use keyword arguments for clarity

```ruby
# Wrong — positional args are order-dependent
def create_user(name, email, age, role)
  # ...
end

# Correct — keyword args are self-documenting
def create_user(name:, email:, age: nil, role: "user")
  # ...
end

create_user(name: "Alice", email: "alice@example.com")
create_user(name: "Bob", email: "bob@example.com", age: 30, role: "admin")
```

### Fix 3: Use splat and double splat for flexible signatures

```ruby
# Wrong — fixed signature
def log(level, message, *args)
  # ...
end

# Correct — flexible signature
def log(message, **options)
  level = options.fetch(:level, :info)
  puts "[#{level}] #{message}"
end

log("Server started", level: :debug)
log("Request received")
```

### Fix 4: Use super with explicit arguments

```ruby
class Parent
  def initialize(name, age)
    @name = name
    @age = age
  end
end

class Child < Parent
  def initialize(name, age = 0)
    super(name, age)  # Pass arguments explicitly
  end
end
```

## Related Errors

- [TypeError](type-error) — wrong argument type passed to a method.
- [NoMethodError](no-method-error) — method doesn't exist on the object.
- [LocalJumpError](local-jump-error) — missing block where one is expected.
