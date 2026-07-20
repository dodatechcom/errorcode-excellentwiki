---
title: "[Solution] Ruby Proc vs Lambda — Arity, Return Behavior, and Mismatch Errors"
description: "Fix Ruby Proc and Lambda errors. Understand arity mismatch, return behavior differences, and argument passing issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, proc, lambda, arity, block"]
severity: "error"
---

# Proc vs Lambda Errors

## Error Message

```
ArgumentError: wrong number of arguments (given 2, expected 1)
# or
LocalJumpError: unexpected return
```

## Common Causes

- Confusing Proc and lambda return semantics (`return` in Proc exits the enclosing method)
- Passing wrong number of arguments to a strict-arity lambda
- Using `&block` with a lambda that rejects extra or missing arguments
- Passing a Proc where a lambda is expected for strict arity checking

## Solutions

### Solution 1: Understand Proc vs Lambda Return Behavior

Procs return from their enclosing method; lambdas return only from themselves.

```ruby
def test_proc
  p = Proc.new { return "from proc" }
  p.call
  "from method"
end

test_proc  # => "from proc" (exits the method entirely)

def test_lambda
  l = lambda { return "from lambda" }
  l.call
  "from method"
end

test_lambda  # => "from method" (return exits only the lambda)
```

### Solution 2: Handle Arity Mismatch with Splat Arguments

Lambdas enforce strict argument counts; Procs are lenient. Use splat to make lambdas flexible.

```ruby
# Lambda enforces arity
strict_add = lambda { |a, b| a + b }
strict_add.call(1, 2, 3)  # ArgumentError: wrong number of arguments
strict_add.call(1)         # ArgumentError: wrong number of arguments

# Use splat for variable arguments
flexible_add = lambda { |*args| args.sum }
flexible_add.call(1, 2, 3)  # => 6
flexible_add.call(1)         # => 1

# Proc is lenient with arity
p = Proc.new { |a, b| [a, b] }
p.call(1, 2, 3)  # => [1, 2] (ignores extra)
p.call(1)         # => [1, nil] (missing arg becomes nil)
```

### Solution 3: Convert Proc to Lambda When Needed

Use `Proc#curry` or `method(:name)` to enforce strict argument checking on procs.

```ruby
# A proc that should be strict
my_proc = Proc.new { |a, b| a + b }

# Convert to lambda behavior using curry
my_lambda = my_proc.curry
my_lambda.call(1).call(2)  # => 3 (proper currying)

# Or define a proper lambda
my_strict_lambda = lambda { |a, b| a + b }

# Check if something is a lambda
my_proc.lambda?  # => false
my_strict_lambda.lambda?  # => true
```

### Solution 4: Use block_given? and Safe Block Passing

Pass blocks safely using `&` and check presence before calling.

```ruby
def process(&block)
  return "no block given" unless block
  block.call("data")
end

process { |d| "processed #{d}" }  # => "processed data"
process                             # => "no block given"

# Store and call later
def wrap_block(&block)
  wrapper = lambda { |*args| block.call(*args) }
  wrapper
end

fn = wrap_block { |x| x * 2 }
fn.call(5)  # => 10
```

## Prevention Tips

- Prefer lambdas for strict arity checking and predictable return behavior
- Use `Proc#lambda?` to distinguish procs from lambdas in shared code
- Avoid `return` inside Procs unless you intentionally want to exit the enclosing method
- Pass blocks with `&` and store as `lambda {}` for later invocation

## Related Errors

- [LocalJumpError]({{< relref "/languages/ruby/local-jump-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [TypeError]({{< relref "/languages/ruby/type-error" >}})
