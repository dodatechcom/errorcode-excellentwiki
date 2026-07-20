---
title: "[Solution] Ruby Block Errors — Missing Block, yield, block_given?"
description: "Fix Ruby block errors. Handle missing blocks, &:method shorthand, yield, and block_given? issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, block, yield, proc, block_given"]
severity: "error"
---

# Ruby Block Errors

## Error Message

```
LocalJumpError: no block given (yield)
# or
ArgumentError: wrong number of arguments
```

## Common Causes

- Calling `yield` when no block was passed to the method
- Confusing `&block` (captures a block) with `yield` (invokes a passed block)
- Using `&:method` shorthand with methods that require arguments
- Passing a lambda where a block is expected without `&`

## Solutions

### Solution 1: Use block_given? Before Yielding

Always guard `yield` with `block_given?` or provide a default block path.

```ruby
def greet(name)
  return "Hello, #{name}!" unless block_given?
  yield(name)
end

greet("Alice")                     # => "Hello, Alice!"
greet("Alice") { |n| "Hi #{n}!" }  # => "Hi Alice!"

# Common pattern: provide default behavior
def fetch(key, &block)
  if block_given?
    yield(key)
  else
    defaults[key]
  end
end
```

### Solution 2: Use &block to Capture and Call Blocks

Use `&block` parameter to store a block and call it explicitly.

```ruby
def repeat(times, &block)
  times.times { block.call }
end

repeat(3) { puts "hello" }

# Store block for later
def later(&block)
  @deferred_block = block
end

later { puts "deferred" }
@deferred_block.call  # => "deferred"
```

### Solution 3: Use &:method Shorthand Correctly

The `&:method` shorthand works with no-argument methods; for arguments, use a lambda or block.

```ruby
# &:method works for zero-argument methods
%w[hello world].map(&:upcase)  # => ["HELLO", "WORLD"]

# For methods with arguments, use a block
%w[hello world].map { |w| w.ljust(10, ".") }
# => ["hello.....", "world....."]

# Or use curry
pad = method(:ljust).curry(2).(".")
%w[hello world].map(&pad)
```

### Solution 4: Pass Blocks to Methods Using Lambda or Proc.new

Convert a Proc or lambda to a block using `&`.

```ruby
my_proc = Proc.new { |x| x * 2 }

# Pass proc as block
[1, 2, 3].map(&my_proc)  # => [2, 4, 6]

# Convert lambda to block
my_lambda = lambda { |x| x.to_s }
%w[a b c].map(&my_lambda)  # => ["a", "b", "c"]

# Or use Proc.new to capture the calling method's block
def wrapper(&block)
  Proc.new(&block)  # re-wraps the block
end
```

## Prevention Tips

- Always use `block_given?` before `yield` to avoid LocalJumpError
- Prefer `&block` parameter over `yield` when you need to pass the block around
- Remember `&:symbol` is shorthand only for zero-argument methods
- Test methods both with and without blocks to ensure they handle both cases

## Related Errors

- [LocalJumpError]({{< relref "/languages/ruby/local-jump-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
