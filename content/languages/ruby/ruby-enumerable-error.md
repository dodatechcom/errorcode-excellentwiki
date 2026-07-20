---
title: "[Solution] Ruby Enumerable — Lazy Evaluation, Infinite Enumerables, and take"
description: "Fix Ruby Enumerable errors. Handle infinite collections, lazy evaluation pitfalls, and memory issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, enumerable, lazy, infinite, iterator"]
severity: "error"
---

# Ruby Enumerable Errors

## Error Message

```
NoMethodError: undefined method `lazy' for ...
# or
SystemStackError: stack level too deep
# or memory exhaustion on infinite collections
```

## Common Causes

- Calling non-lazy methods on infinite enumerables (hangs or crashes)
- Forgetting to include Enumerable and implement `each`
- Chain of lazy operations consuming too much memory
- Recursive enumerable calls causing stack overflow

## Solutions

### Solution 1: Use Lazy for Large or Infinite Collections

Wrap expensive operations with `.lazy` to defer evaluation.

```ruby
# BAD: evaluates entire infinite range, hangs
# (1..Float::INFINITY).select { |n| n.even? }.take(5)

# GOOD: lazy evaluation
evens = (1..Float::INFINITY).lazy.select { |n| n.even? }
evens.take(5).to_a  # => [2, 4, 6, 8, 10]

# Chain multiple lazy operations
result = (1..Float::INFINITY).lazy
  .select { |n| n % 3 == 0 }
  .map { |n| n * 2 }
  .take(4)
  .to_a
# => [6, 12, 18, 24]
```

### Solution 2: Include Enumerable and Implement Each

Any class with an `each` method can use all Enumerable methods.

```ruby
class Fibonacci
  include Enumerable

  def each(&block)
    a, b = 0, 1
    loop do
      block.call(a)
      a, b = b, a + b
    end
  end
end

fib = Fibonacci.new
fib.take(6)  # => [0, 1, 1, 2, 3, 5]
fib.select(&:even?).take(4).to_a  # => [0, 2, 8, 34]
```

### Solution 3: Avoid Stack Overflow with Recursive Enumerables

Use iterative approaches or `Enumerator` for deeply nested enumerable chains.

```ruby
# BAD: recursive flatten can cause stack overflow
nested = [[1, [2, [3, [4, [5]]]]]]
nested.flatten  # => works, but very deep nesting can blow the stack

# GOOD: use Enumerator for deep flattening
def deep_flatten(enum)
  Enumerator.new do |yielder|
    enum.each do |item|
      if item.is_a?(Enumerable)
        deep_flatten(item).each { |i| yielder.yield i }
      else
        yielder.yield item
      end
    end
  end
end

deep_flatten([[1, [2, [3]]], 4]).to_a  # => [1, 2, 3, 4]
```

### Solution 4: Use Enumerable Methods Efficiently

Choose the right method to avoid unnecessary computation.

```ruby
# Use find instead of select + first
(1..Float::INFINITY).find { |n| n > 100 && n.prime? }  # => 101

# Use reduce for accumulation
(1..10).reduce(0, :+)  # => 55

# Use each_with_object for building collections
(1..5).each_with_object([]) { |n, arr| arr << n * 2 }
# => [2, 4, 6, 8, 10]

# Use filter_map for compact mapping (Ruby 2.7+)
(1..10).filter_map { |n| n.even? ? n * 10 : nil }
# => [20, 40, 60, 80, 100]
```

## Prevention Tips

- Use `.lazy` before `.select`, `.map`, or `.filter` on large/infinite collections
- Include `Enumerable` in custom classes and implement `each`
- Use `filter_map` (Ruby 2.7+) instead of `select` + `map` chains
- Test with large datasets to catch memory issues early

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
- [SystemStackError]({{< relref "/languages/ruby/stack-level-too-deep" >}})
- [Ruby Enumerator Error]({{< relref "/languages/ruby/ruby-enumerator-error" >}})
