---
title: "[Solution] Ruby RuntimeError — Runtime Error Fix"
description: "Fix Ruby RuntimeError. Learn about the base class for runtime errors and how to handle raised exceptions properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["runtimeerror", "runtime", "exception", "ruby"]
weight: 5
---

## What This Error Means

A `RuntimeError` is the default exception raised by Ruby's `raise` method without specifying an exception class. It's the base class for many runtime errors, including `FrozenError`.

## Common Causes

- Calling `raise` without specifying an exception class
- Explicitly raised errors with `raise "message"`
- Frozen object modification (now `FrozenError` but inherits from `RuntimeError`)
- Application-level error conditions

## How to Fix

```ruby
# WRONG: Raising generic RuntimeError
def process(data)
  raise "Invalid data" if data.nil?
end

# CORRECT: Use specific exception classes
class InvalidDataError < StandardError; end

def process(data)
  raise InvalidDataError, "Invalid data" if data.nil?
end
```

```ruby
# WRONG: Catching all errors generically
begin
  risky_operation
rescue RuntimeError => e
  puts e.message
end

# CORRECT: Catch specific exceptions
begin
  risky_operation
rescue InvalidDataError => e
  handle_invalid_data(e)
rescue NetworkError => e
  handle_network_error(e)
end
```

```ruby
# WRONG: Not cleaning up resources
begin
  file = File.open("data.txt")
  process(file)
rescue => e
  puts e.message
  # File never closed!
end

# CORRECT: Use ensure for cleanup
begin
  file = File.open("data.txt")
  process(file)
rescue => e
  puts e.message
ensure
  file&.close
end
```

## Examples

```ruby
# Example 1: Raising RuntimeError
begin
  raise "Something went wrong"
rescue RuntimeError => e
  puts e.message  # "Something went wrong"
end

# Example 2: Custom error inheriting from RuntimeError
class AppError < RuntimeError; end
raise AppError, "Application error"

# Example 3: Nested error handling
begin
  begin
    raise "inner error"
  rescue => e
    raise "outer error: #{e.message}"
  end
rescue => e
  puts e.message  # "outer error: inner error"
end
```

## Related Errors

- [FrozenError](frozenerror-ruby) — can't modify frozen object
- [ArgumentError](argumenterror-ruby) — wrong number of arguments
- [TypeError](typeerror-ruby) — wrong type for operation
