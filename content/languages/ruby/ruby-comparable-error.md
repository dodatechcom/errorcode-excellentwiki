---
title: "[Solution] Ruby Comparable Mixin — <=> Returns nil, Comparison Failures"
description: "Fix Ruby Comparable errors. Handle nil from spaceship operator, comparison failures, and mixin issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, comparable, comparison, spaceship, mixin"]
severity: "error"
---

# Ruby Comparable Errors

## Error Message

```
ArgumentError: comparison of String with nil failed
# or
ArgumentError: comparison of Integer with String failed
```

## Common Causes

- `<=>` (spaceship operator) returning `nil` when types are incomparable
- Comparing objects of different types without type checking
- Including Comparable without implementing `<=>`
- Comparing nil values in collections

## Solutions

### Solution 1: Implement <=> with Proper Type Checking

Always return `nil` from `<=>` for incomparable types, but handle that in comparisons.

```ruby
class Score
  include Comparable
  attr_reader :value

  def initialize(value)
    @value = value
  end

  def <=>(other)
    return nil unless other.is_a?(Score)
    value <=> other.value
  end
end

s1 = Score.new(90)
s2 = Score.new(85)
s1 > s2  # => true
s1 <=> "other"  # => nil
```

### Solution 2: Sort Safely with nil Values

Handle nil values in arrays before sorting or use a custom comparator.

```ruby
# BAD: raises ArgumentError
[3, 1, nil, 2].sort  # => ArgumentError: comparison of Integer with nil

# GOOD: reject nils or provide a default
[3, 1, nil, 2].compact.sort  # => [1, 2, 3]

# Or use sort_by with a default
[3, 1, nil, 2].sort_by { |n| n || 0 }  # => [nil, 1, 2, 3]

# Custom comparator for mixed types
items.sort_by { |item| item.is_a?(Numeric) ? [0, item] : [1, item.to_s] }
```

### Solution 3: Define <=> for Custom Sorted Collections

Implement the spaceship operator properly for your domain objects.

```ruby
class Product
  include Comparable
  attr_reader :name, :price

  def initialize(name, price)
    @name = name
    @price = price
  end

  def <=>(other)
    return nil unless other.is_a?(Product)
    [price, name] <=> [other.price, other.name]
  end
end

products = [
  Product.new("Widget", 25),
  Product.new("Gadget", 10),
  Product.new("Thingy", 25)
]
products.sort.map(&:name)  # => ["Gadget", "Thingy", "Widget"]
```

### Solution 4: Use Comparable Module Methods Safely

Understand what Comparable methods expect and guard against nil.

```ruby
class Version
  include Comparable
  attr_reader :major, :minor

  def initialize(major, minor)
    @major = major
    @minor = minor
  end

  def <=>(other)
    return nil unless other.is_a?(Version)
    [major, minor] <=> [other.major, other.minor]
  end

  def between?(min, max)
    (min <=> self) == 1 && (self <=> max) == 1
  end
end

v = Version.new(2, 1)
v.between?(Version.new(1, 0), Version.new(3, 0))  # => true
```

## Prevention Tips

- Always include `Comparable` and implement `<=>` for sorted objects
- Return `nil` from `<=>` for incomparable types — callers should handle this
- Use `compact` before sorting arrays that may contain nil values
- Test comparisons with mixed types to ensure graceful nil returns

## Related Errors

- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
- [TypeError]({{< relref "/languages/ruby/type-error" >}})
