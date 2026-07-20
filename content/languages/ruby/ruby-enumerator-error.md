---
title: "[Solution] Ruby Enumerator — StopIteration, next, rewind Errors"
description: "Fix Ruby Enumerator errors. Handle StopIteration, next past end, rewind, and external enumeration issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, enumerator, iteration, stop_iteration, lazy"]
severity: "error"
---

# Ruby Enumerator Errors

## Error Message

```
StopIteration: iterator advanced past end
# or
RuntimeError: iterator advanced past end
```

## Common Causes

- Calling `next` on an exhausted Enumerator without rescue
- Using an Enumerator after it has been fully consumed
- Forgetting to rewind before iterating again
- Using external enumeration (`.next`) with a finite collection

## Solutions

### Solution 1: Rescue StopIteration When Calling next

Guard `next` calls with a rescue or check for exhaustion.

```ruby
enum = [1, 2, 3].each

loop do
  puts enum.next
end
# => prints 1, 2, 3 — loop naturally rescues StopIteration

# Manual rescue
begin
  enum = [1, 2].each
  enum.next  # => 1
  enum.next  # => 2
  enum.next  # => raises StopIteration
rescue StopIteration
  puts "exhausted"
end
```

### Solution 2: Use Enumerator::Lazy for Infinite Sequences

Avoid computing entire collections when processing large or infinite enumerables.

```ruby
# BAD: creates infinite array, hangs
# (1..Float::INFINITY).select { |n| n.prime? }.first(5)

# GOOD: lazy evaluation
primes = (2..Float::INFINITY).lazy.select { |n| n.prime? }
primes.first(5)  # => [2, 3, 5, 7, 11]

# Chain lazy operations
result = (1..Float::INFINITY).lazy
  .select { |n| n.even? }
  .map { |n| n * n }
  .first(5)
# => [4, 16, 36, 64, 100]
```

### Solution 3: Rewind and Reuse Enumerators

Use `rewind` to reset an Enumerator, or use `each` for re-iteration.

```ruby
enum = [1, 2, 3].each
enum.to_a  # => [1, 2, 3]
enum.next  # => raises StopIteration

enum.rewind
enum.to_a  # => [1, 2, 3] again

# Or create a new enumerator each time
def fresh_enum
  [1, 2, 3].each
end

fresh_enum.to_a  # => [1, 2, 3]
fresh_enum.to_a  # => [1, 2, 3] (new enumerator)
```

### Solution 4: Create Custom Enumerators with Enumerator.new

Build enumerators that yield values on demand using a block.

```ruby
fibonacci = Enumerator.new do |yielder|
  a, b = 0, 1
  loop do
    yielder.yield a
    a, b = b, a + b
  end
end

fibonacci.take(8)  # => [0, 1, 1, 2, 3, 5, 8, 13]

# External iteration
enum = fibonacci
puts enum.next  # => 0
puts enum.next  # => 1
```

## Prevention Tips

- Use `loop { ... enum.next ... }` which automatically rescues StopIteration
- Prefer `Enumerator::Lazy` for large or infinite sequences
- Use `rewind` if you need to iterate the same enumerator multiple times
- Consider using `each` instead of `next` when you don't need external iteration

## Related Errors

- [StopIteration]({{< relref "/languages/ruby/ruby-enumerator-error" >}})
- [RuntimeError]({{< relref "/languages/ruby/runtime-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
