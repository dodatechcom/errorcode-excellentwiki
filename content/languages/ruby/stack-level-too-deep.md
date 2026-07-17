---
title: "[Solution] Ruby SystemStackError — Stack Level Too Deep Fix"
description: "Fix Ruby SystemStackError: stack level too deep. Resolve infinite recursion and optimize recursive algorithms."
languages: ["ruby"]
severities: ["error"]
error_types: ["stack"]
weight: 320
---

# SystemStackError — Stack Level Too Deep Fix

A `SystemStackError` is raised when the call stack overflows due to too many nested method calls, typically from infinite recursion.

## Description

Ruby has a limited call stack size. When recursive calls exceed this limit, `SystemStackError` is raised. This indicates either infinite recursion or a recursive algorithm that's too deep.

Common scenarios:

- **Infinite recursion** — method calls itself without base case.
- **Mutual recursion** — A calls B, B calls A indefinitely.
- **Deep recursion** — valid recursion but stack limit exceeded.
- **Stack overflow in C extensions** — deep C call stacks.

## Common Causes

```ruby
# Cause 1: Missing base case
def factorial(n)
  factorial(n - 1) * n  # No base case!
end
factorial(5)  # SystemStackError

# Cause 2: Mutual recursion
def a
  b
end
def b
  a  # Infinite loop
end
a  # SystemStackError

# Cause 3: Infinite loop masquerading as recursion
def process(node)
  process(node.parent) if node.parent
end
# If nodes form a cycle, this never terminates

# Cause 4: Method name collision
class Foo
  def process
    process  # Calls itself, no base case
  end
end
```

## Solutions

### Fix 1: Add a base case

```ruby
# Wrong
def factorial(n)
  factorial(n - 1) * n
end

# Correct
def factorial(n)
  return 1 if n <= 1  # Base case
  factorial(n - 1) * n
end
```

### Fix 2: Use iteration instead of recursion

```ruby
# Wrong — recursive
def factorial(n)
  return 1 if n <= 1
  factorial(n - 1) * n
end

# Correct — iterative
def factorial(n)
  result = 1
  (2..n).each { |i| result *= i }
  result
end
```

### Fix 3: Use memoization for repeated calls

```ruby
# Wrong — recalculates same values
def fib(n)
  return n if n <= 1
  fib(n - 1) + fib(n - 2)
end

# Correct — memoized
def fib(n, memo = {})
  return n if n <= 1
  memo[n] ||= fib(n - 1, memo) + fib(n - 2, memo)
end
```

### Fix 4: Increase stack size (use with caution)

```ruby
# Increase stack size (default is usually 1MB)
Thread.new { exec "ruby -KU #{$0}" }

# Or set RUBY_THREAD_VM_STACK_SIZE environment variable
# RUBY_THREAD_VM_STACK_SIZE=16777216 ruby script.rb
```

## Related Errors

- [NoMemoryError](memory-error) — system out of memory.
- [RecursionError](#) — Python equivalent (not in Ruby).
- [ScriptError](script-error) — error in script execution.
