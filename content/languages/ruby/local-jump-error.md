---
title: "[Solution] Ruby LocalJumpError — Missing Block Fix"
description: "Fix Ruby LocalJumpError: block missing. Pass blocks to methods that expect them and use block_given? to check."
languages: ["ruby"]
severities: ["error"]
error_types: ["block"]
tags: ["local_jump_error", "block", "yield", "missing_block"]
weight: 360
---

# LocalJumpError — Missing Block Fix

A `LocalJumpError` is raised when a method expects a block but none is given, or when `yield` is called without a block.

## Description

`LocalJumpError` occurs when Ruby tries to yield to a block that doesn't exist. This happens when a method uses `yield` but isn't called with a block.

Common scenarios:

- **yield without block** — method calls `yield` but no block passed.
- **Method requires block** — method expects a block argument.
- **break/next outside block** — `break` or `next` used outside a block.
- **return in block** — `return` from within a block.

## Common Causes

```ruby
# Cause 1: yield without block
def greet
  yield("Hello")
end
greet  # LocalJumpError: no block given (yield)

# Cause 2: Method expects block
def process
  yield
end
process  # LocalJumpError

# Cause 3: break outside block
def foo
  break  # LocalJumpError: break from proc-closure
end

# Cause 4: next outside block
def bar
  next  # LocalJumpError: unexpected next
end
```

## Solutions

### Fix 1: Check if block is given

```ruby
# Wrong
def greet
  yield("Hello")
end

# Correct
def greet
  if block_given?
    yield("Hello")
  else
    "Hello, World!"
  end
end

greet                  # "Hello, World!"
greet { |g| g.upcase } # "HELLO"
```

### Fix 2: Use block parameter with default

```ruby
# Wrong
def greet
  yield("Hello")
end

# Correct
def greet(&block)
  block ? block.call("Hello") : "Hello, World!"
end
```

### Fix 3: Use Proc or Lambda for safe yielding

```ruby
# Wrong
def greet
  yield("Hello")
end

# Correct
def greet
  block = Proc.new { |g| g }
  block.call("Hello")
end
```

### Fix 4: Use ensure_block_given pattern

```ruby
def greet
  raise LocalJumpError, "Block required" unless block_given?
  yield("Hello")
end
```

## Related Errors

- [ArgumentError](argument-error) — wrong number of arguments.
- [NoMethodError](no-method-error) — undefined method.
- [RuntimeError](runtime-error) — generic runtime error.
